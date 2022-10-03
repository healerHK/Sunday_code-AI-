import datetime
import time
import pyautogui
import openpyxl
import pprint
import webbrowser as wb
import pyttsx3 
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 
def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
#---------------------------------------HH:MM:SS AM/PM----------------------------------------------------------

wb = openpyxl.load_workbook('D:\SUNDAY\\notesss.xlsx')
sheet = wb['Sheet1']
cells_hour = sheet['A2']
cells_min =sheet["B2"]
cells_Data =sheet["C2"]
hour=cells_hour.value
if hour >=12 :
    hour=hour-12
    peri="PM"
else: peri="AM"
min =cells_min.value

while True:
    now = datetime.datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if str(hour) ==current_hour:
        if str(min)==current_min:
            if int(current_sec)==0:
                if peri==current_period:
                    print(cells_Data.value)
                    exit()