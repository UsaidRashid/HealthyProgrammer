import time
import pygame
import datetime

def dateTime():
    return datetime.datetime.now()


def getHour():
    import datetime
    return datetime.datetime.now().hour



def playDrink():
    pygame.init()
    file="Drink Water It Will You - English Dialogue.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def Water():
    if (getHour() >= 9 or getHour() <= 17):
        time.sleep(2)
        playDrink()
        time.sleep(5)
        f = open("WaterReminder.txt", "a+")
        f.write(str(dateTime()))
        f.write(" DRANK WATER \n")
        f.close()
