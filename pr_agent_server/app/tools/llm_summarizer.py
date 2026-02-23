import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL = "Qwen/Qwen2.5-72B-Instruct"

# Initialise the HuggingFace Inference client once at import time
_client = InferenceClient(token=HF_API_KEY)

SYSTEM_PROMPT = """\
You are a senior software engineer writing concise, developer-friendly commit summaries.
Given a git diff (and some context), produce a short summary (3-6 bullet points) that explains:
- What files/components were changed
- What the changes do (not HOW — assume the reader can read code)
- Any notable additions, deletions, or refactors

Keep the language clear and professional. Use markdown bullet points (•).
Do NOT reproduce the raw diff. Do NOT add filler phrases like "In this commit...".
"""


def summarize_diff(
    diff: str,
    pusher: str = "",
    branch: str = "",
    commit_message: str = "",
    num_commits: int = 1,
) -> str:
    """
    Use Qwen2.5-72B-Instruct via HuggingFace Inference API to summarise a git diff.
    """
    user_message = (
        f"**Push context**\n"
        f"- Branch: {branch}\n"
        f"- Pushed by: {pusher}\n"
        f"- Commits: {num_commits}\n"
        f"- HEAD commit message: {commit_message}\n\n"
        f"**Git diff:**\n```diff\n{diff}\n```\n\n"
        f"Please summarise the changes made in this push."
    )

    try:
        response = _client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=512,
            temperature=0.3,
        )
        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        print(f"[LLM] HuggingFace inference error: {e}")
        return (
            f"⚠️ Could not generate AI summary (error: {e}).\n\n"
            f"HEAD commit: _{commit_message}_"
        )
