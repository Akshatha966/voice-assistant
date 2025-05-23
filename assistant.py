import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import random
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except:
        speak("Sorry, I did not understand.")
        return ""

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def open_website(site):
    urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://twitter.com"
    }
    url = urls.get(site, f"https://{site}")
    speak(f"Opening {site}")
    webbrowser.open(url)

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia,")
        speak(summary)
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don’t see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
    ]
    joke = random.choice(jokes)
    speak(joke)

def play_music():
    # Put a music file path here on your computer
    music_path = "C:\\Users\\aksha\\Music\\song.mp3"
    if os.path.exists(music_path):
        os.startfile(music_path)
        speak("Playing music.")
    else:
        speak("Sorry, I can't find the music file.")

def main():
    speak("Hello! How can I help you?")
    while True:
        command = listen()

        if 'hello' in command:
            speak("Hello! How are you?")

        elif 'time' in command:
            tell_time()

        elif 'open youtube' in command:
            open_website("youtube")

        elif 'open google' in command:
            open_website("google")

        elif 'open facebook' in command:
            open_website("facebook")

        elif 'open twitter' in command:
            open_website("twitter")

        elif 'wikipedia' in command:
            search_term = command.replace('wikipedia', '').strip()
            if search_term:
                search_wikipedia(search_term)
            else:
                speak("Please say what you want me to search on Wikipedia.")

        elif 'joke' in command:
            tell_joke()

        elif 'play music' in command:
            play_music()

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I did not understand.")

if __name__ == "__main__":
    main()
