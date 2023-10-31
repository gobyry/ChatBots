# Source: haihai.ai's article on Chatbot

import openai

# chatGBT API key
openai.api_key = "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"

# Create messages list.
messages = []

# Describe desired chatbot.
system_msg = input("What type of chatter do you want to chat with?\n")

# Add user input to message history.
messages.append({"role": "system", "content": system_msg})
print("Your new assistant is ready!")

# Run chatbot until user quits.
while input != "quit()":
    # Get user input.
    message = input()
    # Add user input to message history.
    messages.append({"role": "user", "content": message})

    # Generate response using open AI.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    # Extract chatbot reply from API response.
    reply = response["choices"][0]["message"]["content"]
    # Add chatbot reply to message history.
    messages.append({"role": "assistant", "content": reply})
    # Print chatbot reply.
    print("\n" + reply + "\n")
