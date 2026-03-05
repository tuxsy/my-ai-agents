# Agente de Clima con Memoria

Este proyecto es un agente de IA que utiliza la API de Groq para interactuar con los usuarios en español. El agente puede responder preguntas sobre el clima de cualquier ciudad (con datos simulados) y mantiene un historial reciente de la conversación para ofrecer respuestas contextuales.

## Requisitos

- Python 3.9 o superior (determinado por el uso de anotaciones de tipo genéricas como `list[dict]`)

## Tecnologías

- Python
- Groq Cloud API
- python-dotenv (gestión de variables de entorno)

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar las variables de entorno:
   Crear un archivo `.env` en el directorio raíz y añadir su clave de API:
   ```env
   GROQ_API_KEY=su_clave_aqui
   ```

## Uso

Para iniciar el agente, ejecute el script principal:
```bash
python agent.py
```
Escriba "salir" o "exit" para terminar la sesión.

## Nota para desarrolladores

Este proyecto utiliza `pigar` para generar y mantener actualizado el archivo `requirements.txt` automáticamente basándose en las importaciones del código.

Para actualizar el archivo de dependencias:
```bash
pigar generate
```

Modificado por claude-sonnet-4.6 (sin razonamiento)