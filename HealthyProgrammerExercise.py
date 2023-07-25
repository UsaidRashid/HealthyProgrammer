import time
import pygame
import datetime

def dateTime():
    return datetime.datetime.now()


def playExercise():
    pygame.init()
    file="timetoexer_0e195e395297568.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def getHour():
    import datetime
    return datetime.datetime.now().hour

def Exercise():
    if (getHour() >= 9 or getHour() <= 17):
        playExercise()
        time.sleep(5)
        f=open("Exercise.txt","a+")
        f.write(str(dateTime()))
        f.write(" DID EXERCISE \n")
        f.close()

