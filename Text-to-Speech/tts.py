#import necessary libraries
from gtts import gTTS
import os

#text.txt file should have the text which is to be converted to speech/audio
f=open('text.txt')
x=f.read()

#set language=english
language='en'
audio=gTTS(text=x,lang=language,slow=False)

#The audio file is saved in the same directory
audio.save('audio.wav')
os.system('audio.wav')
