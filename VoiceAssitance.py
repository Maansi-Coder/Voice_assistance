import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import pickle 
import pywhatkit
import tkinter as tk
from tkinter import messagebox 
from PIL import ImageTk, Image
from pywikihow import search_wikihow

window= tk.Tk()
window.geometry("700x350")
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Rubi: ",audio)
    
def take_command(pa=1):
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = pa
        audio= r.listen(source)
        
    try:
        print("Recognising.......")
        query= r.recognize_google(audio, language= "en-in")
        
    except Exception as e:
        print(e)
        
        print("Say that again please ..........")
        return "None"
    
    return query

def command():
    speak("Hello "+ text.get())
    speak("How can I help you ")
    while True:
        query= take_command().lower()
        print(query)
        
        if 'wikipedia' in query:
            speak("Serching wikipedia...")
            query= query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=2)
            speak("Wikipedia says")
            print(result)
            speak(result)
    
        elif "open youtube" in query:
            speak("What should I search on youtube")
            sea= take_command()
            a= 'https://www.youtube.com/results?search_query='+sea
            webbrowser.open(a)
            speak("I found this on your search")

        elif "open google" in query:
            speak("What should I search on Google")
            search= take_command()
            search=search.replace("search","")
            pywhatkit.search(search)
            
        elif "open whatsapp" in query:
            webbrowser.open('https://web.whatsapp.com/') 
            
        elif "fine" in query:
            speak("I am glad to hear that")
            
        elif "how are you" in query:
            speak("I am Fine")
            
        elif "thank you" in query:
            speak("I am glad to help you")
            
        elif "tell me about" in query:
            query= query.replace("tell me about", "")
            pywhatkit.info(query,3)
            
        elif "time" in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak("The Time is ")
            speak(strtime)
            
        elif "date" in query:
            strdate= datetime.datetime.now().date()
            speak("The Date is ")
            speak(strdate)
            
        elif "how to " in query:
            query= query.replace("how to","")
            max_results= 1
            how_to= search_wikihow(query, max_results)
            assert len(how_to)==1
            how_to[0].print()
            speak(how_to[0].summary)
            
        elif "sleep" in query:
            speak("You can call me any time")
            break;
        
def start():
    if text.get() == "" :
        messagebox.showwarning("warning", "Please enter the name first!!") 
        return
    command()
    
    



l1= tk.Label(window,text="Hello! Whats your name? ",font="Georgia 30 italic bold")
l1.place(relx=0.15,rely=0.2)

text = tk.StringVar() 
entry1 = tk.Entry(window, textvariable = text, width=25,justify = "center",font="Arial 20 italic bold") 
entry1.focus_force() 
entry1.place(relx=0.25,rely=0.4)

b= tk.Button(window,text="Start",font="Arial 20 italic bold",command=start)
b.place(relx=0.8,rely=0.6)

window.mainloop()
