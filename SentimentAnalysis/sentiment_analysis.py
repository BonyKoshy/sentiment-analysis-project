from optimum.intel import OVModelForSequenceClassification
from transformers import AutoTokenizer, pipeline
import openvino.runtime as ov

# 1. Define Static Shapes (NPU Requirement)
# We force the model to expect exactly 1 sentence of 128 tokens.
STATIC_BATCH_SIZE = 1
STATIC_SEQUENCE_LENGTH = 128

model_id = "distilbert-base-uncased-finetuned-sst-2-english"

try:
    print("DEBUG: Loading model...")
    # Load the model (export=True converts it to OpenVINO format)
    model = OVModelForSequenceClassification.from_pretrained(
        model_id, 
        export=True,
        compile=False # Don't compile yet, we need to reshape first!
    )
    
    # 2. Reshape to Static Dimensions
    # This tells OpenVINO: "Input will ALWAYS be [1, 128]"
    print(f"DEBUG: Reshaping model to static shape [{STATIC_BATCH_SIZE}, {STATIC_SEQUENCE_LENGTH}] for NPU...")
    model.reshape(batch_size=STATIC_BATCH_SIZE, sequence_length=STATIC_SEQUENCE_LENGTH)
    
    # 3. Compile for NPU
    print("DEBUG: Compiling model for NPU...")
    model.to("NPU")
    model.compile()
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    print("DEBUG: SUCCESS! Model loaded on NPU with static shapes.")

except Exception as e:
    print(f"DEBUG: NPU Load Failed. Error: {e}")
    print("DEBUG: Falling back to CPU.")
    model = OVModelForSequenceClassification.from_pretrained(model_id, export=True)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model.to("CPU")

def sentiment_analyzer(text_to_analyse):
    # 4. Preprocess Input to Match Static Shape
    # We must manually tokenize to ensure strict padding/truncation to 128
    encoded_input = tokenizer(
        text_to_analyse, 
        return_tensors="pt", 
        padding="max_length", 
        truncation=True, 
        max_length=STATIC_SEQUENCE_LENGTH
    )
    
    # Run inference directly on the model (pipeline handles this differently, direct call is safer for static NPU)
    output = model(**encoded_input)
    
    # Extract logits to determine label
    logits = output.logits[0]
    
    # Simple logic: Index 1 is usually Positive, Index 0 is Negative for this specific model
    # (We use .item() to get the float value)
    score = float(logits.softmax(dim=0).max())
    label_idx = logits.argmax().item()
    
    # Map index to label (distilbert-sst-2 uses: 0=NEGATIVE, 1=POSITIVE)
    label = "SENT_POSITIVE" if label_idx == 1 else "SENT_NEGATIVE"
    
    return {'label': label, 'score': score}