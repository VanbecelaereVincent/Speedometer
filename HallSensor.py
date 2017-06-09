import time
import RPi.GPIO as GPIO
import LCD

hall_sensor = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(hall_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)

diameter = 45
afstand = 0



def magneet_gedetecteerd(getal):

        global afstand
        afstand += diameter


def get_afstand():
    return afstand

GPIO.add_event_detect(hall_sensor, GPIO.FALLING, callback=magneet_gedetecteerd, bouncetime=500)



















