#HEALTHY PROGRAMMER

"""

WATER-water.mp3 (3.5 litres) 250ml for 14 times - 9 to 5 -EVERY 34 MINUTES - DRANK -
EYES-eyes.mp3 - EVERY 30 MINUTES - EY DONE
Physical Activity-physical.mp3 - EVERY 45 MINUTES - EX DONE

PYGAME MODULE TO PLAY AUDIO

"""

import datetime

import pygame

import time

"""
def sum():
    x=int(input("ENTER VALUE X "))
    y=int(input("ENTER VALUE Y "))
    z=x+y
    print("sum= ",z)


#Main part()
sum()
play_audio()
time.sleep(5)
print("GOOD BYE EVERYONE ")

900
945
1030
1115
1200
1245
130
215
300
345
430
"""

import HealthyProgrammerEyes
import HealthyProgrammerWater
import HealthyProgrammerExercise

def dateTime():
    return datetime.datetime.now()


def getHour():
    return datetime.datetime.now().hour

def getMinute():
    return datetime.datetime.now().minute

print(getHour(),getMinute())

k=int(240)
x=int(660)
if getHour()==9 and getMinute()==0:
    time.sleep(900)
while(getHour() >=9 and getHour()<=17):
    #if (getHour() == 9 and getMinute()==00) or (getHour()==9 and getMinute()==45) or (getHour()==10 and getMinute()==30) or (getHour() == 11 and getMinute() == 15) or (getHour() == 12 and getMinute() == 00) or (getHour() == 12 and getMinute() == 45) or (getHour() == 13 and getMinute() == 30) or (getHour() == 14 and getMinute() == 15) or (getHour() == 15 and getMinute() == 00) or (getHour() == 15 and getMinute() == 45) or (getHour() == 16 and getMinute() == 30) :
    time.sleep(900)
    HealthyProgrammerEyes.Eyes()
    time.sleep(k)
    HealthyProgrammerWater.Water()
    k+=240
    time.sleep(x)
    x+=60
    HealthyProgrammerExercise.Exercise()