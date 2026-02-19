import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_llm(prompt: str):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.3
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        return f"LLM Error: {response.text}"
    
    return response.json()[0]["generated_text"]
