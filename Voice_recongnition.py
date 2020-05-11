# Responds to a name


import speech_recognition
import re

#audio from the microphone
recognizer = speech_recognition.Recognizer()
with spech_recognition.Microphone() as source:
    print("Say something")
    audio = recognizer.listen(source)

#Recognize speech by using Google Spwwch Recognition
words = recognizer.recognize_google(audio)

#print("Google Speed Recognition thinks you said")
#print(recognizer.recognize_google(audio))

#Respond to speech

matches = re.spearch("my name is (.*)", words)
if matches:
    print("Hello, {matches[1]}.")
else:
    print("Hey, you.")