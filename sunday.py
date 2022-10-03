import pyttsx3
import speech_recognition as sr
import os
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def command2():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.listen(source ,phrase_time_limit=5)
    try:
        sunday = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(sunday))
    except sr.UnknownValueError:
        sunday=""
    return sunday

def email():
    speak("""sếp muốn gửi mail cho ai trong danh sách những người bạn này:
             1.kim thoa, 2. Healer, .... Hoặc 0. lựa chọn khác """)
    receiver=command2().lower()
    if "một" in receiver:
        receiverto="kimthoa6a@gail.com"
    if "hai" in receiver:
        receiverto="ynguyenhk@gmail.com"
    if "không" in receiver:
         receivert=command2()

         receivert.replace(" ","").lower()
         receiverto=str(receivert)+"@gmail.com"
    speak("Sếp có muốn điền nội dung văn bản  không ")
    text=command2().lower()
    if "có" in text or "yes" in text or "ok" in text:
        texts=command2().lower()
    speak("Sếp có muốn đính kèm tệp không?")
    file=command2().lower()
    if "có" in file or "yes" in file or "ok" in file:

        speak("Tệp đính kèm sếp muốn gửi :")
        filename=command2().lower()
        path=('C:\\Users\\ynguy\\Documents\\Mail')
        dick=os.listdir(path)
        for i in dick:
            D=(i)
            if filename in D:
               print(i)
               fileto=i
            else:
                speak("không tìm thấy file")
    print(texts, receiverto, fileto)
while True:
    sunday=command2().lower()
    if sunday=="":
        print("Tôi không nghe bạn nói gì, xin nói lại")
    elif "gửi thư" in sunday:
        email()