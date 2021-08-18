import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour<=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. Please tell me how may I help you.")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('roydebayan2002@gmail.com','undertaker007')
    server.sendmail('roydebayan2002@gmail.com',to,content)
    server.close()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
    #   print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    #while True:
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Seacrching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            music_dir='E:\\01 KISHORE KUMAR ROMENTIC'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'email to harry' in query:
            try:
                speak("What should I say ?")
                content=takeCommand()
                to="roysamir614@gmail.com"
                sendEmail(to,content)
                speak("Email sent")
            except Exception as e:
                speak("Error found")



