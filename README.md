# Local AI Sentiment Analysis (Optimized for Intel NPU)

## Overview

This project is a high-performance, privacy-focused web application that performs sentiment analysis on user-provided text. Unlike traditional cloud-based solutions, this application **runs entirely locally** on your machine.

It leverages **Hugging Face Transformers** and **Intel OpenVINO™** to run a BERT-based model directly on your hardware. It is specifically optimized to utilize **Intel NPUs (Neural Processing Units)** for high-speed, low-power inference, with automatic fallbacks to GPU or CPU.

## Key Features

-   **🚀 Local AI Engine**: Replaces external APIs with a local `distilbert-base-uncased-finetuned-sst-2-english` model. Zero latency from network requests and fully offline capable.
-   **⚡ Intel NPU Acceleration**: Uses the `optimum-intel` library to compile and run the model on Intel NPUs (13+ TOPS), freeing up your CPU and GPU for other tasks.
-   **🔒 Privacy First**: Your data never leaves your computer. All analysis happens on-device.
-   **🛠 Robust Engineering**: Implements **Static Shape** optimization (batch size 1, sequence length 128) to ensure compatibility with strict NPU driver requirements.
-   **💻 Modern Web Interface**: A responsive frontend built with HTML5, Bootstrap 5, and JavaScript that communicates asynchronously with the Flask backend.

## Technologies Used

-   **Backend**: Python, Flask
-   **AI Frameworks**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/index), [Intel OpenVINO™](https://docs.openvino.ai/), [Optimum Intel](https://huggingface.co/docs/optimum/intel/index)
-   **Model**: DistilBERT (SST-2 Fine-tuned)
-   **Frontend**: HTML, JavaScript (Fetch API), Bootstrap
-   **Testing**: Python `unittest`, `pylint`

## Prerequisites

-   **Python 3.8** or higher.
-   **Intel NPU Drivers**: Required if you intend to use the NPU. Ensure your Intel NPU drivers are up to date (download from Intel or your device manufacturer).
-   **Visual C++ Redistributable**: Often required for OpenVINO on Windows.

## Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/BonyKoshy/sentiment-analysis-project.git
    cd sentiment-analysis-project
    ```

2.  **Create a Virtual Environment**
    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    
    # Activate on Windows:
    venv\Scripts\activate
    
    # Activate on macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install the required packages for Flask and Intel OpenVINO support.
    ```bash
    pip install flask pylint transformers torch optimum[openvino]
    ```

## Running the Application

1.  **Start the Server**
    Run the Flask server script. On the first run, it will download the AI model and compile it for your specific hardware (this may take a minute).
    ```bash
    python server.py
    ```
    *Watch the console logs: You should see messages confirming "Model loaded on NPU" if your hardware is detected correctly.*

2.  **Access the Web Interface**
    Open your browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

3.  **Analyze Text**
    Type any sentence into the text box and click "Analyze Sentiment". 
    - **Green Result**: Positive Sentiment
    - **Red Result**: Negative Sentiment
    - **Grey Result**: Neutral (or low confidence)

## Troubleshooting

### NPU Not Detected?
If the console says "Falling back to CPU," ensure you have the `optimum[openvino]` package installed and your Intel NPU drivers are current.

### "Dynamic Shapes" Error
The Intel NPU requires **Static Shapes** (fixed input sizes). This project is pre-configured to reshape the model to `[1, 128]`.
- If you modify the code and see `ZE_RESULT_ERROR_INVALID_ARGUMENT`, ensure you are not passing variable-length inputs to the model.
- The `sentiment_analysis.py` file handles this automatically by padding inputs to exactly 128 tokens.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
