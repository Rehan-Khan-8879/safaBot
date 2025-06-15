import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [1] is usually a female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            return command.lower()
        except:
            return ""

# Predefined responses
responses = {
    "hello": "Hi, jaaa be?",
    "hu r u": "I am your saafaa, rehaan.",
    "how r u": "I'm doing well, thank you.",
    "good bye": "Dont leve me pleas"
}

while True:
    command = listen()
    print("You said:", command)

    if command in responses:
        speak(responses[command])
    elif "exit" in command:
        speak("Shutting down.")
        break
    else:
        speak("Sorry, I did not understand.")

