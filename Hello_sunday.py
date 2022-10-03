import SUNDAY_MAIN
import speech_recognition as sr
import webbrowser as wb
import covid 
import pyttsx3
sunday=pyttsx3.init()
voices =sunday.getProperty('voices')
sunday.setProperty('voice', voices[2].id)
def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    sunday.say(audio)
    sunday.runAndWait()
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=2)
  
    try:
        query = r.recognize_google(audio, language ='vi-VN')
        print(f"Healer--->: {query}\n")
  
    except Exception as e:
        query=""
        return "None"
    return query
while True:
    sunday=command().lower()
    if sunday=="":
        print('----')
    elif "sunday" in sunday or "sang đây" in  sunday or "Sony" in sunday:
        SUNDAY_MAIN.run()
    
    elif "covid" in sunday or "tình hình dịch" in sunday:
        covid.covid()
        speak("")