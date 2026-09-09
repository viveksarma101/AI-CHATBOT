import ollama

print("Chatbot has started.")
print("Type any exit commands to end the conversation with the bot.")

exit_commands = ["exit", "quit", "bye", "goodbye", "end"]

messages = [{
    "role": "system",
    "content": "You are a helpful chatbot. Keep your responses concise, avoid excessive emojis and overly enthusiastic language. Avoid making assumptions about the user's identity. Do not present uncertain information as fact. Clearly state when you are unsure. Avoid making up information. If you don't know the answer, say 'I don't know' or 'I'm not sure'."
}]

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
