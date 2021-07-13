import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from requests import *
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak(" Sir Jarvis Here!! Please tell me how can I help You")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vprasad1514@gmail.com', 'prasad2147')
    server.sendmail('your email id', to, content)
    server.close()





if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        if "open notepad" in query:
            apath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(apath)

        elif "open visual studio" in query:
            apath = "C:\\Users\\prasa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\phone\\UCDownloads"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "show my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "open YouTube" in query:
            webbrowser.open("www.youtube.com")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open Facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open YouTube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("sir, what should i search in google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919010098903","this is testing protocol",1,25)

        elif "play song on youtube" in query:
            rd = random.choice
            kit.playonyt("rd")

        elif "email to me" in query:
            try:
                speak("what should I say")
                content = takecommand().lower()
                to = "vadlamudiprasadbhimu@gmail.com"
                sendEmail(to,content)
                speak("email had been sent to me")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to send this mail")


        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()

        speak("sir, do you have any other work")



            #takecommand()
    #speak("Hi Nikhitha! This is Jarvis!!! How can I help you!!")