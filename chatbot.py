print("AI Chatbot started!")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if user_input.lower() == "hello":
        print("Bot: Hello! How can I help you?")
    else:
        print("Bot: I received your message.")
