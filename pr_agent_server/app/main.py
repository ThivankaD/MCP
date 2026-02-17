from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.tools.pr_template import suggest_pr_template  # your tool

app = FastAPI(title="PR Agent Workflow Server")

# Pydantic model
class PRRequest(BaseModel):
    changed_files: List[str]

# Health check
@app.get("/")
def health_check():
    return {"status": "PR Agent MCP Server Running"}

# POST endpoint with JSON body
@app.post("/analyze-pr")
async def analyze_pr(data: PRRequest):
    """
    Analyze PR and suggest a template based on changed files.
    """
    template = suggest_pr_template(data.changed_files)
    return {"suggested_template": template}
