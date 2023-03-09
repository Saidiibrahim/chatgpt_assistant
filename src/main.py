from src.speech.speech import get_audio, speak
from src.large_lang_model.openai import generate_response

prompt = ""

# Main loop to continuously listen for user input
while True:
    text = get_audio()
    if not text:
        continue
    prompt += text
    response = generate_response(prompt)
    speak(response)
    prompt = ""  # Reset prompt after generating response
