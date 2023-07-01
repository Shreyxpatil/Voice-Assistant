import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    command = listen()
    if command == "quit":
        speak("Goodbye!")
        break
    else:
        speak("You said: " + command)
