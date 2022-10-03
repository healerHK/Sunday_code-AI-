import wikipedia 
from googletrans import Translator
import  requests
from bs4 import BeautifulSoup
import pyttsx3
import re
import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if r.pause_threshold ==0.5:
            audio = r.listen(source)
        else: audio = r.listen(source,phrase_time_limit=5)
  
    try:
        query = r.recognize_google(audio, language ='vi-VN')
        print(f"Healer--->: {query}\n")
  
    except Exception as e:
        query=""
        return "None"
    return query


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[2].id) 

def speak(audio):
   print(audio)
   friday.say(audio)
   friday.runAndWait()   
   
response = requests.get("https://covid19.gov.vn/big-story/cap-nhat-dien-bien-dich-covid-19-moi-nhat-hom-nay-171210901111435028.htm")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.findAll( class_='kbwscwl-content clearfix',)
data=str(titles)
data_covid=data.replace('div class="kbwscwl-content clearfix">',"")
data_covid=data_covid.replace("</p><p>","")
data_covid=data_covid.replace("<<p>",'')
data_covid=data_covid.replace("</p></div>",'\n')
data_cv=data_covid.split("\n")
def ALL_covid():
   text = "Đại dịch COVID-19 ở Việt Nam"
   wikipedia.set_lang("en")
   contents = wikipedia.summary(text).split('\n')
   Sum_covid=contents[0].split('.')
   trans=Translator()
   for i in range(1,3):
      text=trans.translate(Sum_covid[i],dest='vi')
      speak(text.text)
def Prov_covid():
      speak("Bạn muốn biết cô vít về tỉnh thành nào ?")
      cvid=command(); a=0 ; sum=0
      if cvid not in data:
            print("Không tìm thấy tình thành nào")
      else:
         for i in range(0,3):
            progress=data_cv[i].split(",")
            for j in progress:
                  if cvid in j:
                     result=str(progress[a])
                     result=result.replace("Tính","")
                     speak(result) 
                     j=j.replace("(","có thêm ") 
                     j=j.replace(")", " ca mắc Cô Vít mới")   
                     speak(j)
                     N=re.findall(r'\d+', j)
                     sum=sum+int(N[0])

            a=1
         res="Tồng cộng 3 ngày qua tỉnh " + cvid +" đã có thêm "+str(sum)+" ca mắc mới"
         speak(res)
def covid():
   
   
   speak("Sếp muốn biết về Cô vít : tính hình chung , tình hình gần đây, tình hình của 1 tỉnh thành nào đó: ")
   infor=command().lower()
   if "tình hình chung" in infor:
         ALL_covid()
   elif "tình hình những ngày gần đây" in infor or "tình hình gần đây" in infor:   
         for i in range(0,3):
               vn=data_cv[i].split(":")
               speak(vn[0].replace("Các tỉnh, thành phố ghi nhận ca bệnh như sau",""))
   elif "tình hình của 1 tỉnh thành" in infor or "tình hình của một tỉnh thành" in infor:
      Prov_covid()
