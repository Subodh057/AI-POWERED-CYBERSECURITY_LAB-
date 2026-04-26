import os
from dotenv import load_dotenv
import google.generativeai as genai
from config import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

def analyze(data):
    try:
        prompt = PROMPT.format(log_data=data)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"""
AI analysis unavailable due to API/quota error.

Fallback SOC Analysis:
- Snort generated alerts successfully.
- Triage logic processed the alert.
- Review alerts/alerts.json for severity.
- Investigate source IP, destination IP, ports, and alert message.

Error:
{str(e)}
"""
