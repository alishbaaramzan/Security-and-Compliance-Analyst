from typing import Literal

from pydantic import BaseModel


Status = Literal["PASS", "FAIL", "UNKNOWN"]


class RequirementAssessment(BaseModel):
    requirement_id: str
    status: Status
    reasoning: str
    evidence: str
    recommended_action: str


class Assessment(BaseModel):
    overall_status: Literal["PASS", "REVIEW_REQUIRED"]
    assessments: list[RequirementAssessment]
    risks: list[str]
    recommended_actions: list[str]