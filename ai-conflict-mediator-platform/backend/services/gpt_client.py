import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_message(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a conflict mediator assistant."},
                {"role": "user", "content": f"Rewrite this message in a calm, professional, and neutral tone:\n\n{message}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print("Error calling OpenAI API:", e)
        return "Unable to rewrite message due to an error."
