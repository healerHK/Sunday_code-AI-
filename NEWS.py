import  pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
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
        audio=c.listen(source ,phrase_time_limit=3)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(query))
    except sr.UnknownValueError:
        query=""
    return query
def news():   
    n=0; detail=[""]; Sum_news=[]; contents=[]
    response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll('h3', class_='title-news')
    links = [link.find('a').attrs["href"] for link in titles]
    speak("Theo báo tuoitre.vn, những tin tức mới nhất được liệt kê với những tiêu đề dưới đây: ")
    for link in links :
        news = requests.get("https://tuoitre.vn" + link)
        soup = BeautifulSoup(news.content, "html.parser")
        title = str(soup.find("h1", class_="article-title"))
        newtitle=title.replace('<h1 class="article-title">',"").replace('</h1>',"")
        abstract = str(soup.find("h2", class_="sapo")).replace('<h2 class="sapo">',"").replace('</h2>',"")
        body = soup.find("div", id="main-detail-body")
        content = body.findChildren("p", recursive=False)[0].text +      body.findChildren("p", recursive=False)[1].text
        contents.append(content)
        n+=1
        if n<6:
            new="tiêu đề "+str(n)+": " + newtitle
            Sum_news.append(str(new))
            speak(str(new))
            detail.append(abstract)
            #print("Mô tả: " + abstract)
            print("________________________")
        else:
            break
    while True:
        speak("Bạn nghe mô tả hay nội dung của tiêu đề nào")
        m=command().lower()
        print(m)
        if ("không" or "0" or "khỏi") in m:
            speak("Ok Sếp. Chúc sếp 1 ngày tốt lành")  
            break
        else:
            for i in range (0,6):
                if m in Sum_news[i]:
                    describe= "Tiêu đề",i+1,"được mô tả như sau:" + detail[int(i+1)]
                    speak(str(describe))
                    speak("Cảm ơn bạn đã lắng nghe")
                    break
                else: 
                    speak('Tiêu đề của sếp không có. Xin vui lòng thử lại hoặc là không. ')
                    break
         
    
      