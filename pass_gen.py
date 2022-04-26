import string
import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def micro_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("password length..?")
        speak("what will be the length of your password?")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
        query = ''
        try:
            print("working on it...")
            speak('got it, creating your password..')
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            speak("I did not get that")
            return 'None'
        return query

if __name__=="__main__":
    command = micro_input().lower()
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3= string.digits
    s4= string.punctuation
    s=[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    p_len = int(command)
    print(p_len)
    random.shuffle(s)
    speak("Your password is:")
    print("".join(s[0:p_len]))
    speak("".join(s[0:p_len]))



