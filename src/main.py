from large_lang_model.llm_response import chatgpt_chain
from speech.speech import speak, get_audio

while True:
    text = get_audio()
    if not text:
        continue
    response_text = chatgpt_chain.predict(human_input=text)
    speak(response_text)
