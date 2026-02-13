# my-ai-agents

A collection of example AI agents demonstrating different capabilities and use cases.

## Overview

This repository contains examples of AI agents that demonstrate various patterns and capabilities:

- **Chatbot Agent**: Conversational AI with pattern matching
- **Task Automation Agent**: Scheduled task execution and management
- **Data Analysis Agent**: Statistical analysis and insights
- **Code Assistant Agent**: Code analysis and improvement suggestions

## Agents

### 1. Simple Chatbot Agent
Location: `agents/chatbot/`

A rule-based conversational agent that demonstrates:
- Pattern-based response generation
- Context tracking
- Interactive chat interface

```bash
python agents/chatbot/simple_chatbot.py
```

### 2. Task Automation Agent
Location: `agents/task_automation/`

An agent for scheduling and executing automated tasks:
- Interval-based task scheduling
- Task execution tracking
- Status monitoring

```bash
python agents/task_automation/task_agent.py
```

### 3. Data Analysis Agent
Location: `agents/data_analysis/`

Statistical analysis agent with capabilities:
- Descriptive statistics (mean, median, mode, etc.)
- Outlier detection
- Trend identification
- Dataset comparison

```bash
python agents/data_analysis/data_agent.py
```

### 4. Code Assistant Agent
Location: `agents/code_assistant/`

Code analysis and improvement suggestions:
- Line counting (code, comments, blank)
- Function and class detection
- Import statement analysis
- Style checking
- Improvement suggestions

```bash
python agents/code_assistant/code_agent.py
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/tuxsy/my-ai-agents.git
cd my-ai-agents
```

2. Run any agent example:
```bash
python agents/chatbot/simple_chatbot.py
```

3. Import agents in your own code:
```python
from agents.chatbot.simple_chatbot import SimpleChatbot

bot = SimpleChatbot()
response = bot.respond("Hello!")
print(response)
```

## Structure

```
my-ai-agents/
├── README.md
└── agents/
    ├── chatbot/
    │   ├── simple_chatbot.py
    │   └── README.md
    ├── task_automation/
    │   ├── task_agent.py
    │   └── README.md
    ├── data_analysis/
    │   ├── data_agent.py
    │   └── README.md
    └── code_assistant/
        ├── code_agent.py
        └── README.md
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Contributing

Feel free to add more agent examples or improve existing ones!

## License

MIT License
