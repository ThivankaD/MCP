import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_push_diff(repo_full_name: str, base_sha: str, head_sha: str) -> str:
    """
    Fetch the unified diff between two commits using the GitHub Compare API.
    Returns the raw diff string (truncated to 6000 chars to stay within LLM limits).
    """
    url = f"https://api.github.com/repos/{repo_full_name}/compare/{base_sha}...{head_sha}"
    headers = {**_HEADERS, "Accept": "application/vnd.github.v3.diff"}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        diff_text = response.text

        # Truncate very large diffs to avoid LLM token limits
        max_chars = 6000
        if len(diff_text) > max_chars:
            diff_text = diff_text[:max_chars] + "\n\n... [diff truncated for length] ..."

        return diff_text if diff_text.strip() else "(no diff available)"

    except requests.RequestException as e:
        return f"(could not fetch diff: {e})"


def post_commit_comment(repo_full_name: str, commit_sha: str, body: str) -> bool:
    """
    Post a comment on a specific commit via the GitHub Commits API.
    Returns True on success, False on failure.
    """
    url = f"https://api.github.com/repos/{repo_full_name}/commits/{commit_sha}/comments"

    try:
        response = requests.post(url, headers=_HEADERS, json={"body": body}, timeout=15)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"[GitHub] Failed to post commit comment: {e}")
        return False
