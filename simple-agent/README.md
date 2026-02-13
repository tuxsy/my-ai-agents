# Simple Agent

Un chatbot de línea de comandos simple pero con actitud. Este agente usa la API de Groq para responder tus preguntas de manera útil... aunque un poco maleducada.

## Qué hace

Es un asistente conversacional que:
- Responde preguntas y ayuda con tareas
- Tiene una personalidad "maleducada" (es útil pero gruñón)
- Funciona en la terminal con una interfaz simple

## Requisitos

- **Python 3.9+**

## Tecnologías

- **Python** - Lenguaje principal
- **Groq API** - Para inferencia rápida de LLMs
- **Qwen3-32B** - El modelo de lenguaje utilizado

## Instalación

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Crea un archivo `.env` con tu API key de Groq:
   ```
   GROQ_API_KEY=tu_api_key_aqui
   ```

## Uso

```bash
python agent.py
```

Escribe tus mensajes y recibe respuestas (algo groseras pero útiles). Para salir, escribe `exit`, `quit` o `salir`.

---

## Nota para desarrolladores

Este proyecto usa [pigar](https://github.com/damnever/pigar) para gestionar el archivo `requirements.txt`.

### Instalar pigar

```bash
pip install pigar
```

### Actualizar requirements.txt

Cuando añadas o elimines dependencias en el código, ejecuta:

```bash
pigar generate
```

Esto analizará los imports del proyecto y actualizará `requirements.txt` automáticamente con las versiones correctas.

### Actualizar README

Este proyecto incluye un comando de OpenCode para mantener el README actualizado. Desde OpenCode, ejecuta:

```
/update-readme
```

El comando analizará el proyecto y regenerará el README con la estructura y contenido actualizados.
