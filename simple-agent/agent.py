from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

print("Agente de IA maleducado")

while True:

    user_text = input("Tú: ").strip()

    if not user_text:
        continue

    if user_text.lower() in ["salir", "exit", "quit"]:
        print("Adiós.")
        break

    messages = [
        {"role": "system",
            "content": "Eres un asistente de IA muy maleducado y respondes de forma útil pero desagradable."},
        {"role": "user", "content": user_text},
    ]

    resp = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=messages,
    )

    msg = resp.choices[0].message
    assistan_text = msg.content or ""

    print(f"Asistente: {assistan_text}")

