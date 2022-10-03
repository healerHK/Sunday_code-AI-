from googletrans import Translator
import speech_recognition as sr
import pyttsx3
translator = Translator() 
def speak(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[2].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_german(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[1].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_English(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[3].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_spain(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[4].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_french(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[5].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_japan(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[6].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_korean(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[7].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_Portuguese(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[8].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_russia(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[9].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
def speak_china(audio):
    friday=pyttsx3.init()    ;  
    voices = friday.getProperty('voices')
    friday.setProperty('voice', voices[10].id) 
    print('S.U.N.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
    
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print("Healer:")
        audio=c.record(source,duration=5)
    try:
        query = c.recognize_google(audio,language='vi-VN')
        print("Healer -->: {}".format(query))
    except sr.UnknownValueError:
        query=""
    return query
def trans():   
    speak("""tôi có thể giúp sếp phiên dịch các thứ tiếng như: Anh; Pháp, Nga, Đức,Tây Ban Nha, Bồ Đầu Nha, Nhật, Hàn Quốc, Trung Quốc.
      Mời sếp nói""")
    m=command().lower()
    langs=m;
    if "trong tiếng" in m or "tiếng" in m:    
         data=m.find("trong tiếng")
         m=m.replace(m[data:len(m)]," ")
         data2=m.find("tiếng")
         m=m.replace(m[data2:len(m)]," ")
    m=m.replace("nói như nào"," ")
    m=m.replace("nói như thế nào"," ")
    m=m.replace("nói thế nào"," ")
    print(m)
    if "anh" in langs or "english" in langs:
        translated = translator.translate(m, dest='en')
        msp=m+'được phiên dịch ra tiếng Anh  là'
        speak(msp)
        speak_English(translated.text)
    elif "đức" in langs or "german" in langs:
        translated = translator.translate(m, dest='de')
        msp=m+'được phiên dịch ra tiếng Đức là'
        speak(msp)
        speak_german(translated.text)
    elif "pháp" in langs or "french" in langs:
        translated = translator.translate(m, dest='fr')
        msp=m+'được phiên dịch ra tiếng Pháp là'
        speak(msp)
        speak_french(translated.text)
    elif "tiếng nhật" in langs or "japanese" in langs:
        translated = translator.translate(m, dest='ja')
        msp=m+'được phiên dịch ra tiếng Nhật là'
        speak(msp)
        speak_japan(translated.text)
    elif "tiếng hàn" in langs or "korean" in langs:
        translated = translator.translate(m, dest='ko')
        msp=m+'được phiên dịch ra tiếng Hàn là'
        speak(msp)
        speak_korean(translated.text)
    elif "tiếng nga" in langs or "russian" in langs:
        translated = translator.translate(m, dest='ru')
        msp=m+'được phiên dịch ra tiếng Nga là'
        speak(msp)
        speak_russia(translated.text)
    elif "tiếng trung" in langs or "chinese" in langs:
        translated = translator.translate(m, dest='zh-CN')
        msp=m+'được phiên dịch ra tiếng Trung là'
        speak(msp)
        speak_china(translated.text)
    elif "tây ban nha" in langs or "spain" in langs:
        translated = translator.translate(m, dest='es')
        msp=m+'được phiên dịch ra tiếng Tây Ban Nha là'
        speak(msp)
        speak_spain(translated.text)
    elif "bồ đầu nha" in langs or "portuguese" in langs:
        translated = translator.translate(m, dest='pt')
        msp=m+'được phiên dịch ra Bồ Đầu Nha là'
        speak(msp)
        speak_Portuguese(translated.text)
    else: speak("tôi không hiểu được, sếp vui lòng chỉ cần nói câu cần phiên dịch cộng với trong tiếng gì đó")
    speak("Tôi đã phiên dịch xong, sếp muốn sử dụng lại chỉ cần nói dịch thuật")
    

