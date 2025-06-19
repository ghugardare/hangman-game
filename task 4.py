def respond_to_input(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! 😊"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! 👋 Have a nice day!"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created in Python!"
    else:
        return "Sorry, I don't understand that yet. 🤖"

def run_chatbot():
    print("🤖 Simple Chatbot is online! Type something (type 'bye' to quit)\n")
    
    while True:
        user_input = input("You: ")
        reply = respond_to_input(user_input)
        print("Bot:", reply)
        
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
