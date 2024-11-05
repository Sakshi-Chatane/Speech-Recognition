# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:47:36 2024

@author: Sakshi Chatane
"""

import speech_recognition as sr

# For recognizing speech input
r = sr.Recognizer()

# Initiating Speech Recognition by using Recognizer function.
while True:
    try:
        with sr.Microphone() as source:
            print("Speak Something...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(f"Recognized Text: {text}")

            # Exit condition to break the loop if the user says "exit"
            if text == "exit":
                print("Exiting...")
                break
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
    except Exception as e:
        print("You are trying to be funny")
        print(f"Error: {e}")
    
    # Re-initialize the recognizer after each iteration
    r = sr.Recognizer()


        
"""import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def recognize_speech():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something...")

        # Listen for the user's input
        audio = recognizer.listen(source)

        try:
            # Convert the audio to text using Google's speech recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("Could not request results; please check your internet connection.")

# Run the function
recognize_speech()
"""