from dotenv import load_dotenv
from groq import Groq
import os
from simple_memory import SimpleMemory
import json
from tools import Tools

load_dotenv()

MEMORY_MAX_MESSAGES = 10

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
memory = SimpleMemory(max_messages=MEMORY_MAX_MESSAGES)
agent_tools = Tools(credentials_path=os.getenv("GOOGLE_CREDENTIALS_PATH"))
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_datetime",
            "description": (
                "Obtiene la fecha y hora actual en formato RFC3339."
                "Útil para que el asistente pueda conocer la fecha y hora actual y así responder preguntas relacionadas con el tiempo"
                "o programar eventos."
            ),
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": (
                "Revisa si el calendario del usuario está disponible entre time_start y time_end."
                "Los datos time_start y time_end deben estar en el formato RFC3339 (sin incluir offset para la zona horaria),"
                "por ejemplo: 2024-01-01T10:00,"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "time_start": {
                        "type": "string",
                        "description": "La fecha de inicio para verificar la disponibilidad, en formato RFC3339 sin offset para la zona horaria."
                    },
                    "time_end": {
                        "type": "string",
                        "description": "La fecha de fin para verificar la disponibilidad, en formato RFC3339 sin offset para la zona horaria."
                    }
                },
                "required": [
                    "time_start",
                    "time_end"
                ]
            }
        }
    },
]

print("Agente de IA iniciado. Escribe 'salir' para terminar la conversación.")


def process_response(client: Groq, tools: Tools, messages: list[dict], user_input: str):
    # Agregamos el mensaje del usuario a la conversación
    messages.append(
        {"role": "user", "content": user_input},
    )

    while True:
        resp = client.chat.completions.create(
            model="qwen/qwen3-32b",
            messages=messages,
            tools=TOOLS,
        )

        msg = resp.choices[0].message

        # Si es un simple texto, lo mostramos y terminamos
        if not getattr(msg, "tool_calls", None):
            return msg.content or ""

        messages.append({
            "role": "assistant",
            "content": msg.content or "",
            "tool_calls": [tc.model_dump() for tc in msg.tool_calls]
        })

        # Si es una llamada a una herramienta:
        #  1. Ejecutamos la herramienta
        #  2. Agregamos el resultado a la conversación
        #  3. Volvemos a llamar al modelo para que genere una respuesta final
        #  4. Si es un texto lo mostramos, si es otra heramienta, repetimos el proceso.

        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments or {})

            print(
                f"Llamada a herramienta {name} con argumentos {args}")

            if name == "get_current_datetime":
                tool_response = tools.get_current_datetime()
            elif name == "check_availability":
                tool_response = tools.check_availability(
                    time_start=args.get("time_start"),
                    time_end=args.get("time_end"),
                )
            else:
                print(f"Herramienta {name} no encontrada")
                tool_response = {"error": f"Herramienta {name} no encontrada"}

            # Agregar resultado de la herramienta a la conversación
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_response, ensure_ascii=False),
            })


# Bucle principal de interacción con el usuario
while True:

    user_text = input("Tú: ").strip()

    if not user_text:
        continue

    if user_text.lower() in ["salir", "exit", "quit"]:
        print("Adiós.")
        break

    assistan_text = process_response(
        client, agent_tools, memory.messages(), user_text)
    print(f"Asistente: {assistan_text}")

    # Guardar en memoria
    memory.add(role="user", content=user_text)
    memory.add(role="assistant", content=assistan_text)
