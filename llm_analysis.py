import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs(log_text):
    if not log_text.strip():
        return " No logs to analyze."

    prompt = f"""
Analyze these logs to identify the possible cause of high CPU usage.
Provide a clear reason if identifiable.

Logs:
{log_text[:10000]}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.3
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f" OpenAI error: {e}"

