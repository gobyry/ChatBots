# Source: The AI Advantage's Video

import openai

# chatGBT API key.
openai.api_key = "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"

# Prompt for chat bot answer.
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Explain why the Porsche GT3RS is the best car ever made."}])

# Print chat bot answer.
print(completion.choices[0].message.content)

