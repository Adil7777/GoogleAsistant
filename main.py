import sys
import webbrowser
import cv2
import speech_recognition as sr
import playsound
from gtts import gTTS
import pyjokes
import os
import datetime
import wikipedia


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


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print(task)
    except sr.UnknownValueError:
        # talk('I can not understand you')
        task = command()

    return task


def wiki(words):
    return wikipedia.summary(words)


def open_camera():
    cap = cv2.VideoCapture(0)
    while 1:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def make_something(task):
    words = ''
    url = ''

    if 'youtube' in task:
        words = 'Opening YouTube'
        url = 'youtube.com'

    elif 'wikipedia' in task:
        words = wiki(task.replace('wikipedia', ''))
        print(words)

    elif 'facebook' in task:
        words = 'Opening Facebook'
        url = 'facebook.com'

    elif 'instagram' in task:
        words = 'Opening Instagram'
        url = 'instagram.com'

    elif 'anecdote' in task:
        words = pyjokes.get_joke()
        print(words)

    elif 'time' in task:
        words = str(datetime.datetime.now())

    elif 'stop' in task:
        talk('Alright, stopping program')
        sys.exit()

    elif 'camera' in task:
        talk('opening camera')
        open_camera()

    print(task)

    talk(words)
    if url != '':
        webbrowser.open(url)


while 1:
    make_something(command())
