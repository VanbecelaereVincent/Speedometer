import time
import RPi.GPIO as GPIO



knop_aan_uit = 21

wissel = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(knop_aan_uit, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def knop_gedrukt(nmbr):

    global wissel
    wissel += 1



GPIO.add_event_detect(knop_aan_uit, GPIO.FALLING, callback=knop_gedrukt, bouncetime=1000)

