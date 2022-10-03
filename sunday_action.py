import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import serial
import requests 
import random 
import pyautogui
import time
import unidecode
import wikipedia
import yagmail
import  pyaudio
import openpyxl
import Search_program


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[2].id) 

def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()

def thoigian():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        speak("Tôi có thể giúp gì cho sếp") 

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
def film():
    speak("Tôi có 2 lựa chọn cho sếp: 1 xem phim theo thể loại, 2 là xem phim theo tên đầy đủ(nếu tên phim không đầy đủ thì t")
def stop():
    speak('OK')

def weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = command()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pác-can
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)    
    else:
        speak("Không tìm thấy địa chỉ của bạn")

def mychoice():
    speak("Sếp hãy lựa chọn bộ phim mà mình muốn")
    while True:
         pyautogui.hscroll(-30)  
         time.sleep(1) 

def tell_me_about():
    try:
        speak("Sếp muốn nghe về gì ạ")
        text = command().lower()
        wikipedia.set_lang("Vi")
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(0)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = command().lower()
            if "có" not in ans:
                speak('ok sếp, thấy tôi ngầu chưa,haha!!!')
                break
            speak(content)
            time.sleep(0)

        
    except:
        speak("tôi không định nghĩa được thuật ngữ của bạn. Xin mời sếp nói lại")        


if __name__  =="__main__":
 welcome()
 while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        #Program 1:--------------------------------------Giao tiếp-----------------------------------------------------------
        if query=="":
            print("...")
        
        #Program 2:----------------------------------Dịch vụ mở ứng dụng------------------------------------------------
        elif "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "word" in query:
            Search_program.Word()
        elif "excell" in query:
            Search_program.Excel()
        elif "Powerpoint" in query:
            Search_program.PowerPoint()
        elif "Access" in query:
            Search_program.Access()
        elif "mở ứng dụng" in query:
            speak("Bạn muốn mở ứng dụng trên desktop hay bất kì:")
            pro=command().lower()
            if "bất kì" in pro:
                Search_program.search_Win()
            else: Search_program.List_program()
        
            
        #program 3:---------------------------------Dự báo thời tiết---------------------------------------------------
        elif "thời tiết" in query:
            weather()
            
        #program 4:--------------------------------------Wikidia-------------------------------------------------------
        elif "tra cứu" in query:
            tell_me_about()
            
        #program 4:----------------------------Nhạc vs Film--------------------------------------------------
        elif "mở nhạc" in query:
            list=range(1,7)
            music=str(random.choice(list))+".mp3"
            wb.open('D:\SUNDAY\\music\\'+music)
        elif "nhạc mạnh" in query:
            a=range(11,14)
            music=str(random.choice(a))+".mp3"
            wb.open('D:\SUNDAY\\music\\'+music)
        elif 'nhạc buồn' in query:
            b=range(30,34)
            music=str(random.choice(b))+'.mp3'
            wb.open('D:\SUNDAY\Music\\'+music)
            time.sleep(20)
            pyautogui.keyDown('Alt')
            pyautogui.press('F4')
            pyautogui.keyUp('Alt')
        
        elif "mở phim" in query or "phim" in query:
             speak('Sếp muốn xem phim gì') 
             film=command()
             if "hành động" in film:
              wb.open("https://mephimmy.com/") 
             if "tình cảm" in film:
              wb.open("https://mephimhanz.com/")    
             if "anime" in film:
              wb.open("https://anime47.com/")
             if "hài" in film:
              wb.open("https://www.haitetvn.com/")
             else:
              speak('Không có thể loại mà sếp yêu cầu')
                                         
        #program 6:--------------------------------------Ngày vs Giờ hiện tại------------------------------------------
        elif "mấy giờ" in query or "what time is it" in query:
                now = datetime.datetime.now()
                speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
        elif "ngày mấy " in query or "ngày bao nhiêu" in query:
            now = datetime.datetime.now()
            speak("Hôm nay là ngày %d tháng %d năm %d" %(now.day, now.month, now.year))
            
         #program 7:------------------------------------------Control led--------------------------------------------------------
        
            #program 8: --------------------------------------Funny story--------------------------------------------------------
        elif "goodbye" in query or "bye" in query or "tạm biệt" in query:
            exit()  
        
        
            
        