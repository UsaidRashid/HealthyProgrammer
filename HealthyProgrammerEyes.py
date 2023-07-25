import time
import pygame
import datetime

def dateTime():
    return datetime.datetime.now()


def getHour():
    import datetime
    return datetime.datetime.now().hour


def playEyes():
    pygame.init()
    file="Close Your Eyes.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def Eyes():
    if (getHour() >= 9 or getHour() <= 17):
        time.sleep(2)
        playEyes()
        time.sleep(5)
        f = open("EyesExercise.txt", "a+")
        f.write(str(dateTime()))
        f.write(" DID EYES EXERCISE \n")
        f.close()

