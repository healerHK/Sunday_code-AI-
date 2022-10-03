import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import serial
Arduino_Serial = serial.Serial('COM5',9600)
s = Arduino_Serial.readline()
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[2].id) 

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

    
        