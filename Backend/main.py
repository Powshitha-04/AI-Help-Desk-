from fastapi import FastAPI
from pydantic import BaseModel
from AI_classifier import analyze_ticket

app = FastAPI()

class TicketRequest(BaseModel):
    short_description: str
    description: str

@app.get("/")
def root():
    return {"status": "AI Helpdesk backend is running"}

@app.post("/analyze")
def analyze(data: TicketRequest):
    combined_text = f"{data.short_description}\n{data.description}"
    result = analyze_ticket(combined_text)
    return result