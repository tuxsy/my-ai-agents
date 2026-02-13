# Simple Agent

Un chatbot de linea de comandos simple pero con actitud. Este agente usa la API de Groq para responder preguntas de manera util pero con personalidad "maleducada".

## Requisitos

- Python 3.9 o superior

## Tecnologias

- **Python** - Lenguaje principal
- **Groq API** - Inferencia rapida de LLMs
- **Qwen3-32B** - Modelo de lenguaje utilizado
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
