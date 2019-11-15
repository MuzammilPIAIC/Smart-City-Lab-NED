import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty("voice",voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good evening")


    speak("I am Jarvis sir. Please tell me how mai I help you")



def takeCommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print("user said: ",query)
    except Exception as e:
        print('say again')
        return "None"
    return query
    

def house_price(area,no_of_bedrooms):
    df=pd.read_csv("sample3.csv")
    reg=LinearRegression()
    reg.fit(df[["area","bedrooms"]],df.price)
    x=reg.predict([[area,no_of_bedrooms]])
    return x
    
    
    
    
if __name__ == "__main__":
    wishme()
    while True:
    
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open coursera" in query:
            webbrowser.open("coursera.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif "open browser" in query:
            path='"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
            os.startfile(path)
        elif "house" in query:
            try:
                speak("how much area you required")
                area=takeCommand()
                speak("Please tell me number of bedrooms you are required")
                no_of_bedrooms=takeCommand()
                print("number of bedroom are:",no_of_bedrooms)
                final=house_price(float(area),float(no_of_bedrooms))
                
                print(final)
                speak(final)
                
            except Exception as e:
                print(e)
                speak("i am not able to predict this")
                print("sorry sir")




