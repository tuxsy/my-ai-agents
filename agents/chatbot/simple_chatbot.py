"""
Simple Chatbot Agent
A basic conversational AI agent that can respond to user inputs.
"""

import random


class SimpleChatbot:
    """A simple rule-based chatbot agent."""
    
    def __init__(self, name="ChatBot"):
        self.name = name
        self.context = []
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
            "how are you": ["I'm doing great, thanks for asking!", "I'm functioning well!", "All systems operational!"],
            "bye": ["Goodbye!", "See you later!", "Have a great day!"],
            "help": ["I'm here to chat with you. Try saying hello, asking how I am, or saying goodbye!"],
        }
    
    def respond(self, user_input):
        """Generate a response based on user input."""
        if not user_input:
            return "Please say something!"
        
        # Store context
        self.context.append(user_input)
        
        # Simple pattern matching
        user_input_lower = user_input.lower()
        
        for key, responses in self.responses.items():
            if key in user_input_lower:
                return random.choice(responses)
        
        # Default response
        return f"Interesting! Tell me more about '{user_input}'."
    
    def get_context(self):
        """Return the conversation context."""
        return self.context


def main():
    """Run the chatbot in interactive mode."""
    chatbot = SimpleChatbot()
    print(f"{chatbot.name}: Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print(f"{chatbot.name}: {chatbot.respond('bye')}")
            break
        
        response = chatbot.respond(user_input)
        print(f"{chatbot.name}: {response}")


if __name__ == "__main__":
    main()
