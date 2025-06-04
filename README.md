# Artificial-Intelligence-ChatBot
To create the new project - ChatBot(related to Artificial Intelligence)

Goal: Your Python program will send text to an LLM (like Google's Gemini or OpenAI's GPT) and print its reply.

Step-by-Step Guide: Basic Chatbot
1. Choose Your LLM API:

Recommendation for easy start: Google's Gemini API or OpenAI's GPT-3.5 API. They are powerful and have good Python libraries.
For this guide, I'll use a generic "LLM_API" concept.
2. Get an API Key:

You'll need to sign up with the chosen provider (e.g., Google AI Studio for Gemini, OpenAI platform for GPT).
Generate an API Key. Keep this secret; it authenticates your requests.
3. Set up Your Python Environment:

Install Python: Make sure you have Python 3.8+ installed.
Create a Virtual Environment (Recommended):
Bash

python -m venv chatbot_env
source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
Install Libraries:
Bash

pip install google-generativeai # For Google Gemini
# OR
# pip install openai # For OpenAI GPT
4. Write the Python Code:

Let's use the google-generativeai library for this example.

Python

import google.generativeai as genai
import os

# --- CONFIGURATION ---
# IMPORTANT: Replace "YOUR_API_KEY" with your actual Gemini API Key.
# Even better: set it as an environment variable (e.g., in your shell: export GOOGLE_API_KEY='your_key')
# genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
genai.configure(api_key="YOUR_API_KEY") # For quick testing, but not recommended for sensitive use

# --- INITIALIZE THE MODEL ---
# Choose a model. 'gemini-pro' is good for text-only chat.
model = genai.GenerativeModel('gemini-pro')

# --- START A CHAT SESSION ---
# This maintains conversation history for context.
chat = model.start_chat(history=[])

print("Chatbot: Hello! Type 'quit' to exit.")

# --- CHAT LOOP ---
while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break

    try:
        # Send user's message and get a response
        response = chat.send_message(user_input)

        # Print the chatbot's reply
        print(f"Chatbot: {response.text}")
    except Exception as e:
        print(f"Chatbot Error: {e}")
        print("Please try again or check your API key/network connection.")

5. Run Your Chatbot:

Save the code above as chatbot.py.
Open your terminal/command prompt, navigate to the folder where you saved it.
Activate your virtual environment (if you created one): source chatbot_env/bin/activate
Run the script: python chatbot.py
How it Works (Concepts in Action):

LLM Model: genai.GenerativeModel('gemini-pro') loads the pre-trained Gemini Pro model.
Tokenization (Behind the Scenes): When you send_message(user_input), your text is tokenized by the API before being processed by the LLM. You don't directly see it here.
Chat History: chat = model.start_chat(history=[]) and chat.send_message() automatically manage and send the past conversation turns (tokens) to the LLM, giving it context for your current input.
Embeddings & RAG: Not directly used in this basic setup, but these would come into play if you wanted your chatbot to answer questions based on your specific documents (RAG) or perform semantic search (Embeddings).
Hallucinations: In this basic setup, the LLM might still hallucinate if it doesn't know the answer. RAG is the solution for this in more advanced applications.
A


