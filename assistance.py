import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI="7c562e154c1349dcabe8fece1a27bfdb"
# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process recognized commands
def process_command(c):
    print(f"Command received: {c}")

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "today's headlines"in c.lower():
        try:
         r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsAPI}")
         data = r.json()
         if data["status"] == "ok":
             print(f"\n Top {len(data['articles'])} Headlines from the US:\n")
         for i, article in enumerate(data["articles"], 1):
              speak(f"{i}. {article['title']}") 
        except requests.exceptions.RequestException as e:
              print("An error occurred:", e) 

    elif c.lower().startswith("play"):
        try:
            song_name = c.lower().split(" ", 1)[1] #it will split play skyfall(or any other song) in ["play","skyfall"] and will select skyfall as it is on 1st index.
            link = musiclibrary.mymusic.get(song_name)
            if link:
                speak(f"Playing {song_name}")
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song in your library.")
        except IndexError:
            speak("Please say the name of the song after 'play'.")
    else:
        speak("Sorry, I don't recognize that command.")
    
        
    

  
# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Listening for wake word 'Jarvis'...")

        try:
            # Listen for wake word
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)  #timeout:-Maximum time (in seconds) to wait for someone to start speaking.
                                                                                   #phrase_time_out:-Maximum duration (in seconds) for capturing a phrase after speech starts.
            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                print("Jarvis activated. Listening for your command...")

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