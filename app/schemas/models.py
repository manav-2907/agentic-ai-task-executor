from pydantic import BaseModel
from typing import List


class ResumeAnalysis(BaseModel):
    summary: str
    skills: List[str]
    suggested_roles: List[str]
    interview_questions: List[str]