import speech_recognition as sr
import pyttsx3
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize the speech recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

template = """
Answer the question below

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("I am Friday! Say 'exit' to quit.")
    speak("I am Friday! Say 'exit' to quit.")
    
    while True:
        user_input = listen()
        if user_input is None:
            continue
        if user_input.lower() == "exit":
            break
        
        result = chain.invoke({"context": context, "question": user_input})
        print("BOT:", result)
        speak(result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__=="__main__":
    handle_conversation()
