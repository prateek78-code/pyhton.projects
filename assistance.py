import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pywhatkit  # to play any song from YouTube
import wikipedia  # to open any website
import os
import pyjokes  # to tell jokes
from datetime import datetime
from sympy import sympify  # to calculate math expressions

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = "YOUR_NEWS_API_KEY"
weather_key = "YOUR_OPENWEATHER_API_KEY"  

# Speak text aloud
def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

# Stop current YouTube playback (by killing browser)
def stop_current_playback():
    try:
        # For Windows and Chrome; replace with your browser if needed
        os.system("taskkill /im chrome.exe /f")
        speak("Stopped current playback.")
    except Exception as e:
        print("Error stopping browser:", e)

# Process voice command
def process_command(c):
    print(f"Command received: {c}")
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open srm site" in c:
        speak("Opening SRM site")
        webbrowser.open("https://www.srmist.edu.in")

    elif "open" in c:
        try:
            site = c.split("open", 1)[1].strip().replace(" ", "")
            url = f"https://www.{site}.com"
            speak(f"Opening {site}")
            webbrowser.open(url)
        except:
            speak("I couldn't open that site.")

    elif "world headlines" in c or "today's headlines" in c:
        try:
            url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=5&apiKey={newsAPI}"
            r = requests.get(url)
            data = r.json()
            if data["status"] == "ok":
                articles = data["articles"]
                speak(f"Reading top {len(articles)} headlines from around the world.")
                for i, article in enumerate(articles, 1):
                    speak(f"Headline {i}: {article['title']}")
        except:
            speak("Sorry, I could not fetch headlines.")

    elif c.startswith("play"):
        try:
            stop_current_playback()  # Stop existing playback
            song_name = c.split(" ", 1)[1]
            speak(f"Playing {song_name}")
            pywhatkit.playonyt(song_name)
        except IndexError:
            speak("Please say the name of the song after 'play'.")
        except Exception as e:
            speak("Sorry, I couldn't play the song.")
            print("Error:", e)

    elif "time" in c:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "today's weather" in c:
        city = "chennai"
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
            print(f"Requesting weather URL: {url}")
            r = requests.get(url)
            data = r.json()
            print("Weather response:", data)
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}")
            else:
                speak("Sorry, could not get weather information.")
        except Exception as e:
            print("Weather exception:", e)
            speak("Sorry, I couldn't fetch the weather information.")

    elif "who is" in c or "what is" in c:
        try:
            result = wikipedia.summary(c, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("Your query is too broad, please be more specific.")
        except Exception:
            speak("Sorry, I couldn't find that.")

    elif "calculate" in c:
        expr = c.replace("calculate", "").strip()
        try:
            result = sympify(expr)
            speak(f"The result is {result}")
        except:
            speak("Sorry, I couldn't calculate that.")

    elif " a note on" in c:
        note = c.replace("write a note on", "").strip()
        if note:
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
            speak("Note written.")
        else:
            speak("Please say the note clearly after 'write a note on'.")

    elif "read notes" in c:
        try:
            with open("notes.txt", "r") as f:
                speak(f.read())
        except:
            speak("No notes found.")

    elif "shutdown" in c:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    elif "restart" in c:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")

    elif "tell me a joke" in c:
        joke = pyjokes.get_joke()
        speak(joke)

    else:
        speak("Sorry, I don't recognize that command.")

# Main assistant loop
if __name__ == "__main__":
    speak("Initializing Kinshuk...")

    while True:
        print("Listening for wake word 'kinshuk'...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "kinshuk":
                speak("Yes, how may I help you?")
                print("Kinshuk activated. Listening for your command...")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                process_command(command)

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")




