import os
import google.generativeai as genai
from dotenv import load_dotenv
from config import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

def analyze(log_data):
    prompt = PROMPT.format(log_data=log_data)
    response = model.generate_content(prompt)
    return response.text
