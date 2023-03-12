from src.speech.speech import get_audio, speak
from src.large_lang_model.openai import generate_response

# prompt = ""
content = ""

messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]


# Main loop to continuously listen for user input
while True:
    text = get_audio()
    if not text:
        continue
    # prompt += text
    content += text
    messages.append({"role": "user", "content": content})
    response = generate_response(messages)
    speak(response)
    content = ""  # Reset prompt after generating response
