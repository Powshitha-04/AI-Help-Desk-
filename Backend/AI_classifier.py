from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def analyze_ticket(ticket_text):
    prompt = f"""
You are an IT helpdesk AI assistant.
Analyze the IT support issue below and return ONLY a valid JSON object.
No explanation. No markdown. No extra text. Just the JSON.

Required fields:
- category (one of: Network, Hardware, Security, Software)
- priority (one of: Low, Medium, High, Critical)
- assignment_group (one of: Network Team, Hardware Team, Security Team, Software Team, IT Support)
- solution (a short suggested fix, 1-2 sentences)

Issue:
{ticket_text}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)