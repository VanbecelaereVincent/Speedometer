import time
import RPi.GPIO as GPIO
import datetime
hall_sensor = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(hall_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)

diameter = 100 #deze ophalen uit veld website (standaard op nul zetten? want wat gebeurd eerste keer?)
diameter_km = diameter / 100000.0

# deelsessies = []
# deelsessie = []


startijd = time.time()
eindtijd = 0
verstreken = 0
totale_afstand = 0


snelheid = 0

parameter = 0


def magneet_gedetecteerd(getal):

        global totale_afstand, eindtijd, startijd, verstreken, snelheid, parameter

        parameter += 1

        eindtijd = time.time()

        totale_afstand += diameter_km
        totale_afstand = round(totale_afstand,3)
        verstreken = eindtijd - startijd

        kilometer_per_sec = round(diameter_km / verstreken, 10)
        snelheid = kilometer_per_sec * 3600
        snelheid = round(snelheid,2)

        startijd = eindtijd



GPIO.add_event_detect(hall_sensor, GPIO.FALLING, callback=magneet_gedetecteerd, bouncetime=20)

























