from fastapi import FastAPI, Request, Header
from app.integrations.github import get_push_diff, post_commit_comment
from app.integrations.slack import send_slack_message
from app.tools.llm_summarizer import summarize_diff

app = FastAPI(title="Git Push Summarizer MCP Server")


@app.get("/")
def health():
    return {"status": "Git Push Summarizer is running 🚀"}


@app.post("/webhook/github")
async def github_webhook(request: Request, x_github_event: str = Header(None)):
    """
    Receives GitHub webhook events.
    On 'push': fetches diff → LLM summary → GitHub commit comment + Slack notification.
    """
    try:
        payload = await request.json()
    except Exception:
        return {"status": "ignored", "reason": "empty or invalid body"}

    # Respond to GitHub's handshake ping
    if x_github_event == "ping":
        return {"status": "pong"}

    # Handle push event
    if x_github_event == "push":
        repo = payload["repository"]["full_name"]
        branch = payload.get("ref", "").replace("refs/heads/", "")
        pusher = payload.get("pusher", {}).get("name", "unknown")
        before_sha = payload.get("before", "")
        head_commit = payload.get("head_commit", {})
        head_sha = head_commit.get("id", "")
        commit_message = head_commit.get("message", "(no message)")
        num_commits = len(payload.get("commits", []))

        if not head_sha:
            return {"status": "ignored", "reason": "no head commit"}

        # 1. Fetch unified diff between before → after
        diff = get_push_diff(repo, before_sha, head_sha)

        # 2. Generate LLM summary
        summary = summarize_diff(
            diff=diff,
            pusher=pusher,
            branch=branch,
            commit_message=commit_message,
            num_commits=num_commits,
        )

        # 3. Post as a commit comment on GitHub
        comment_body = (
            f"##  Push Summary\n\n"
            f"**Branch:** `{branch}` &nbsp;|&nbsp; "
            f"**Pushed by:** `{pusher}` &nbsp;|&nbsp; "
            f"**Commits:** {num_commits}\n\n"
            f"{summary}"
        )
        post_commit_comment(repo, head_sha, comment_body)

        # 4. Notify the team on Slack
        slack_message = (
            f"*📌New Push to `{repo}` on `{branch}`*\n"
            f"Pushed by *{pusher}* · {num_commits} commit(s)\n"
            f"Latest commit: _{commit_message}_\n\n"
            f"*Summary:*\n{summary}"
        )
        send_slack_message(slack_message)

        return {"status": "push processed", "repo": repo, "branch": branch}

    return {"status": "ignored", "event": x_github_event}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
