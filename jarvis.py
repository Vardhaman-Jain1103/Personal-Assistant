import ctypes
from socket import timeout
import time
import re
import webbrowser
from winsound import PlaySound
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import os
import subprocess as sp
import cv2
import random
import pyautogui 
import smtplib
from requests import get
import json
import socket
import json
import pywhatkit
from urllib.request import urlopen
import requests

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    
    if hour>=6 and hour<=12:
        speak(f"Good Morning its {tt}")
    elif hour>12 and hour<=18:
        speak(f"Good Afternoon its {tt}")
    elif hour>18 and hour<24:
        speak(f"Good Evening its {tt}")
    else:
        speak("Good Night")

def sendEmail(to,content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vardhamanjainalt@gmail.com', 'VardhamanJain123456789')
    server.sendmail('vardhamanjainalt@gmail.com', to, content)

if __name__ == "__main__":
    wish()
    speak("This is advance jarvis! how may i help you?")

def run_jarvis():
    command = take_command()
    print(command)

    #notepad
    if 'open notepad' in command:
        npath = "C:\\windows\\system32\\notepad.exe"
        os.startfile(npath)
        speak("Opening notepad")
    
    #chrome
    elif 'open chrome' in command:
        cpath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(cpath)
        speak("Opening chrome")

    #command prompt
    elif 'open command prompt' in command:
            cppath = "C:\\windows\\system32\\cmd.exe"
            os.startfile(cppath)
            speak("Opening command prompt")

    # #camera
    # elif 'open camera' in command:
    #     speak("Opening camera")
    #     def open_camera():
    #     sp.run('start microsoft.windows.camera:', shell=True)

    #open insta
    elif "open instagram" in command:
        webbrowser.open("www.instagram.com")
        speak("Opening Instagram")
    #music
    elif "play music" in command:
        music_dir = "D:\\love songs"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
        speak("playing  music")

    #google
    elif "open google" in command:
        speak("Sir what should i search in google")
        # cm = take_command().lower()
        # webbrowser.open("{cm}")
        # speak("Opening google")
        # url = "http://docs.python.org/library/webbrowser.html"
        # webbrowser.get(using='google-chrome').open(url,new=new)
        import wikipedia as googleScrap
        query=query.replace("google","")
        speak("This is what i found on google")
        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query, 3)
            speak(result)
        except:
            speak("No data found")

    #youtube
    elif "open youtube" in command:
        webbrowser.open("www.youtube.com")
        speak("Opening youtube")

    #elif "send message" in command:
        kit.sendwhatmsg("+919822054114", "Hi",0,0)
        speak("message send")

    # #elif "email" in command:
    #     try:
    #         speak("What should i say")
    #         content = take_command().lower()
    #         to = "jainvardhaman1103@gmail.com"
    #         sendEmail(to, content)
    #         speak("Email has been send succesfully")

    #     except Exception as e:
    #         print(e)
    #         speak("error in sending email")

    #music
    elif 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        kit.playonyt(song)
        speak("playing music")

    #time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)

    #info
    elif 'who is' in command:
        person = command.replace("who the heck is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    #alarm
    elif "set alarm" in command:
        speak("At what time sir?")
        time = input(": Enter the Time :")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M")

            if now == time:
                speak("Time to wake up sir")
                PlaySound("ringtone.mp3")
                speak ("Alarm closed")

            elif now>time:
                break

    #shutdown
    elif "shutdown" in command:
        os.system("shutdown /s /t 30")

    #restart
    elif "restart" in command:
       sp.call(["shutdown", "/r"])

    #sleep
    #elif "sleep"  or "hibernate" in command:
        #os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    #lock windiw
    elif 'lock window' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
    
    #close notepad    
    elif "close notepad" in command:
        speak("Okay sir! closing notepad")
        os.system(  "taskkill /f /im notepad.exe")

    #close command prompt
    elif "close command prompt" in command:
        speak("okay sir, closing command prompt")
        os.system("taskkill /f /im cmd.exe")

    #close chrome
    elif "close chrome" in command:
        speak("okay sir, closing command prompt")
        os.system("taskkill /f /im chrome.exe")

    #close music
    elif "close music" in command:
        speak("okay sir, closing music")
        os.system("taskkill /f /im D:\\love songs")

    #switch the window
    elif "switch the window" in command:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    #ip address
    elif "ip address" in command:
        ip_address = requests.get('https://api64.ipify.org?format=json').json()
        speak(ip_address)
        return ip_address["ip"]
        
    # # calling the Nominatim tool
    # elif "where i am" or "where are we" in command:
    #     speak("Wait sir! let me check")
    #     url='http://ipinfo.io.json'
    #     response=urlopen(url)
    #     data=json.load(response)
    #     print(data)

    #reminder
    elif "remember that" in query:
        remebermsg= query.replace("remeber that","")
        remebermsg = query.replace("jarvis", "")
        speak("You told me to remind you that: "+remebermsg)
        remeber = open('data.txt', 'w')
        remeber.write(remebermsg)
        remeber.close()

    elif "what do you remeber" in command:
        remeber.open('data.txt', 'r')
        speak("You told me that" + remeber.read())
    # #exit
    elif "no thanks" or "thanks" in command:
        speak("thanks for using me bye")
        os.system.exit()


    # elif re.search('weather', command):
    #     city = command.split(' ')[-1]
    #     weather_res =  weather(city=city)
    #     print(weather_res)
    #     speak(weather_res)
        
    else:
        speak('Please say the command again.')

    speak("sir do you have any other work")

while True:
    run_jarvis()