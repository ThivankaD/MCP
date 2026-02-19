import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message: str):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, json=payload)
