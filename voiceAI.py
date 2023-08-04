#to convert text to speech using pyttsx3
import pyttsx3
import speech_recognition as sr
#to search in web
import webbrowser
import datetime
import pyjokes
import os
#using time module to elapse some time for voice AI to restart after a run
import time
import smtplib
#converting speech to text

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sptext():
    recognizer=sr.Recognizer()
    #microphone to record  
    with sr.Microphone() as source:
        print("Listening.....")
        #removing background noise from source
        recognizer.adjust_for_ambient_noise(source)
        #creating audio variable to store voice
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            #using google recognizer to store voice
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understanding")

#converting text to speech
def speechttx(x):
    
    engine= pyttsx3.init()
    voices=engine.getProperty('voices')
    #use voices[0] for male voice and voice[1] for female voice
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    #setting the speed of voice if not set default speed is taken
    engine.setProperty('rate',150)
    engine.say(x)
    #converting speech to text
    engine.runAndWait()

if __name__=='__main__':
    #making speech to text function case insensitive
    if "friday" in sptext().lower():
        speechttx("Hi Nishanth hope you are doing good")
        while True:
            speech=sptext()
            data1=speech.lower()
            if "made you" in data1:
                creator ="I was created by Nishanth Mungara on 18 of July 2023"
                speechttx(creator)
                
            elif "your name" in data1:
                name="My name is Friday"
                speechttx(name)
                
            elif "time" in data1:
                #strftime is used to search time %I for hours %M for mins and %p for Am or Pm
                time=datetime.datetime.now().strftime("%I%M%p")
                speechttx("Hey Nishanth the time is")
                speechttx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "open mail" in data1:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
            elif "joke" in data1:
                #setting language of joke and category of jokes
                joke_1=pyjokes.get_joke(language="en",category="all")
                print(joke_1)
                speechttx(joke_1)
            elif "play song" in data1:
                addr="D:\Projects\MyVoiceAsst\songs"
                #make the os print list of songs
                listsong=os.listdir(addr)
                print(listsong)
                #starting file using start fun of os
                print("Enter the song Number")
                speechttx("Please enter the song number from the list")
                index=int(input())
                os.startfile(os.path.join(addr,listsong[index]))
                
            elif "exit" in data1:
                speechttx("Thank you Nishanth hope I will talk to you soon")
                break
            #time delay in seconds
            
            elif "send mail" in data1:
                sender="nishanthmungara29@gmail.com"
                receivers=["mungaravrao@rediffmail.com"]
                message=MIMEMultipart()
                message['From']=sender
                message['To']=", ".join(receivers)
                message['Subject']="Test email"
                body="this is a test Mail"
                message.attach(MIMEText(body,"plain"))
                
                
                try:
                    smtpobj=smtplib.SMTP('localhost')
                    smtpobj.sendmail(sender,receivers,message.as_string)
                    print("sent mail succesfully")
                    speechttx("sent mail succesfully")
                except Exception as e:
                    print ("Error: unable to send email")
                    print(e)
                
            time.sleep(6)
    