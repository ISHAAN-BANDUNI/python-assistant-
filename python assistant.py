import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Define some basic responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm functioning perfectly!", "I'm doing well, thank you!"]
    ],
    [
        r"what is your name?",
        ["I am your Python Assistant.", "You can call me Assistant."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"what can you do?",
        ["I can answer your questions, provide information, and assist with basic tasks."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Happy to help!"]
    ],
    [
        r"what is the weather like today?",
        ["I'm sorry, I don't have access to real-time weather data. You can check a weather website or app."]
    ],
    [
        r"what is the time?",
        ["I don't have access to real-time data. You can check your device's clock."]
    ],
    [
        r"who created you?",
        ["I was created by a Python developer.", "I'm a program written in Python."]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist you with your queries and provide helpful information."]
    ],
    [
        r"how do I learn Python?",
        ["You can start by reading Python documentation, taking online courses, or practicing coding exercises."]
    ],
    [
        r"what is AI?",
        ["AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think and learn."]
    ],
    [
        r"what is machine learning?",
        ["Machine learning is a subset of AI that involves training algorithms to learn from and make predictions based on data."]
    ],
    [
        r"what is the capital of (.*)",
        ["The capital of %1 is [insert capital here]. You can look it up for more details."]
    ],
    [
        r"what is (.*)",
        ["I'm not sure about that. You might want to search online for more information."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ]
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Main loop
def main():
    print("Hello! I'm your Python Assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Assistant: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()