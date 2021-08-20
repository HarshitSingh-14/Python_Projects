import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


def takeCommand():  #take input from mic to text(string))

    r = sr.Recognizer()
    with sr.Microphone() as Source:
        #print("Yes ...Listening....")
        r.pause_threshold = 1  # to increase time....
        audio = r.listen(Source)

    try: 
        #print("Recognising.....")
        query= r.recognize_google(audio,language='en-in')
        #print(f"User said  ::   {query}\n")
    except Exception as e:
        #print(e)
        print("\nWe were not able to play simultaneously , so pls try again")
        exit()
    return query
engine = pyttsx3.init('sapi5')   #  to take voice..

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def game(comp, you):
    if comp == you:
        return None 
    elif comp =='st':
        if you =='sc':
            return False
        elif you =='p':
            return True

    elif comp =='sc':
        if you =='p':
            return False 
        elif you =='st':
            return True
    
    elif comp =='p':
        if you =='st':
            return False 
        elif you =='sc':
            return True


def hack(query):
    if 'stone' in query:
        randomNo = 2
    elif 'st' in query:
        randomNo = 2
    elif 'tone' in query:
        randomNo = 2
    elif 'bone' in query:
        randomNo = 2
    elif 'clone' in query:
        randomNo = 2
    elif 'rock' in query:
        randomNo = 2
    elif 'phone' in query:
        randomNo = 2
    elif 'roke' in query:
        randomNo = 2
    elif 'pathar' in query:
        randomNo = 2


    elif 'paper' in query:
        randomNo = 3
    elif 'hater' in query:
        randomNo = 3
    elif 'pay' in query:
        randomNo = 3
    elif 'p' in query:
        randomNo = 3
    elif 'panna' in query:
        randomNo = 3


    elif 'scissor' in query:
        randomNo= 1
    elif 'pizza' in query:
        randomNo= 1
    elif 'figure' in query:
        randomNo= 1
    elif 'kanji' in query:
        randomNo= 1
    elif 'sc' in query:
        randomNo= 1
    elif 'thank you' in query:
        randomNo= 1
    elif 'canchi' in query:
        randomNo= 1
    elif 'tenchi' in query:
        randomNo= 1
    elif 'can' in query:
        randomNo= 1

    return randomNo



print("Computer's TURN  -> Stone   (st) , Paper   (p), Scisser   (sc)   -->   DONE")
print("Player's TURN  -> Stone   (st) , Paper   (p), Scisser   (sc)   -->   ")
query=takeCommand().lower()
you=input("??    ")

randomNo=hack(query)

#randomNo=random.randint(1,3)


if randomNo==1:
    comp='st'
elif randomNo==2:
    comp='p'
elif randomNo==3:
    comp='sc'

# print(randomNo)
a= game(comp, you)

print(f"Computer Chose {comp}")  #using f we can use inside " "
print(f"You chose {you}\n")

if a == None:
    print("The game is a draw")
    speak("It's a draw")
elif a==1:
    print("You WIN !!")
    speak("you win")
else: 
    print("You LOSE !!")
    speak("you lose")
