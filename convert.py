import pyttsx3
import speech_recognition as sr
import requests
import  re
path_w = 'D:\SUNDAY\money.txt'
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[2].id) 
def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.listen(source,phrase_time_limit=5)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(query))
    except sr.UnknownValueError:
        query=""
    return query
class Currency_convertor:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"] 
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount; 
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        with open(path_w,"w",encoding='UTF-8') as f:
             f.write("{} {} bằng  {} {}".format(str(initial_amount),from_currency,str(amount),to_currency))
def convert():    
          speak("Sếp muốn đổi đơn vị tiền tệ nào?")
          url = ('http://api.exchangeratesapi.io/v1/latest?access_key=2d22c3c25cba871ca70d4fb13501e9d6')  
          c = Currency_convertor(url)
          money=command().lower() ; money1=""; money2="";
          number= re.search(r'\d+', money)   
          money=money.replace(str(number.group()),"")
          if "nghìn" in money:
               number=str(number.group())+'000'
          if "triệu" in money:
               number=str(number.group())+'000000'
          if "tỷ" in money:
               number=str(number.group())+'000000000'
          div=len(money) // 2
          for i in range(0,div):
               money1=money1+money[i] 
          for i in range(div,len(money)):
               money2=money2+money[i]
          from_country="" ;to_country=""
          #----------------------------------------From_country---------------------------------------------------------
          if "đô la mỹ"  in money1 or "usd"in money1 or "mỹ" in money1:
               from_country= from_country+"USD"
          elif "việt" in money1 or "việt nam đồng" in money1 or "vnd" in money1:
               from_country=from_country+"VND"
          elif "won" in money1 or "hàn quốc" in money1:
               from_country=from_country+"KRW"
          elif "yên" in money1 or "nhật" in money1:
               from_country=from_country+"JPY"
          elif "nhân dân tệ" in money1 or "trung" in money1:
               from_country=from_country+"RMB"
          elif "đô la úc" in money1 or "aud" in money1:
               from_country=from_country+"AUD"
          elif "euro" in money1 or"tiền châu âu" in money1 or "ê rô" in money1:
               from_country=from_country+"EUR"
          elif "Rúp" in money1 or "nga" in money1:
               from_country=from_country +"RUB"
          elif "Ruppe" in money1 or "ấn" in money1:
               from_country=from_country+"INR"
          elif "thái" in money1 or "bạc thái" in money1:
               from_country=from_country +"THB"
          elif "bảng" in money1 or "anh" in money1:
               from_country=from_country +"GBP"
          else: 
               speak(" xin lỗi tôi không nhận biết được đơn vị tiền tệ bạn muốn đổi ")
               print(money)
               exit()
          #------------------------------------------To_Country--------------------------------------------------------
          if "đô la mỹ"  in money2 or "usd"in money2 or "mỹ" in money2:
               to_country=to_country+ "USD"
          elif "việt" in money2 or "việt nam đồng" in money2 or "vnd" in money2:
               to_country=to_country+"VND"
          elif "won" in money2 or "hàn quốc" in money2:
               to_country=to_country+"KRW"
          elif "yên" in money2 or "nhật" in money2:
               to_country=to_country+"JPY"
          elif "nhân dân tệ" in money2 or "trung" in money2:
               to_country=to_country+"RMB"
          elif "đô la úc" in money2 or "aud" in money2:
               to_country=to_country+"AUD"
          elif "euro" in money2 or"tiền châu âu" in money2 or "ê rô" in money2:
               to_country=to_country+"EUR"
          elif "Rúp" in money2 or "nga" in money2:
               to_country=to_country +"RUB"
          elif "Ruppe" in money2 or "ấn" in money2:
               to_country=to_country+"INR"
          elif "thái" in money2 or "bạc thái" in money2:
               to_country=to_country +"THB"
          elif "bảng anh" in money2 or "anh" in money2:
               to_country=to_country +"GBP"    
          else: 
               speak(" xin lỗi tôi không nhận biết được đơn vị tiền tệ bạn muốn đổi sang")
               exit()
          rult=str(c.convert(from_country,to_country,int(number)))
          with open(path_w,encoding='UTF-8') as f:
                    rult=f.read()
          speak(rult)
   
    
