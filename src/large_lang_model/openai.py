import openai
from decouple import config


# Set up OpenAI API credentials
openai.api_key = config("OPENAI_KEY")

# Set up the OpenAI model
# model_engine = "text-davinci-003"


# Function to generate OpenAI response based on user input
# def generate_response(prompt_input):
#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt_input,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     message = response.choices[0].text
#     return message

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = response.choices[0].message.content
    return chat_response
