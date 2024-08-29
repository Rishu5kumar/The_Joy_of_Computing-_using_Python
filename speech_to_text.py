# speech recognition is an api provided by google
# it converts audio file to text

# sudo pip install SpeechRecognition

# take an audio file and covert it into .wav extension as this only works on .wav extension files

import os
import speech_recognition as sr

# Using os.path.expanduser to expand the tilde (~) to the home directory
audio_file = os.path.expanduser("~/ringtone.wav")

r = sr.Recognizer()  # Initialize the recognizer

# Using the audio file as a source
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)  # Reads the audio file

try:
    print("Audio file contains:", r.recognize_google(audio))  # Print the text
except sr.UnknownValueError:
    # In case it is not able to understand the audio
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    # In case we are not able to get the results from Google SpeechRecognition
    print("Could not get the results from Google Speech Recognition")
