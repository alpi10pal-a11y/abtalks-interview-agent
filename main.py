import json
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

# Load curriculum and candidate data
curriculum = json.load(open(Path("data/curriculum.json")))
candidate = json.load(open(Path("data/candidate.json")))

@app.get("/")
def root():
    return {"message": "Hello ALPI, FastAPI is working!"}

@app.post("/api/interview/start")
def start_interview():
    return {
        "message": f"Interview started for {candidate['name']}",
        "questions": curriculum["topics"][0]["questions"]
    }

@app.post("/api/interview/answer")
def answer_interview(answer: str):
    return {
        "message": f"Received answer: {answer}",
        "next_question": curriculum["topics"][1]["questions"][0]
    }

@app.get("/api/interview/feedback")
def feedback():
    return {
        "strengths": candidate["skills"],
        "weaknesses": ["Needs more practice with ML"],
        "next_steps": ["Revise supervised vs unsupervised learning"]
    }
