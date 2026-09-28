import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    base_url="https://api.xkiro.com/v1",
    api_key=os.getenv("XKIRO_API_KEY")
)


def ask_ai(question):
    response = client.chat.completions.create(
        model="qwen/qwen3.6-27b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content


while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_ai(question)

    print("\nAI:", answer)