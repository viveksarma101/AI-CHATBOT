import ollama
print("Chatbot has started.")
print("Type any exit commands to end the conversation with the bot.")
exit_commands = ["exit", "quit", "bye", "goodbye", "end"]
while True:
    user_input = input("You: ")
    if user_input.lower() in exit_commands:
        print("Exiting the chatbot. Goodbye!")
        break
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = ollama.chat(
        model="qwen3:4b",
        messages=messages
    )
    messages.append({
    "role": "assistant",
    "content": response.message.content 
    })
    print("Chatbot:", response.message.content)
