import pymupdf
from langchain.agents import create_agent
from app.schemas.models import ResumeAnalysis
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

def extract_text(pdf_path: str) -> str:
    """Extract text from a PDF. Raises on failure instead of returning an error string."""
    doc = pymupdf.open(pdf_path)
    try:
        return "".join(page.get_text() for page in doc)
    finally:
        doc.close()



def build_prompt(resume_text: str) -> str:
    return f"""
Analyze this resume:
{resume_text}

Return:
1. Summary of the resume.
2. Skills mentioned in the resume.
3. Suitable job roles according to the resume.
4. Interview questions.
"""


def analyze_resume(pdf_path: str) -> tuple[ResumeAnalysis, dict]:
    # LangChain reads OPENAI_API_KEY from the environment automatically.
    # Make sure it's set before running; fail early with a clear message if not.
    
    resume_text = extract_text(pdf_path)

    agent = create_agent(model="gpt-5", response_format=ResumeAnalysis)
    result = agent.invoke(
        {"messages": [{"role": "user", "content": build_prompt(resume_text)}]}
    )

    ai_message = result["messages"][-1]
    structured: ResumeAnalysis = result["structured_response"]
    return {
    "analysis": structured,
    "usage": ai_message.usage_metadata
}

if __name__ == "__main__":
    pass
    # result = analyze_resume(r"")

    # print(result)