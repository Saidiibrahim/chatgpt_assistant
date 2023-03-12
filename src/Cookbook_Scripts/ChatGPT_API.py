import openai
from decouple import config


# Set up OpenAI API credentials
openai.api_key = config("OPENAI_KEY")

messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]

while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')