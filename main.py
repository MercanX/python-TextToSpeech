import playsound
import  speech_recognition as sr
from gtts import gTTS
import random
import os

def toSound(text,lang="en"):
    
    tts = gTTS(text = text, lang= lang)
    fileName = "afm-"+ str(random.randint(0,100)) + "-"+lang+".mp3"
    tts.save(fileName)
    #playsound.playsound(fileName)
    #os.remove(fileName)

r = sr.Recognizer()

with open("text.txt", "r",encoding="utf-8") as file:
   text = file.read()   

toSound(text,"en")
