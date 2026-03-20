from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("QWEN_API_KEY")
base_url = os.getenv("QWEN_BASE_URL", "https://api.aitunnel.ru/v1")

if not api_key:
    print("API Key not found!")
else:
    client = OpenAI(api_key=api_key, base_url=base_url)
    try:
        print(f"Connecting to {base_url}...")
        models = client.models.list()
        print("Available models:")
        for m in models.data:
            print(m.id)
    except Exception as e:
        print(f"Error: {e}")
