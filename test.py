import pyttsx3
friday=pyttsx3.init()
voices = friday.getProperty('voices')
for voice in voices:
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)
