# Basic Chatbot

def get_reply(message):
    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I am a simple chatbot."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


def chat():
    print("Bot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()
        reply = get_reply(user_input)
        print("Bot:", reply)
        if user_input == "bye":
            break


chat()