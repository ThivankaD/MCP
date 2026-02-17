def suggest_pr_template(changed_files: list[str]) -> str:
    """
    Select PR template based on changed files.
    """

    if any("frontend" in f for f in changed_files):
        return "frontend-template.md"

    if any("api" in f for f in changed_files):
        return "backend-template.md"

    if any("ml" in f or "model" in f for f in changed_files):
        return "llm-template.md"

    if any(".github/workflows" in f for f in changed_files):
        return "devops-template.md"

    return "general-template.md"
