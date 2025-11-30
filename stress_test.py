import requests
import time
import concurrent.futures

# The confusing passage from above
PASSAGE = """The breathtaking speed at which this system achieves absolute failure is truly a marvel of modern engineering, surpassing all expectations of incompetence. While the interface is delightfully colorful, it serves only to highlight the catastrophic underlying logic that renders the user experience a joyful nightmare of frustration. I am not unhappy with the effort, but I am certainly not pleased with the disaster that is the result. It works perfectly at being imperfect, a flawless execution of flawed design. To say I hate it would be an understatement, yet to say I like it would be a lie; it exists in a quantum state of magnificent failure and terrible success."""

url = "http://127.0.0.1:5000/sentimentAnalyzer"
params = {'textToAnalyze': PASSAGE}

def send_request(i):
    try:
        # We don't print the result to save console time, just hit the NPU
        requests.get(url, params=params)
    except Exception as e:
        print(f"Request failed: {e}")

print("Starting NPU Stress Test... (Press Ctrl+C to stop)")
print("Check your Task Manager > Performance > Intel NPU now.")

# We use a thread pool to send many requests at once, 
# ensuring the NPU always has a queue of work.
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    count = 0
    while True:
        # Schedule 50 requests at a time
        futures = [executor.submit(send_request, count + i) for i in range(50)]
        concurrent.futures.wait(futures)
        count += 50
        if count % 100 == 0:
            print(f"Processed {count} requests...")