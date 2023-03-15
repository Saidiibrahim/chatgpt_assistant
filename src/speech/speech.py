import speech_recognition as sr
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os
# import pyttsx3
from decouple import config


"""pyttsx3 Engine Setup"""
# Set up the text-to-speech engine
# engine = pyttsx3.init()


"""SpeechRecognition"""
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


"""pyttsx3"""
# Function to convert text to speech
# def speak(text_input):
#    engine.say(text_input)
#    engine.runAndWait()


""""TTS W/ AMAZON POLLY"""
# Set up the Amazon Polly client
client = boto3.client('polly',
                      region_name='us-east-1',
                      aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"))


def speak(text):
    try:
        # Request speech synthesis
        response = client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'  # Change to the desired voice ID
        )

        # Save the audio stream to a file
        with open('speech.mp3', 'wb') as f:
            f.write(response['AudioStream'].read())

        # Play the audio file
        os.system('afplay speech.mp3')  # Change to the appropriate command for your OS

    except (BotoCoreError, ClientError) as error:
        print(error)


