import os
from dotenv import load_dotenv
import google.generativeai as genai
from config import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

def analyze(data):
    prompt = PROMPT.format(log_data=data)
    response = model.generate_content(prompt)
    return response.text
