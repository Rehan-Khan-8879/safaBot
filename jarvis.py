import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Ready to comply. What can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except:
        speak("Say that again please...")
        return "None"
    return query.lower()

def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        'divided': operator.truediv,
    }[op]

def eval_binary_expr(op1, oper, op2):
    return get_operator_fn(oper)(int(op1), int(op2))

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'open youtube' in query:
            speak("What would you like to watch?")
            qrry = takeCommand()
            kit.playonyt(qrry)

        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={qry}")

        elif 'play music' in query:
            music_dir = 'E:\\Musics'  # Change this path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'play iron man movie' in query:
            movie_path = 'E:\\ironman.mkv'  # Change this path
            os.startfile(movie_path)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow("Webcam", frame)
                if cv2.waitKey(1) == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "take screenshot" in query:
            speak("Tell me a name for the file")
            name = takeCommand()
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot saved")

        elif "calculate" in query:
            speak("Ready to calculate")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                expression = r.recognize_google(audio)
                result = eval_binary_expr(*(expression.split()))
                speak(f"Your result is {result}")
            except:
                speak("Sorry, I couldn't understand")

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ip = requests.get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            except:
                speak("Network error")

        elif "volume up" in query:
            for _ in range(10):
                pyautogui.press("volumeup")

        elif "volume down" in query:
            for _ in range(10):
                pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "go to sleep" in query:
            speak("Okay, shutting down.")
            sys.exit()

        elif "who are you" in query:
            speak("My name is Six. I can do everything my creator programmed me to do.")

        elif "who created you" in query:
            speak("I was created using Python in Visual Studio Code.")

        elif "open notepad and write my channel name" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('notepad')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write("How To Manual", interval=0.1)

        elif "type" in query:
            query = query.replace("type", "")
            pyautogui.write(query)

        elif "subscribe" in query:
            speak("Please subscribe to our channel 'How To Manual' for more tutorials.")
