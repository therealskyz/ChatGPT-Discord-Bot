from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def chatgpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
