import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import threading
import serial
import requests
import random
import pyautogui
import time
import wikipedia
import pyaudio
import openpyxl
import Search_program
import convert
import translate
import Sunday_boy as SB
from Funny_stories import Story

from Communication import communication
from Alarm_clock import set_alarm
import NEWS
import covid
friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[0].id)
friday.setProperty('rate', 300)


def speak(audio):
    print('Healer:'+audio)
    for i in audio:
        if i == "." or i == ',':
            audio = audio.replace(i, '\n')
    for i in audio.splitlines():
        friday.say(i)
        friday.runAndWait()


def thoigian():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It is")
    speak(Time)


def welcome():
    # Chao hoi
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Chào buổi sáng, sếp!")
    elif hour >= 12 and hour < 18:
        speak("Chào buổi chiều, sếp!")
    elif hour >= 18 and hour < 24:
        speak("Chào buổi tối, sếp!")
    speak("Tôi có thể giúp gì cho sếp?")


def command():
    r = sr.Recognizer()
    try:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=None)
            query = r.recognize_google(audio, language='vi-VN')
            query = query.lower()
            print(f"Healer--->: {query}\n")
    except sr.UnknownValueError:
        r = sr.Recognizer()
        return
    return query


def film():
    speak("Tôi có 2 lựa chọn cho sếp: 1 xem phim theo thể loại, 2 là xem phim theo tên đầy đủ(nếu tên phim không đầy đủ thì t")


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
        Trời hôm nay quang mây. Dự báo nắng nóng ở 1 số nơi.""".format(day=now.day, month=now.month, year=now.year, hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                       hourset=sunset.hour, minset=sunset.minute,
                                                                       temp=current_temperature, pressure=current_pressure, humidity=current_humidity)
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
                break
            speak(content)
            time.sleep(0)

        speak('ok sếp, thấy tôi ngầu chưa,haha!!!')
    except:
        speak("tôi không định nghĩa được thuật ngữ của bạn. Xin mời sếp nói lại")


welcome()
while True:
    query = command()
# All the command will store in lower case for easy recognition
# Program 1:--------------------------------------Giao tiếp-----------------------------------------------------------
    if query == None:
        print("....")
# Program 2:----------------------------------Dịch vụ mở ứng dụng------------------------------------------------
    elif "mở google" in query:
        speak("Sếp muốn tôi tìm gì")
        search = command()
        url = f"https://google.com/search?q={search}"
        wb.get().open(url)
        speak(f'Đây là kết quả {search} trên google')
    elif "mở youtube" in query:
        speak("Sếp muốn tôi tìm gì")
        search = command()
        url = f"https://youtube.com/search?q={search}"
        wb.get().open(url)
        speak(f'Đây là kết quả {search} trên youtube')
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
        pro = command().lower()
        if "bất kì" in pro:
            Search_program.search_Win()
        else:
            Search_program.List_program()
    elif "đóng google" in query or "đóng youtube" in query:
        pyautogui.hotkey('Ctrl', 'w')
        speak("Tôi đã đóng ứng dụng")
# program 3:--------------------------------------Dự báo thời tiết---------------------------------------------------
    elif "thời tiết" in query:
        weather()

# program 4:--------------------------------------Wikidia-------------------------------------------------------
    elif "tra cứu" in query or "bách khoa toàn thư" in query:
        tell_me_about()

# program 4:--------------------------------------Nhạc vs Film--------------------------------------------------
    elif "mở nhạc" in query:
        speak('Sếp muốn tôi mở nhạc gì')
    elif "tùy" in query or "tự chọn" in query:
        list = range(1, 7)
        music = str(random.choice(list))+".mp3"
        wb.open('D:\SUNDAY\\music\\'+music)
    elif "nhạc mạnh" in query:
        a = range(11, 14)
        music = str(random.choice(a))+".mp3"
        wb.open('D:\SUNDAY\\music\\'+music)
    elif 'nhạc buồn' in query:
        b = range(30, 34)
        music = str(random.choice(b))+'.mp3'
        wb.open('D:\SUNDAY\Music\\'+music)
    elif 'tắt nhạc' in query:
        time.sleep(2)
        pyautogui.hotkey('win', 'q')
        time.sleep(1)
        pyautogui.write("Groove")
        pyautogui.press('Enter')
        time.sleep(2)
        pyautogui.hotkey('Alt', 'F4')
    elif "mở phim" in query or "phim" in query:
        speak('Sếp muốn xem phim gì')
        films = command().lower()
        if "hành động" in films:
            wb.open("https://mephimmy.com/")
        if "tình cảm" in films:
            wb.open("https://mephimhanz.com/")
        if "anime" in films:
            wb.open("https://anime47.com/")
        if "hài" in films:
            wb.open("https://www.haitetvn.com/")
        else:
            speak('Không có thể loại mà sếp yêu cầu')

# program 6:--------------------------------------Ngày vs Giờ hiện tại------------------------------------------
    elif "mấy giờ" in query:
        now = datetime.datetime.now()
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày mấy" in query or "ngày bao nhiêu" in query:
        now = datetime.datetime.now()
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))

# program 7:------------------------------------------Control led--------------------------------------------------------

# program 8: --------------------------------------Funny story------------------------------------------------------------------
    elif "truyện hài" in query or "truyện cười" in query or "kể chuyện" in query:
        Story.funnyst()
# Program 9:---------------------------------------Convert-----------------------------------------------------------------------
    elif "đổi tiền" in query or "đổi đơn vị" in query:
        convert.convert()
# Program 10:--------------------------------------Translate----------------------------------------------------------------------
    elif 'dịch thuật' in query or 'dịch giúp tôi' in query or 'phiên dịch' in query:
        translate.trans()
# Program 11:--------------------------------------News--------------------------------------------------------------------------
    elif 'tin tức' in query or "báo hôm nay" in query or "tin gì hot" in query or "có tin gì mới" in query:
        NEWS.news()
# Program 12:--------------------------------------My_Doctor----------------------------------------------------------
    elif 'chẩn đoán bệnh' in query or 'cứu tôi với' in query or "tro ly ao" in query:
        wb.open('D:\SUNDAY\Doctor\doctormain.pyw')
    elif 'dừng lại' in query:
        with open("D:\SUNDAY\Stop.txt", mode='w', encoding='UTF-8') as f:
            f.write("dừng lại")
# Program 13:--------------------------------------Alarm_clock---------------------------------------------------------
    elif 'báo thức' in query or 'đặt giờ' in query or 'đặt hẹn' in query or 'hẹn giờ' in query:
        set_alarm.set_time()
# program 14:--------------------------------------MY_DOOR--------------------------------------------------------------

# program 15:-------------------------------------Sunday_boy---------------------------------------------------------------

# Program 16:-------------------------------------Covid_pandemic------------------------------------------------------------
    elif 'tình hình côvít' in query or "tình hình dịch" in query:
        covid.covid()
# Program 17:------------------------------------AI_mouse----------------------------------------------------------------------
    elif 'chuột ảo' in query or 'chuột thông minh' in query:
        speak("tôi đang khởi động chuột thông minh, hãy chờ tôi trong giây lát")
        wb.open('D:\SUNDAY\AI_mouse\mouse.pyw')
# Program 18:------------------------------------Sunday_SOS--------------------------------------------------------------

# Program 19:-----------------------------------Yamail_Face_detect-----------------------------------------------------
    elif 'bật chế độ vắng nhà' in query or 'bật chế độ không nhà' in query:
        open("D:\SUNDAY\Face_detect\Face_detect.txt", mode='w').close
        with open("D:\SUNDAY\Face_detect\Face_detect.txt", mode='w', encoding='UTF-8') as ff:
            ff.write("có")
        speak(
            'chế độ vắng nhà đã được bật, tôi sẽ gửi gmail cho sếp khi có người tới nhà')
    elif 'tắt chế độ vắng nhà' in query or 'tắt chế độ không nhà' in query:
        open("D:\SUNDAY\Face_detect\Face_detect.txt", mode='w').close
        speak('chế độ vắng nhà đã tắt')
# Program 20:------------------------------------Sunday-eyes----------------------------------------------------------
    elif 'bật thiên lý nhãn' in query or 'bật camera cảm xúc' in query or "bật camera phân tích cảm xúc" in query:
        open('D:\SUNDAY\Opencv\sunday_eyes.txt', 'w').close
        wb.open("D:\SUNDAY\Opencv\Sunday_eyes.pyw")
        speak('tôi đang khởi chạy camera, sếp vui lòng chờ 1 lúc')
    elif 'tắt thiên lý nhãn' in query or 'tắt camera cảm xúc' in query or "tắt camera phân tích cảm xúc" in query:
        with open('D:\SUNDAY\Opencv\sunday_eyes.txt', 'w', encoding='UTF-8') as fs:
            fs.write('tắt')
            fs.close
        speak('Tôi đã tắt camera')
    elif 'bật camera ngoài cổng' in query or 'bật camera nhận diện' in query or "bật camera an ninh" in query:
        open('D:\SUNDAY\Face_detect\Face_stop.txt', 'w').close
        wb.open("D:\SUNDAY\Face_detect\Face_detect.pyw")
        speak('tôi đang khởi chạy camera, sếp vui lòng chờ 1 lúc')
    elif 'tắt camera ngoài cổng' in query or 'tắt camera nhận diện' in query or "tắt camera an ninh" in query:
        with open('D:\SUNDAY\Face_detect\Face_stop.txt', 'w', encoding='UTF-8') as fs1:
            fs1.write('tắt')
            fs1.close
        speak('Tôi đã tắt camera')
# Program 21:----------------------------------Sleep mode-------------------------------------------------------------
    elif "bye" in query or "goodbye" in query or "tạm biệt" in query:
        speak("ok sếp, chúc sếp 1 ngày tốt lành")
        break
    else:
        communication.trochuyen(query)
