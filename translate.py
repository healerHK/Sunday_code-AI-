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
    speak("""t??i c?? th??? gi??p s???p phi??n d???ch c??c th??? ti???ng nh??: Anh; Ph??p, Nga, ?????c,T??y Ban Nha, B??? ?????u Nha, Nh???t, H??n Qu???c, Trung Qu???c.
      M???i s???p n??i""")
    m=command().lower()
    langs=m;
    if "trong ti???ng" in m or "ti???ng" in m:    
         data=m.find("trong ti???ng")
         m=m.replace(m[data:len(m)]," ")
         data2=m.find("ti???ng")
         m=m.replace(m[data2:len(m)]," ")
    m=m.replace("n??i nh?? n??o"," ")
    m=m.replace("n??i nh?? th??? n??o"," ")
    m=m.replace("n??i th??? n??o"," ")
    print(m)
    if "anh" in langs or "english" in langs:
        translated = translator.translate(m, dest='en')
        msp=m+'???????c phi??n d???ch ra ti???ng Anh  l??'
        speak(msp)
        speak_English(translated.text)
    elif "?????c" in langs or "german" in langs:
        translated = translator.translate(m, dest='de')
        msp=m+'???????c phi??n d???ch ra ti???ng ?????c l??'
        speak(msp)
        speak_german(translated.text)
    elif "ph??p" in langs or "french" in langs:
        translated = translator.translate(m, dest='fr')
        msp=m+'???????c phi??n d???ch ra ti???ng Ph??p l??'
        speak(msp)
        speak_french(translated.text)
    elif "ti???ng nh???t" in langs or "japanese" in langs:
        translated = translator.translate(m, dest='ja')
        msp=m+'???????c phi??n d???ch ra ti???ng Nh???t l??'
        speak(msp)
        speak_japan(translated.text)
    elif "ti???ng h??n" in langs or "korean" in langs:
        translated = translator.translate(m, dest='ko')
        msp=m+'???????c phi??n d???ch ra ti???ng H??n l??'
        speak(msp)
        speak_korean(translated.text)
    elif "ti???ng nga" in langs or "russian" in langs:
        translated = translator.translate(m, dest='ru')
        msp=m+'???????c phi??n d???ch ra ti???ng Nga l??'
        speak(msp)
        speak_russia(translated.text)
    elif "ti???ng trung" in langs or "chinese" in langs:
        translated = translator.translate(m, dest='zh-CN')
        msp=m+'???????c phi??n d???ch ra ti???ng Trung l??'
        speak(msp)
        speak_china(translated.text)
    elif "t??y ban nha" in langs or "spain" in langs:
        translated = translator.translate(m, dest='es')
        msp=m+'???????c phi??n d???ch ra ti???ng T??y Ban Nha l??'
        speak(msp)
        speak_spain(translated.text)
    elif "b??? ?????u nha" in langs or "portuguese" in langs:
        translated = translator.translate(m, dest='pt')
        msp=m+'???????c phi??n d???ch ra B??? ?????u Nha l??'
        speak(msp)
        speak_Portuguese(translated.text)
    else: speak("t??i kh??ng hi???u ???????c, s???p vui l??ng ch??? c???n n??i c??u c???n phi??n d???ch c???ng v???i trong ti???ng g?? ????")
    speak("T??i ???? phi??n d???ch xong, s???p mu???n s??? d???ng l???i ch??? c???n n??i d???ch thu???t")
    

