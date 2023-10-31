# Source: The AI Advantage's Chatbot Video

import openai
import gradio

# ChatGBT API key
openai.api_key = "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"

# Describe your chatbot's expertise.
messages = [{"role": "system", "content": "You are a mechanic that specializes in tuning sports cars."}]

# Chatbot function.
def CustomChatGPT(user_input):
    # Add user input to message history.
    messages.append({"role": "user", "content": user_input})
    # Generate response using open AI.
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    # Extract chatbot reply from API response.
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    # Add chatbot reply to message history.
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    # Return chatbot reply.
    return ChatGPT_reply

# Create Gradio interface.
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

# Launch Gradio interface.
demo.launch(share=True)
