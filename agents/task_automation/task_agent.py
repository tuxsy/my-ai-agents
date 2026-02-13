"""
Task Automation Agent
An agent that can schedule and execute automated tasks.
"""

import json
import time
from datetime import datetime, timedelta
from typing import Callable, List, Dict, Any


class Task:
    """Represents a scheduled task."""
    
    def __init__(self, name: str, action: Callable, interval_seconds: int = 0):
        self.name = name
        self.action = action
        self.interval_seconds = interval_seconds
        self.last_run = None
        self.run_count = 0
    
    def should_run(self) -> bool:
        """Check if task should run based on interval."""
        if self.last_run is None:
            return True
        
        if self.interval_seconds == 0:
            return False
        
        elapsed = (datetime.now() - self.last_run).total_seconds()
        return elapsed >= self.interval_seconds
    
    def execute(self) -> Any:
        """Execute the task action."""
        result = self.action()
        self.last_run = datetime.now()
        self.run_count += 1
        return result


class TaskAutomationAgent:
    """Agent that manages and executes automated tasks."""
    
    def __init__(self, name="TaskAgent"):
        self.name = name
        self.tasks: List[Task] = []
        self.running = False
    
    def add_task(self, name: str, action: Callable, interval_seconds: int = 60):
        """Add a task to the agent."""
        task = Task(name, action, interval_seconds)
        self.tasks.append(task)
        print(f"[{self.name}] Added task: {name} (runs every {interval_seconds}s)")
    
    def remove_task(self, name: str):
        """Remove a task by name."""
        self.tasks = [t for t in self.tasks if t.name != name]
        print(f"[{self.name}] Removed task: {name}")
    
    def run_once(self):
        """Run all tasks that are due."""
        for task in self.tasks:
            if task.should_run():
                try:
                    result = task.execute()
                    print(f"[{self.name}] Executed {task.name}: {result}")
                except Exception as e:
                    print(f"[{self.name}] Error in {task.name}: {e}")
    
    def run(self, duration_seconds: int = None):
        """Run the agent continuously or for a specified duration."""
        self.running = True
        start_time = datetime.now()
        
        print(f"[{self.name}] Starting automation agent...")
        
        while self.running:
            self.run_once()
            
            # Check if duration limit reached
            if duration_seconds:
                elapsed = (datetime.now() - start_time).total_seconds()
                if elapsed >= duration_seconds:
                    break
            
            time.sleep(1)  # Check every second
        
        print(f"[{self.name}] Stopped.")
    
    def stop(self):
        """Stop the agent."""
        self.running = False
    
    def get_status(self) -> Dict[str, Any]:
        """Get status of all tasks."""
        status = {
            "agent": self.name,
            "running": self.running,
            "tasks": []
        }
        
        for task in self.tasks:
            task_info = {
                "name": task.name,
                "interval": task.interval_seconds,
                "last_run": task.last_run.isoformat() if task.last_run else None,
                "run_count": task.run_count
            }
            status["tasks"].append(task_info)
        
        return status


def example_task_hello():
    """Example task: Print hello."""
    return "Hello from automated task!"


def example_task_time():
    """Example task: Print current time."""
    return f"Current time: {datetime.now().strftime('%H:%M:%S')}"


def example_task_counter():
    """Example task: Count up."""
    if not hasattr(example_task_counter, "count"):
        example_task_counter.count = 0
    example_task_counter.count += 1
    return f"Counter: {example_task_counter.count}"


def main():
    """Run the task automation agent with example tasks."""
    agent = TaskAutomationAgent()
    
    # Add example tasks
    agent.add_task("hello_task", example_task_hello, interval_seconds=5)
    agent.add_task("time_task", example_task_time, interval_seconds=3)
    agent.add_task("counter_task", example_task_counter, interval_seconds=2)
    
    # Run for 10 seconds
    print("\nRunning tasks for 10 seconds...\n")
    agent.run(duration_seconds=10)
    
    # Print final status
    print("\nFinal Status:")
    print(json.dumps(agent.get_status(), indent=2))


if __name__ == "__main__":
    main()
