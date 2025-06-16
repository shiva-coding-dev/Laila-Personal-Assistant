import speech_recognition as sr
import webbrowser 
import pyttsx3
import requests
import musicLibrary
import apps
from groq import Groq
import sys
from dotenv import load_dotenv
import os
conversation_history = []
recognizer = sr.Recognizer()
engine = pyttsx3.init()
import wikipedia_api
requests.get("https://www.google.com")

load_dotenv()
newsapi = os.getenv("newsapi")

def speak(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def aiProcess(history):
    client = Groq(
        api_key= os.getenv("api_key")
    )
    completion = client.chat.completions.create(
        model="llama3-70b-8192", 
        messages=[
            {"role": "system", "content": "You are a virtual assistant named LAILA which is created by a skilled developer Shiva ,skilled in general tasks like Alexa and Google Cloud AND PLEASE give short responses. Remember previous xonversations and give responses accordingly."},
            *history
        ]
    )

    return completion.choices[0].message.content

from wikipedia.exceptions import DisambiguationError, PageError

def openAppsOnCommand(command):
    for key in apps.app_map:
        if key in command:
            app_name = apps.app_map[key]
            if "'" in app_name:  # prevent shell errors
                    speak("Sorry, app name contains unsupported characters.")
                    return
            speak(f"Opening {app_name}")
            os.system(f"open -a \"{app_name}\"")  # use double quotes for safety
            return
    speak("App not found ")
import my_websites

def openWebsitesOnCommand(command):
    for key in my_websites.newWeb:
        if key in command:
            website_name = my_websites.newWeb[key]
            if "'" in website_name:
                speak("Sorry, app name contains unsupported characters.")
                return
            speak(f"Opening {key}")
            webbrowser.open(website_name)
            return
    speak("Website not included yet ")

def processCommand(command):
    global conversation_history
    command = command.lower().strip()
    conversation_history.append({"role": "user", "content": command})
    try:

        if "website" in command.lower():
            website = command.lower().split(" ")[1]
            link = my_websites.newWeb[website]
            webbrowser.open(link)
            speak(f"Opening {website}")

        elif command.lower().startswith("play"):
            song = command.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        
        elif "news" in command.lower():
            r = requests.get("https://newsapi.org/v2/top-headlines?q=india&apiKey=3c98a3133d254ab89c8dcc1705c35981")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles",[])
                for article in articles:
                    speak(article['title'])

        elif command.lower().startswith("open"):
            openAppsOnCommand(command)
        
        elif "wikipedia" in command.lower():
            speak("Wikipedia search is on. Please say the title.")
            try:
                with sr.Microphone() as source:
                    print("🎤 Listening for Wikipedia title...")
                    audio = recognizer.listen(source, timeout=5)
                    wiki_command = recognizer.recognize_google(audio)
                    print("✅ Recognized:", wiki_command)
                    wiki_summary = wikipedia_api.get_summary(wiki_command)
                    print(wiki_summary)
                    speak(wiki_summary)                
            except sr.WaitTimeoutError:
                speak("You were silent. Please try again.")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand. Please repeat.")
            except sr.RequestError:
                speak("Speech service error. Check your internet.")
        elif "hariom" in command.lower():
            speak("ki maa ka bhosda , hariom ki maa ka bhosada , hariom ki maa ka bhosada ")
        elif "time travel" in command.lower():
            speak("Time Travel Machine Activating ! Tie up your seat belts ")

        elif "switch off" in command.lower():
            speak("LAILA Switching OFF")
            sys.exit()
        else:
            if len(conversation_history) > 20:
                conversation_history = conversation_history[-20:]
            output = aiProcess(conversation_history)
            speak(output)
            conversation_history.append({"role": "assistant", "content": output})
    except Exception:
        print("Error")
    


if __name__ == "__main__":
    speak("Initializing LAILA")
    laila_active = False
    while(True):
        r = sr.Recognizer()    
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("🎧 Listening...")
                audio = recognizer.listen(source, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print("🗣️ Heard:", command)

                if not laila_active:
                    if "laila" in command:
                        laila_active = True
                        speak("Yes")
                    else:
                        print("🔇 Wake word not detected.")
                else:
                    if "switch off" in command:
                        speak("Laila switching off.")
                        break
                    else:
                        processCommand(command)

        except sr.UnknownValueError :
            print("Laila Couldn't Understand the audio ")
        except sr.RequestError as e:
            print("Error {}".format(e))

