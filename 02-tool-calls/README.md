# Agente con Llamada a Herramientas (Tool Calls)

Este proyecto implementa un agente de inteligencia artificial capaz de interactuar con el calendario de Google mediante el uso de herramientas (tool calls). El agente puede verificar disponibilidad y crear eventos en el calendario basándose en las peticiones del usuario en lenguaje natural.

## Requisitos

- Python 3.9 o superior (requerido para el módulo `zoneinfo`)
- Una cuenta de Google con la API de Google Calendar habilitada
- Credenciales de Groq API

## Tecnologías

- Python
- Groq Cloud API (Modelo: qwen/qwen3-32b)
- Google Calendar API
- python-dotenv
- google-api-python-client
- google-auth-oauthlib

## Instalación

1. Clona el repositorio y navega al directorio del proyecto.
2. Instala las dependencias necesarias:
   ```bash
   pip install python-dotenv groq google-api-python-client google-auth-oauthlib
   ```
3. Configura las variables de entorno:
   - Crea un archivo `.env` y añade tu `GROQ_API_KEY`.
4. Configura las credenciales de Google:
   - Descarga tu archivo `credentials.json` desde la consola de Google Cloud y colócalo en la raíz de este directorio.

## Uso

Para ejecutar el agente, utiliza el siguiente comando:

```bash
python agent.py
```

El agente solicitará autorización a través del navegador la primera vez que se ejecute para generar el archivo `token.json`.

## Nota para desarrolladores

Se utiliza `pigar` para mantener actualizado el archivo `requirements.txt`. Para generar o actualizar las dependencias, utiliza:

```bash
pigar generate
```

Modificado por gemini-3-flash-preview (github-copilot)
