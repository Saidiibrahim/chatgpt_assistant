import speech_recognition as sr
import openai
import pyttsx3

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up the OpenAI model
model_engine = "text-davinci-003"
prompt = ""

# Set up the text-to-speech engine
engine = pyttsx3.init()


# Function to get the user's speech input
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


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


# Function to convert text to speech
def speak(text_input):
    engine.say(text_input)
    engine.runAndWait()


# Main loop to continuously listen for user input
while True:
    text = get_audio()
    if not text:
        continue
    prompt += text
    response = generate_response(prompt)
    speak(response)
    prompt = ""  # Reset prompt after generating response

