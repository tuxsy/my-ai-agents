# Task Automation Agent

An agent that schedules and executes automated tasks at specified intervals.

## Features
- Schedule tasks with custom intervals
- Execute tasks automatically
- Track task execution history
- Get status of all tasks

## Usage

```python
from agents.task_automation.task_agent import TaskAutomationAgent

# Create an agent
agent = TaskAutomationAgent(name="MyAgent")

# Define a task function
def my_task():
    return "Task executed!"

# Add task to run every 60 seconds
agent.add_task("my_task", my_task, interval_seconds=60)

# Run for 120 seconds
agent.run(duration_seconds=120)

# Get status
status = agent.get_status()
print(status)
```

## Running the Example

```bash
python agents/task_automation/task_agent.py
```

## Example Output

```
[TaskAgent] Added task: hello_task (runs every 5s)
[TaskAgent] Added task: time_task (runs every 3s)
[TaskAgent] Added task: counter_task (runs every 2s)

Running tasks for 10 seconds...

[TaskAgent] Starting automation agent...
[TaskAgent] Executed hello_task: Hello from automated task!
[TaskAgent] Executed time_task: Current time: 10:30:45
[TaskAgent] Executed counter_task: Counter: 1
...
```
