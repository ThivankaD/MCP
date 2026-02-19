from fastapi import FastAPI, Request, Header
from app.tools.pr_template import suggest_pr_template
from app.tools.ci_summary import summarize_ci
from app.integrations.github import get_changed_files
from app.integrations.slack import send_slack_message

app = FastAPI(title="PR Agent Workflow Server")

@app.get("/")
def health():
    return {"status": "PR Agent Running"}

@app.post("/webhook/github")
async def github_webhook(request: Request, x_github_event: str = Header(None)):
    payload = await request.json()

    # PR Event
    if x_github_event == "pull_request":
        pr = payload["pull_request"]
        repo = payload["repository"]["full_name"]
        pr_number = pr["number"]
        author = pr["user"]["login"]

        changed_files = get_changed_files(repo, pr_number)
        template = suggest_pr_template(changed_files)

        message = f"""
🚀 New PR #{pr_number} by {author}
📁 Suggested Template: {template}
Files Changed:
{chr(10).join(changed_files)}
"""

        send_slack_message(message)

        return {"status": "PR processed"}

    # CI Event
    if x_github_event == "workflow_run":
        workflow = payload["workflow_run"]["name"]
        status = payload["workflow_run"]["conclusion"]

        summary = summarize_ci(workflow, status)

        send_slack_message(f"⚙️ CI Update:\n{summary}")

        return {"status": "CI processed"}

    return {"status": "ignored"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
