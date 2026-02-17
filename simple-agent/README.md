# Simple Agent

Un chatbot de linea de comandos simple que usa la API de Groq para responder preguntas. Incluye un sistema de memoria para mantener el contexto de la conversacion (hasta 10 mensajes).

## Requisitos

- Python 3.9 o superior (requerido por el modulo `zoneinfo`)

## Tecnologias

- **Python** - Lenguaje principal
- **Groq API** - Inferencia rapida de LLMs
- **qwen/qwen3-32b** - Modelo de lenguaje utilizado
- **Google Calendar API** - Integracion con calendario
- **python-dotenv** - Gestion de variables de entorno

## Instalacion

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Crea un archivo `.env` con tu API key de Groq:
   ```
   GROQ_API_KEY=tu_api_key_aqui
   ```

3. Para usar la integracion con Google Calendar, agrega la ruta a tus credenciales (requerido actualmente):
   ```
   GOOGLE_CREDENTIALS_PATH=ruta/a/credentials.json
   ```

## Uso

```bash
python agent.py
```

Escribe tus mensajes y recibe respuestas. Para salir, escribe `exit`, `quit` o `salir`.

## Herramientas

El agente tiene acceso a las siguientes herramientas que puede invocar automaticamente segun el contexto de la conversacion:

- **get_current_datetime** - Obtiene la fecha y hora actual. Util para preguntas relacionadas con el tiempo o para programar eventos.
- **check_availability** - Verifica la disponibilidad en Google Calendar para un rango de fechas. Usa la zona horaria `Europe/Madrid` por defecto.

El token de autenticacion de Google se almacena en el directorio `.temp/`.

## Nota para desarrolladores

Este proyecto usa [pigar](https://github.com/damnever/pigar) para gestionar el archivo `requirements.txt`.

### Instalar pigar

```bash
pip install pigar
```

### Actualizar requirements.txt

Cuando modifiques las dependencias en el codigo, ejecuta:

```bash
pigar generate
```

Esto analiza los imports del proyecto y actualiza `requirements.txt` con las versiones correctas.

---

Modificado por Gemini 3 Pro (con razonamiento)
