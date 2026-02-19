import requests
import os


def get_changed_files(repo_full_name: str, pr_number: int) -> list[str]:
    """Fetch the list of changed file paths for a given PR from GitHub API."""
    headers = {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json"
    }
    files_url = f"https://api.github.com/repos/{repo_full_name}/pulls/{pr_number}/files"
    response = requests.get(files_url, headers=headers)
    response.raise_for_status()
    return [f["filename"] for f in response.json()]


def handle_pull_request_event(payload):
    action = payload["action"]

    if action != "opened":
        return

    pr_number = payload["pull_request"]["number"]
    repo_full_name = payload["repository"]["full_name"]

    changed_files = get_changed_files(repo_full_name, pr_number)

    # Choose template
    from app.tools.pr_template import suggest_pr_template
    template_name = suggest_pr_template(changed_files)

    # Read template from prompts folder
    template_path = os.path.join("app", "prompts", template_name)
    with open(template_path, "r") as f:
        template_content = f.read()

    # Update PR body via GitHub API
    headers = {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json"
    }
    update_url = f"https://api.github.com/repos/{repo_full_name}/pulls/{pr_number}"
    requests.patch(update_url, headers=headers, json={"body": template_content})
