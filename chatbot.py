import ollama

print("Chatbot has started.")
print("Type 'exit', 'quit', 'bye', 'goodbye', or 'end' to stop.")

exit_commands = ["exit", "quit", "bye", "goodbye", "end"]

while True:
    user_input = input("You: ")

    if user_input.lower() in exit_commands:
        print("Exiting the chatbot. Goodbye!")
        break

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Chatbot:", response.message.content)
