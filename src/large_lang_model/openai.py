import openai


# Set up OpenAI API credentials
openai.api_key = "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"

# Set up the OpenAI model
model_engine = "text-davinci-003"


# Function to generate OpenAI response based on user input
def generate_response(prompt_input):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message
