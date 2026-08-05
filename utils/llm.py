import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "google/gemma-3-9b-it:free"


def generate_answer(question, context):

    prompt = f"""
You are a legal assistant.

Answer ONLY using the supplied context.

Never use outside knowledge.

If the answer cannot be found in the context,
reply exactly:

"The information is not available in the supplied documents."

Context:

{context}

Question:

{question}
"""

    try:

        response = requests.post(

            "https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },

            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            },

            timeout=60,
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:

        return f"OpenRouter Error:\n{e}"