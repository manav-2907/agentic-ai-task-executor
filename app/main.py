from fastapi import FastAPI
from app.routes.resume import router as resume_router

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Agentic ai task executor"}

app.include_router(resume_router)
