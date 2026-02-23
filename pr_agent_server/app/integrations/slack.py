import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_slack_message(message: str) -> bool:
    """
    Send a message to the configured Slack channel via Incoming Webhook.
    Returns True on success, False on failure.
    """
    if not SLACK_WEBHOOK_URL:
        print("[Slack] SLACK_WEBHOOK_URL is not set — skipping notification.")
        return False

    try:
        response = requests.post(
            SLACK_WEBHOOK_URL,
            json={"text": message},
            timeout=10,
        )
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"[Slack] Failed to send message: {e}")
        return False
