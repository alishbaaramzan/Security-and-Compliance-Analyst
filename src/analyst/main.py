import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .agent import SecurityAnalyst


app = FastAPI(title="AI Security Analyst")

analyst = SecurityAnalyst()

WEB_DIR = Path(__file__).parent / "web"


class AssessmentRequest(BaseModel):
    use_case: dict


@app.get("/")
def index():
    return FileResponse(WEB_DIR / "index.html")


@app.post("/assess")
def assess(request: AssessmentRequest):
    try:
        assessment = analyst.assess(request.use_case)

        return assessment.model_dump()

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


app.mount(
    "/static",
    StaticFiles(directory=WEB_DIR),
    name="static",
)