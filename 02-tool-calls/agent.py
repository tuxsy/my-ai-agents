from dotenv import load_dotenv
from groq import Groq
import os
from simple_memory import SimpleMemory
import json
from tools import Tools
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

MEMORY_MAX_MESSAGES=10

api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)
memory = SimpleMemory(max_messages=MEMORY_MAX_MESSAGES)
now = datetime.now(ZoneInfo("America/Monterrey"))
SYSTEM_PROMPT = f"""
Eres un asistente que habla en español y responde de manera muy breve y concisa.

Reglas:
- Antes de crear una reunión, SIEMPRE debes pedir confirmación explícita del usuario.
- Si el usuario no confirma, NO llames create_event.

Fecha y hora actual:
{now.strftime("%Y-%m-%d %H:%M:%S")} (UTC-6, hora local)
"""
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": (
                "Revisa si el calendario del usuario está disponible entre time_ini y time_end "
                "usando Google Calendar. Los datos time_ini y time_end DEBEN estar en el formato "
                "RFC3339 (con offset para la zona horaria). Por ejemplo: "
                "2025-12-30T10:00:00-06:00"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "time_ini": {
                        "type": "string",
                        "description": "La fecha de inicio para revisar disponibilidad en formato RFC3339"
                    },
                    "time_end": {
                        "type": "string",
                        "description": "La fecha fin para revisar disponibilidad en formato RFC3339"
                    }
                },
                "required": ["time_ini", "time_end"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_event",
            "description": (
                "Crea un evento (reunión) en Google Calendar. "
                "start y end DEBEN estar en RFC3339 con offset."
                "Ejemplo: 2025-12-30T10:00:00-06:00"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "Título de la reunión"},
                    "start": {"type": "string", "description": "Fecha de inicio en formato RFC3339"},
                    "end": {"type": "string", "description": "Fecha fin en formato RFC3339"},
                    "description": {"type": "string", "description": "Descripción de la reunión (opcional)"}
                },
                "required": ["summary", "start", "end"]
            }
        }
    }
]

print("Agente de IA")

def process_response(client:Groq, memory_messages: list[dict], user_text:str):
    #Obtener la memoria
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(memory_messages)
    messages.append({"role": "user", "content": user_text})
    
    while True:
        resp = client.chat.completions.create(
            model="qwen/qwen3-32b",
            messages=messages,
            tools=TOOLS
        )

        msg = resp.choices[0].message
        
        #Si no hay llamados a herramientas, entonces ya regresamos la respuesta
        if not getattr(msg, "tool_calls", None):
            return msg.content or ""
        
        messages.append({
            "role": "assistant",
            "content": msg.content or "",
            "tool_calls": [tc.model_dump() for tc in msg.tool_calls]
        })
        
        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments or "{}")
            
            if name == "check_availability":
                tools = Tools()
                result = tools.check_availability(
                    time_ini=args["time_ini"],
                    time_end=args["time_end"]
                )
            elif name == "create_event":
                tools = Tools()
                result = tools.create_event(
                    summary=args["summary"],
                    start=args["start"],
                    end=args["end"],
                    description=args.get("description", "")
                )
            else:
                print(f"Se intentó llamar a una herramienta desconocida {name}")
                result = {"error": f"Herramienta desconocida: {name}"}
                
            #Agregar a los mensajes el resultao del llamado de la herramienta.
            #Esto lo recibirá el modelo al continuar la iteración
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, ensure_ascii=False)
            })

while True:
    
    user_text = input("Tú: ").strip()
    if not user_text:
        continue
    
    if user_text.lower() in ("exit", "salir"):
        print("Hasta luego!")
        break
    
    assistant_text = process_response(client, memory.messages(), user_text)
    print(f"Asistente: {assistant_text}")
    
    #Actualizar la memoria
    memory.add("user", user_text)
    memory.add("assistant", assistant_text)