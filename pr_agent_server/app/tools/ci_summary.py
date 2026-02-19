def summarize_ci(workflow: str, status: str) -> str:
    """
    Generate a human-readable CI summary message.
    """
    status_emoji = {
        "success": "✅",
        "failure": "❌",
        "cancelled": "🚫",
        "skipped": "⏭️",
    }.get(status, "❓")

    return f"{status_emoji} Workflow '{workflow}' completed with status: **{status}**"
