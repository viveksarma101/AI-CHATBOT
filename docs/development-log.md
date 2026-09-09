### Development Log
# About This Project:
This project is an attempt to understand the workflow and functioning of
basic chatbots and escalate a simple chatbot into an AI agent.
The project is a learning exercise covering APIs, LLMs,
agent architecture, and teaches wise usage of resources.

## Stage 1 — Initial Chatbot
Created a basic chatbot using a Python input loop.

## Stage 2 — Basic Response Handling
Hard coded predefined responses for basic user inputs. 

## Stage 3 — Qwen + Ollama Integration
Integrated the Qwen 3:4B model through Ollama so the chatbot could generate responses to arbitrary user requests.
# What is Ollama? How did I access Qwen? 
Ollama is a tool that allows language models to be run locally on a computer and accessed through a simple command-line interface and API.
I used Ollama to download and run the Qwen 3:4B model locally on the PC. 
My chatbot then communicated with the running model locally through the Ollama Python library.

The basic flow was:
User -> Chatbot (Python Coded) -> Ollama -> Qwen 3:4B -> Response -> User

# Stage 4 — Conversation Memory
Added message history so previous user and assistant messages are sent to the model during the conversation.

# Stage 5 — Adding System Instructions
The chatbot was behaving too casually, sometimes making assumptions about the user and confidently presenting unknown information as fact.
To address this, I added a `system` message with instructions for how the model should behave during the conversation.
This was my first step toward controlling the chatbot's behavior through
prompting rather than relying entirely on the model's default behavior.
