print("AI Chatbot started!")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    print("Bot: I received your message.")
