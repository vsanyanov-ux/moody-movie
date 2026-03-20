from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("QWEN_API_KEY")
base_url = os.getenv("QWEN_BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)

models_to_try = [
    "qwen2.5-3b-instruct",
    "qwen/qwen2.5-3b-instruct",
    "qwen-2.5-3b-instruct",
    "qwen2-3b-instruct",
    "qwen-3b"
]

for model in models_to_try:
    print(f"Testing {model}...")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "hi"}],
            max_tokens=5
        )
        print(f"  SUCCESS: {response.choices[0].message.content}")
        break
    except Exception as e:
        print(f"  FAILED: {e}")
