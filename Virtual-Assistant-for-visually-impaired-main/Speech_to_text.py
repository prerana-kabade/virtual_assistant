

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from gtts import gTTS
from back import *
from playsound import playsound
import speech_recognition as sr
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
            with open('ans.txt','a') as f:
                f.write('\n')
                f.write(''.join(said))
                file.close() 
        except Exception as e:
            texttospeech("Please say again")
    return said

def read_file(file):
    flag = True
    while flag:
        try:
            speech= gTTS(text=str(file), lang='en', slow=False)
            filename="voice.mp3"
            speech.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return    

mainwindow= Tk()
mainwindow.title('Virtual Assistant for visually impaired')
mainwindow.geometry('300x200')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='#97FFFF')
Label(mainwindow, text='SMART BLIND ASSISTANT',
     font=('Times New Roman', 16), bg='#FFFFE0', wrap=True, wraplength=450).place(x=25, y=0)

def Query():
    file=open("Guide.txt","r").read().replace("\n"," ")
    read_file(file)
    say=speechtotext()
    if "yes" in say:
        texttospeech("All the best")
        texttospeech("Your examination begins")
        texttospeech("1)Define cybersecurity.")
        say = speechtotext()
        if "next question" in say:
            texttospeech("2)What is big data analytics?")
            say = speechtotext()
            if "next question" in say:
                texttospeech("3)Explain iot architecture.")
                say = speechtotext()
                if "next question" in say:
                    texttospeech("4)Describe Hadoop framework.")
                    say=speechtotext()
                    if "next question" in say:
                        texttospeech("5)what are the different types of analytics tool?")
                        say=speechtotext()
                        if "next question" in say:
                            texttospeech("Your examination ended successfully")
                            texttospeech("Thank you")

    

def Login():
    loginwindow = Toplevel(mainwindow)
    loginwindow.title('Virtual Assistant for visually impaired')
    loginwindow.geometry("400x300")
    loginwindow.configure(bg='#FFB6C1')
    texttospeech("Welcome Student")
    texttospeech("To login say hello")
    say=speechtotext()
    if "hello" in say:
        texttospeech("Please sign in!")

    Label(loginwindow, text='SIGN IN', font=("Times New Roman", 15), bg='#D3D3D3').place(x=50)
    Label(loginwindow, text="Username").place(x=100,y=30)
    Label(loginwindow, text="Password ").place(x=100,y=50)
    e1=Entry(loginwindow)
    e1.place(x=200,y=30)
    e2=Entry(loginwindow)
    e2.place(x=200,y=50)
    submitbutton=Button(loginwindow,text='Submit',font=('Times New Roman', 16), bg='#C1FFC1', command=lambda:login(e1.get(),e2.get()))
    submitbutton.place(x=100,y=100)
    exambutton=Button(loginwindow,text='Exam',font=('Times New Roman', 16), bg='#C1FFC1', command=Query)
    exambutton.place(x=200,y=200)

    
    
loginbutton = Button(mainwindow, text='LOGIN', font=('Times New Roman', 16), bg='#FFC0CB',command=Login)
loginbutton.place(x=100, y=150)




mainwindow.update()
mainwindow.mainloop()



