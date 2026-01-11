from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ClarificationOutput(BaseModel):
    clarifying_questions: List[str] = Field(..., max_items=8)
    assumptions: List[str]
    interpreted_requirement: str


class DataSpec(BaseModel):
    schema: Dict[str, Any]
    version: str
    domain: str


class WorkflowSpec(BaseModel):
    prompt: str
    steps: List[str]
    rubric: Dict[str, str]
    max_time_minutes: int = 6


class QAPlan(BaseModel):
    automated_checks: List[str]
    sampling_strategy: str
    pii_handling: str


class LearnerResponse(BaseModel):
    responses: Dict[str, Any]
