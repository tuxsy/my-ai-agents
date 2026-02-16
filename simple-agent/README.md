# Simple Agent

Un chatbot de linea de comandos simple que usa la API de Groq para responder preguntas. Incluye un sistema de memoria para mantener el contexto de la conversacion.

## Requisitos

- Python 3.9 o superior

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

3. (Opcional) Para usar la integracion con Google Calendar, agrega la ruta a tus credenciales:
   ```
   GOOGLE_CREDENTIALS_PATH=ruta/a/credentials.json
   ```

## Uso

```bash
python agent.py
```

Escribe tus mensajes y recibe respuestas. Para salir, escribe `exit`, `quit` o `salir`.

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
