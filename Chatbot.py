import random
from datetime import datetime

def chatbot():
    print("Welcome to Smart Chatbot!")
    print("Type bye to exit.")

    name = ""

    while True:
        user = input("\nYou: ").lower().strip()

        if user in ["hello", "hallo", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "my name is" in user:
            name = user.replace("my name is", "").strip()
            print("Bot: Nice to meet you,", name.title())

        elif "what is my name" in user:
            if name:
                print("Bot: Your name is", name.title())
            else:
                print("Bot: Tell me your name first.")

        elif user in ["how are you", "kaise ho"]:
            print("Bot: I am fine. Thank you!")

        elif "time" in user:
            print("Bot:", datetime.now().strftime("%I:%M %p"))

        elif "date" in user:
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif "joke" in user:
            jokes = [
                "Why do programmers love Python? It is easy!",
                "Why did the computer go to doctor? It had a virus!"
            ]
            print("Bot:", random.choice(jokes))

        elif user in ["thanks", "thank you"]:
            print("Bot: You are welcome!")

        elif user in ["bye", "exit", "goodbye"]:
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()