import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init()
#engine.setProperty( name:'rate', value:150)
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
    try:
        command=recognizer.recognize_google(audio).lower()
        print(f"you said:{command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, i didnt catch that.")
        return " "
    except sr.RequestError:
        speak("could not conect to google speech recognition.")
        return (" ")
def execute_command(command):
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"the current time is{time}")
    elif "search for" in command:
        query = command.replace("search for"," ").strip()
        speak(f"searhing for {query}")
        pywhatkit.search(query)
    elif "open" in command:
        app_name = command.replace("open", "").strip().lower()
        mac_apps = {
            "notepad": "TextEdit",
            "calculator": "Calculator",
            "paint": "Preview",
            "word": "Microsoft Word",
            "excel": "Microsoft Excel",
            "whatsapp": "WhatsApp"
            # Add more mac apps here if needed
        }
        if app_name in mac_apps:
            speak(f"Opening {app_name}")
            os.system(f'open -a "{mac_apps[app_name]}"')
        else:
            speak(f"Sorry, I don't know how to open {app_name} yet.")
    elif "play" in command:
        song=command.replace("play"," ").strip()
        speak(f"playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif "wikipedia" in command:
        topic = command.replace("wikipedia"," ").strip()
        #summary=wikipedia.summary(*args:topic, sentences=1)
        summary = wikipedia.summary(topic, sentences=1)
        speak(summary)
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("i didnt understand that command.")

speak("Hello Aiman! how can i assist you?")
while True:
    command=listen()
    if command:
        execute_command(command)
