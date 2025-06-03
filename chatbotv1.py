import google.generativeai as genai
import os
import sys # Import sys to exit if API key is missing

# --- CONFIGURATION ---
# It's highly recommended to set your API Key as an environment variable.
# On macOS/Linux, you can do this in your terminal before running the script:
# export GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
# On Windows (Command Prompt): set GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
# On Windows (PowerShell): $env:GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY_HERE"

# Try to get the API key from the environment variable
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: GOOGLE_API_KEY environment variable not set.")
    print("Please set it before running the script (e.g., export GOOGLE_API_KEY='YOUR_KEY_HERE')")
    sys.exit(1) # Exit the script if no API key is found

genai.configure(api_key=api_key)

# --- INITIALIZE THE MODEL ---
# Choose a model. 'gemini-pro' is generally good for text-only chat.
# Make sure this model name is actually available to you.
MODEL_NAME = 'gemini-1.5-flash-latest' # Or 'gemini-1.0-pro', 'gemini-1.5-pro-latest' etc. if needed

try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    print(f"ERROR: Could not initialize model '{MODEL_NAME}'. This often means the API key is invalid or the model name is incorrect/unavailable for your account/region.")
    print(f"Details: {e}")
    sys.exit(1)

# --- START A CHAT SESSION ---
# This maintains conversation history for context.
chat = model.start_chat(history=[])

print("Chatbot: Hello! Type 'quit' to exit.")

# --- CHAT LOOP ---
while True:
    user_input = input("You: ").strip() # .strip() removes leading/trailing whitespace

    if not user_input: # Handle empty input
        print("Chatbot: Please type something before pressing Enter.")
        continue

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
        print("This could be due to an invalid API key, network issue, or unsupported model.")
        print("Please check your API key and verify model availability.")