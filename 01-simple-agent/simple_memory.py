from collections import deque


class SimpleMemory:
    def __init__(self, max_messages:int=10):
        self.max_messages = max_messages
        self._messages = deque(maxlen=max_messages)

    def add_system_message(self, content: str):
        self.add("system", content)

    def add(self, role: str, content: str):
        self._messages.append({"role": role, "content": content})

    def messages(self):
        return list(self._messages)
