import pyttsx3
import datetime 
import speech_recognition as sr
import os
import pyautogui
h=1; program=[]
def vn(audio):
    Sunday=pyttsx3.init()
    voices = Sunday.getProperty('voices')
    Sunday.setProperty('voice', voices[2].id)  
    print('S.U.N.D.A.Y: ' + audio)
    Sunday.say(audio)
    Sunday.runAndWait()
def speak(audio):
    friday=pyttsx3.init()
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[0].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.listen(source,phrase_time_limit=3)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(query))
    except sr.UnknownValueError:
        query=""
    return query  
def List_program():  
    h=1; program=[]
    vn("Sau đây là danh sách các ứng dụng có trên Start Menu:")
    dirname = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
    files = os.listdir(dirname)
    for i in files:
         if "lnk" in i:
             program.append(i)
             i=i.rstrip('.lnk')
             pro=str(h)+": "+str(i)
             speak(str(pro))
             h+=1
    vn("Bạn muốn mở ứng dụng nào trong danh sách trên: ")
    pro_open=input()
    bo=True
    for i in program:
        if pro_open in i: 
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\'+i)
            vn("Ứng dụng đã được mở")
            bo=True;
            break
        else:
            bo=False;
    if bo==False:
        vn("Không tìm thấy ứng dụng nào") 
def Word():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
    vn('Word đã được mở. Đã sẵn sàng để soạn thảo')
def Excel():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
    vn("Excel 2016 đã được mở. Đã sẵn sàng để soạn thảo")
def PowerPoint():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')
    vn("PowerPoint đã được mở. Đã sẵn sàng để soạn bài trình chiếu")
def Access():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access.lnk')
    vn("Access đã được mở. Đã sẵn sàng để xây dựng data base ")
def Garena():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Garena\Garena\Garena.lnk')
    vn("Garena đã được mở. Đã sẵn sàng để chơi game")
def search_Win():
    vn('ứng dụng bạn muốn tìm kiếm là gì')
    m=command().lower()
    pyautogui.keyDown('win')
    pyautogui.press('q')
    pyautogui.keyUp('win')
    pyautogui.write(m)
    pyautogui.press('Enter')



 