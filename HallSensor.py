import time
import datetime
import RPi.GPIO as GPIO
import LCD
import Application

hall_sensor = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(hall_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)

diameter = 100 #deze ophalen uit veld website (standaard op nul zetten? want wat gebeurd eerste keer?)
diameter_km = diameter / 100000.0

# huidige = datetime.datetime


deelsessies = []
deelsessie = []


startijd = time.time()
eindtijd = 0
verstreken = 0
totale_afstand = 0
huidige_afstand = 0
snelheid = 0

parameter = 0


def magneet_gedetecteerd(getal):

        global totale_afstand, eindtijd, startijd, verstreken, snelheid, parameter

        parameter += 1

        eindtijd = time.time()

        totale_afstand += diameter_km
        verstreken = eindtijd - startijd

        kilometer_per_sec = round(diameter_km / verstreken, 10)
        snelheid = kilometer_per_sec * 3600

        startijd = eindtijd


# def opslaan_deelsessies():
#
#         global huidige_afstand, start, stop
#
#         if(Application.startijd != 0):
#                 start = time.time()
#                 if(time.time() == start + 60):
#                         stop = time.time()
#                         afstand = totale_afstand - huidige_afstand
#                         deelsessie.append(start)
#                         deelsessie.append(stop)
#                         deelsessie.append(afstand)
#                         deelsessies.append(deelsessie)
#
#
#                 huidige_afstand = totale_afstand


def get_afstand():
        return totale_afstand

GPIO.add_event_detect(hall_sensor, GPIO.FALLING, callback=magneet_gedetecteerd, bouncetime=500)

# opslaan_deelsessies()



















