import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import os
from typing import Dict, Any
from flask import Flask

rec = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def task(c):
    print(c)
    if "open behance" in c.lower():
        webbrowser.open("https://www.behance.net")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://Instagram.com")
    elif "open google" in c.lower():
        webbrowser.open("https://Google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "shutdown" in c.lower():
        os.system("shutdown /s /t 1")
    elif "restart" in c.lower():
        os.system("shutdown /r /t 1")
    elif "info" in c.lower():
        os.system("systeminfo")  
    elif "open spotify app" in c.lower():
        os.system("start Spotify")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        return None
    

class GeminiAPI:
    def __init__(self, api_key: str):
        
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_text(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating text: {str(e)}"
    

   

def main(sp):
    api_key = "AIzaSyCimOOgJwHxrml6DJg7-oY8NkNKnWVRnog"
    gemini = GeminiAPI(api_key)
    response = gemini.generate_text(n)
    print("Text Generation Response:", response)
    speak(response)


if __name__ == "__main__":
    speak("Command ME Pratyush..")
    
    while True:
        r = sr.Recognizer()


        print("recognizing...")  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, )
            command = r.recognize_google(audio)
            print(command)
            sta=command.split()
            print(sta)
            cod=str(" ".join(sta[1:]))
            
            n=cod.lower()
            print(n)
            def do(n):
                result = task(n) or main(n)
                return result
            do(n)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError:
            print("Network error. Please check your connection.")
            speak("Network error. Please check your connection.")

            
        




        
        
