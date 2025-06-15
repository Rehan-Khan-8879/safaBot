from openai import OpenAI
import pyttsx3

# 🔐 Setup OpenRouter API key and endpoint
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# 🎤 Text-to-speech
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ⌨️ User input
def listen():
    return input("Type your command: ")

# 🤖 Chat with AI
def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  # You can use other free models like 'meta-llama/llama-3-8b-instruct'
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 🔁 Loop
while True:
    command = listen()
    if command.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye, Rehan.")
        break
    if command:
        reply = chat_with_ai(command)
        print(f"JARVIS: {reply}")
        speak(reply)
