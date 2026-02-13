# Simple Chatbot Agent

A basic conversational AI agent that demonstrates rule-based pattern matching and context management.

## Features
- Pattern-based response generation
- Conversation context tracking
- Interactive chat interface

## Usage

```python
from agents.chatbot.simple_chatbot import SimpleChatbot

# Create a chatbot instance
chatbot = SimpleChatbot(name="MyBot")

# Get responses
response = chatbot.respond("Hello")
print(response)
```

## Running Interactively

```bash
python agents/chatbot/simple_chatbot.py
```

## Example Conversation

```
ChatBot: Hello! I'm a simple chatbot. Type 'quit' to exit.
You: hello
ChatBot: Hi there!
You: how are you
ChatBot: I'm doing great, thanks for asking!
You: bye
ChatBot: Goodbye!
```
