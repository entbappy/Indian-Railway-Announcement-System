"""
Author : Bappy Ahmed
Email : bappymalik4161@gmail.com
Date : 04 sept 2020
"""

import os
import pandas as pd  
from pydub import AudioSegment
from gtts import gTTS    #google text to speech


#It takes a text and consists as an audio clip of the text
def text_to_speech(text,fileName):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text= mytext, lang= language , slow= False)
    myobj.save(fileName)

# This function returns pydub's audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

# It will split railway.mp3
def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    
    # 1. Generate "kripiya dhiyan dejiye"
    start = 88000 #from milisec
    finish = 90200  #to
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3', format = "mp3")

    # 2. is from city

    # 3. Generate "se chalkar"
    start = 91000 
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3', format = "mp3")

    # 4. is via-city

    # 5. Generate "ke rastee"
    start = 94000 
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3', format = "mp3")

    # 6. is to-city

    # 7. Generate "ko jane wali gaari sangkha"
    start = 96000 
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format = "mp3")

    # 8. is train no and name

    # 9. Generate "kuch hei samay main platform sankhya"
    start = 105500 
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3', format = "mp3")

    # 10. is platform number

    # 11. Generate "per aa rahi hai"
    start = 109000 
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3', format = "mp3")


# It generates The announcement
def generateAnnouncement(filename):
    excelRead = pd.read_excel(filename)
    # print(excelRead)
    for index , item in excelRead.iterrows():
        
        # 2- Generate from-city
        text_to_speech(item['from'], '2_hindi.mp3')
        
        # 4- Generate via-city
        text_to_speech(item['via'], '4_hindi.mp3')
        
        # 6- Generate to-city
        text_to_speech(item['to'], '6_hindi.mp3')
        
        # 8- Generate train no and name
        text_to_speech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        
        # 10- Generate platform number
        text_to_speech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        
        announcement = mergeAudios(audios)
        announcement.export(f"announcement{item['train_no']}_{index+1}.mp3", format="mp3")

    


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")






