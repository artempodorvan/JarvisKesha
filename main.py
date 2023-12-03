import speech_recognition as sr
import os
import sys
import pyttsx3
import random
from datetime import datetime
import webbrowser
from bs4 import BeautifulSoup
import requests
import subprocess
import pyttsx3
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title('Jarvis Kesha')
root.geometry("500x600")

bg_label = tk.Label(root)
bg_label.place(relwidth=1, relheight=1)

def close_window():
    root.destroy()

button = tk.Button(root, text="Start", font=("Arial", 20), bg="red", command=close_window)
button.place(relx=0.5, rely=0.1, anchor="center", width=350, height=100)

root.mainloop()

url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

recognizer = sr.Recognizer()
tts = pyttsx3.init()

jokes = [
    'Why don\'t scientists trust atoms? Because they make up everything!',
    'Did you hear about the mathematician who\'s afraid of negative numbers? He\'ll stop at nothing to avoid them.',
    'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'How do you organize a space party? You "planet"!',
    'Why did the bicycle fall over? Because it was two-tired!'
]
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en")
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return ""

    except sr.RequestError as e:
        print("Speech recognition error: {0}".format(e))
        return ""
def speak_text(text):
    tts.setProperty('rate', 120)
    tts.setProperty('voice', 'en')
    tts.say(text)
    tts.runAndWait()
def get_weather():
    weather_info = ""

    main_loaded = soup.find("div", class_="main loaded")

    if main_loaded:
        date_element = main_loaded.find("p", class_="date")
        now = datetime.now()
        current_date = now.strftime("%d")

        if date_element and date_element.text.strip() == current_date:

            temperature_element = main_loaded.find("div", class_="temperature")
            if temperature_element:
                min_temperature = temperature_element.find("div", class_="min").find("span").text.strip()
                max_temperature = temperature_element.find("div", class_="max").find("span").text.strip()

                min_temperature = str(min_temperature)
                max_temperature = str(max_temperature)
                weather_info = f"Kyiv weather: Min temperature: {min_temperature}, Max temperature: {max_temperature}."

    return weather_info
def create_folder():
    folder_name = 'folder'
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    new_folder_path = os.path.join(desktop_path, folder_name)

    try:
        os.mkdir(new_folder_path)
        speak_text(f" {folder_name} was created on the desktop")

    except FileExistsError:
        speak_text(f"{folder_name} already exists")

    except Exception as e:
        speak_text(f"error{str(e)}")

number = 0
run = True
roblox_process = None

while run:
    user_input = recognize_speech()

    if user_input:
        response = "You said: " + user_input
        print("Bot response:", response)

        if "kesha" in user_input or 'jarvis' in user_input:
            speak_text("yes sir")
            number += 1

        elif "your developer is" in user_input and number != 0:
                speak_text('I\'m created by Artem Podorvan. He is a senior programmer and he destroy NASA.')

        elif 'tell me about yourself' in user_input and number != 0:
            speak_text('I\'m Jarvis or Kesha i have two names and I like eating, pooping, spitting, and everything horrible that my developer taught me.')

        elif 'tell me a joke' in user_input and number != 0:
            number = random.randint(0, 4)
            speak_text(jokes[number])

        elif 'what time is it' in user_input and number != 0:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            speak_text(f"The current time is {current_time}")

        elif 'open youtube' in user_input and number != 0:
            webbrowser.open("https://www.youtube.com")

        elif 'climate' in user_input and number != 0:
            weather_info = get_weather()
            if weather_info:
                speak_text(weather_info)
            else:
                speak_text("I couldn't find weather information for today.")

        elif 'open roblox' in user_input and number != 0:
            if roblox_process is None:
                program_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Roblox\Roblox Player.lnk"

                try:
                    roblox_process = subprocess.Popen(program_path, shell=True)
                    speak_text("Roblox Player opened successfully")

                except Exception as e:
                    print(f"Error opening Roblox Player: {str(e)}")

            else:
                speak_text("Roblox Player is already running.")

        elif 'open viber' in user_input and number != 0:
            if roblox_process is None:
                program_path = r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Viber.lnk"

                try:
                    roblox_process = subprocess.Popen(program_path, shell=True)
                    speak_text("Roblox Player opened successfully")

                except Exception as e:
                    print(f"Error opening Roblox Player: {str(e)}")

            else:
                speak_text("Viber is already running.")

        elif 'open telegram' in user_input and number != 0:
            if roblox_process is None:
                program_path = r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk"

                try:
                    roblox_process = subprocess.Popen(program_path, shell=True)
                    speak_text("Telegram opened successfully")

                except Exception as e:
                    print(f"Error opening Roblox Player: {str(e)}")

            else:
                speak_text("Viber is already running.")

        elif 'create a folder' in user_input and number != 0:
            create_folder()

        elif 'see you later' in user_input and number != 0:
            speak_text('see you never monkey')
            sys.exit(0)
