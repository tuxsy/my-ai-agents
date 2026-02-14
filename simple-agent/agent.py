from dotenv import load_dotenv
from groq import Groq
import os
from simple_memory import SimpleMemory

load_dotenv()

MEMORY_MAX_MESSAGES = 10

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
memory = SimpleMemory(max_messages=MEMORY_MAX_MESSAGES)

print("Agente de IA maleducado")

while True:

    user_text = input("Tú: ").strip()

    if not user_text:
        continue

    if user_text.lower() in ["salir", "exit", "quit"]:
        print("Adiós.")
        break

    # Leer memoria
    messages = memory.messages()
    messages.append(
        {"role": "user", "content": user_text},
    )

    resp = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=messages,
    )

    msg = resp.choices[0].message
    assistan_text = msg.content or ""

    print(f"Asistente: {assistan_text}")

    # Guardar en memoria
    memory.add(role="user", content=user_text)
    memory.add(role="assistant", content=assistan_text)

