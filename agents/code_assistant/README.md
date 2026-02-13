# Code Assistant Agent

An agent that helps analyze code, find patterns, and suggest improvements.

## Features
- Count lines of code (total, code, comments, blank)
- Find function and class definitions
- Identify import statements
- Perform basic style checks
- Suggest code improvements

## Usage

```python
from agents.code_assistant.code_agent import CodeAssistantAgent

# Create an agent
agent = CodeAssistantAgent(name="CodeHelper")

# Add code snippet
code = """
def hello():
    print("Hello, World!")
"""
agent.add_snippet("my_code", code)

# Analyze
analysis = agent.analyze("my_code")
print(analysis)

# Get suggestions
suggestions = agent.suggest_improvements("my_code")
print(suggestions)
```

## Running the Example

```bash
python agents/code_assistant/code_agent.py
```

## Example Output

```
[CodeAssistant] Added code snippet: calculator

=== Code Analysis ===

Line Count:
{
  "snippet": "calculator",
  "total_lines": 30,
  "code_lines": 20,
  "blank_lines": 5,
  "comment_lines": 5
}

Functions found: ['add', 'multiply', 'power', 'main']
Classes found: ['Calculator']

Imports:
{
  "snippet": "calculator",
  "imports": ["math", "sys"],
  "from_imports": []
}

Improvement Suggestions:
1. Code looks good! Keep up the good work.
```
