from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os
import sys


text=""

def texttospeech(text):
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            filename="speak.mp3"
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said




def login(addr,pwd):
    if len(addr)==0 and len(pwd)==0:
         text1 = "Please sign in! "
         texttospeech(text1)
        
    elif len(addr)==0:
         texttospeech("Enter your Username")
         
         
    elif len(pwd)==0:
          texttospeech("Enter your password")
         
          
    else:
          texttospeech("Congratulations, you successfully signed in!")
          uname=addr
          pswd=pwd
          texttospeech("Your username"+uname+"Your password"+pswd+"Is this correct")
          say=speechtotext()
          if "yes" in say:
             with open('ans.txt','w') as f:
                  print(uname,file=f)
                  print(pswd,file=f)
             texttospeech("You can click exam button now!")
          if "no" in say:
              texttospeech("Please enter correctly")
          

               
   
          

       

                 

