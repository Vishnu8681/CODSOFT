import re
import random
from datetime import datetime

user_name = None 

chatbot_rules = {
    "greeting": {
        "patterns": [r"\bhi\b", r"\bhello\b",r"\bhai\b", r"\bhey\b", r"good morning", r"good evening"],
        "responses": ["Hello! 👋", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "patterns": [r"\bbye\b", r"goodbye", r"see you", r"quit", r"exit"],
        "responses": ["Goodbye! 👋", "See you soon!", "Bye, take care!"]
    },
    "thanks": {
        "patterns": [r"thank", r"thanks", r"thank you"],
        "responses": ["You're welcome 😊", "Anytime!", "Glad I could help!"]
    },
    "ask_name": {
        "patterns": [r"your name", r"who are you"],
        "responses": ["I'm CodBot 🤖, your AI chatbot!"]
    },
    "capture_name": {
        "patterns": [r"my name is (?P<name>[A-Za-z]+)", r"i am (?P<name>[A-Za-z]+)"],
        "responses": ["Nice to meet you, {name}! 😃", "Hello {name}, how can I help you today?"]
    },
    "ask_time": {
        "patterns": [r"time", r"current time"],
        "responses": [f"The time now is {datetime.now().strftime('%H:%M:%S')}"]
    },
    "ask_date": {
        "patterns": [r"date", r"today"],
        "responses": [f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"]
    },
    "weather": {
        "patterns": [r"weather", r"temperature", r"hot", r"cold"],
        "responses": [
            "I can’t check live weather 🌦️, but it’s always sunny in my world!",
            "Looks like a great day to code ☀️"
        ]
    },
    "joke": {
        "patterns": [r"joke", r"make me laugh"],
        "responses": [
            "😂 Why don’t programmers like nature? It has too many bugs.",
            "🤣 Why do Java developers wear glasses? Because they can’t C#!",
            "😆 My code never has bugs, only features."
        ]
    },
    "fact": {
        "patterns": [r"fact", r"tell me something"],
        "responses": [
            "💡 Did you know? The first computer virus was created in 1986.",
            "🤯 Fun fact: Python was named after Monty Python, not the snake.",
            "📚 AI can now write poems, code, and even chat with you!"
        ]
    },
    "motivation": {
        "patterns": [r"motivate", r"inspire", r"quote"],
        "responses": [
            "🚀 Keep pushing, success is near!",
            "🔥 Don’t stop when you’re tired. Stop when you’re done.",
            "💪 Every expert was once a beginner."
        ]
    },
    "math": {
        "patterns": [r"\d+\s*[\+\-\*/]\s*\d+"],
        "responses": ["math_mode"]  
    },
    "smalltalk": {
        "patterns": [r"how are you", r"what's up", r"how’s it going"],
        "responses": [
            "I’m doing great, thanks for asking! 🤖",
            "All good here. Ready to chat!",
            "I’m just code, but I feel awesome 😎"
        ]
    },
    "help": {
        "patterns": [r"help", r"what can you do", r"commands"],
        "responses": [
            "📌 I can chat with you, tell jokes, facts, motivation, date/time, "
            "solve math, remember your name, and say goodbye.\n"
            "👉 Try: 'hi', 'my name is Vishnu', 'time', 'joke', '2+2', 'fact', 'bye'."
        ]
    }
}

def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower()

    for intent, data in chatbot_rules.items():
        for pattern in data["patterns"]:
            match = re.search(pattern, user_input)
            if match:
                if intent == "capture_name":
                    user_name = match.group("name").capitalize()
                    response = random.choice(data["responses"])
                    return response.format(name=user_name)

                
                if intent == "math":
                    try:
                        result = eval(user_input)
                        return f"🧮 The result is {result}"
                    except:
                        return "Hmm, I couldn’t calculate that 🤔"

                response = random.choice(data["responses"])
                if user_name:
                    response = response.replace("{name}", user_name)
                return response

    return "Sorry, I don't understand that. 🤔 Type 'help' to see what I can do."

print("CodBot 🤖: Hello! What help do you want?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CodBot 🤖: Goodbye! 👋 Stay motivated!")
        break
    response = chatbot_response(user_input)
    print("CodBot 🤖:", response)
