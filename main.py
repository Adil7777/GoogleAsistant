import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
import playsound
from gtts import gTTS
import pyjokes
import os
import datetime


def talk(words):
    if words != '':
        tts = gTTS(words, lang='en')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    # engine = pyttsx3.init()
    # engine.say(words)
    # engine.runAndWait()


talk('Do not forget subscribe and share with your friends, thanks for watching')

# def command():
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print('Say something')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, 1)
#         audio = r.listen(source)
#
#     try:
#         task = r.recognize_google(audio).lower()
#         print(task)
#     except sr.UnknownValueError:
#         # talk('I can not understand you')
#         task = command()
#
#     return task
#
#
# def make_something(task):
#     words = ''
#     url = ''
#
#     if 'youtube' in task:
#         words = 'Opening YouTube'
#         url = 'youtube.com'
#
#     elif 'facebook' in task:
#         words = 'Opening Facebook'
#         url = 'facebook.com'
#
#     elif 'instagram' in task:
#         words = 'Opening Instagram'
#         url = 'instagram.com'
#
#     elif 'anecdote' in task:
#         words = pyjokes.get_joke()
#         print(words)
#
#     elif 'time' in task:
#         words = str(datetime.datetime.now())
#
#     elif 'stop' in task:
#         talk('Alright, stopping program')
#         sys.exit()
#
#     talk(words)
#     if url != '':
#         webbrowser.open(url)
#
#
# while 1:
#     make_something(command())
