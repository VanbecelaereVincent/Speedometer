import time
import RPi.GPIO as GPIO
hall_sensor = 20
import dbconn

GPIO.setmode(GPIO.BCM)
GPIO.setup(hall_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)


startijd = time.time()
eindtijd = 0
verstreken = 0
totale_afstand = 0


snelheid = 0

parameter = 0

def ophalen_diameter():

        try:

                db = dbconn.DbConnection()

                sql1 = ('SELECT DiameterWiel from Gebruiker ORDER BY ID DESC LIMIT 1')

                diameter_lijst = db.query(sql1)
                diameter = diameter_lijst[0][0]

        except:
                diameter = 0

        print(diameter)
        return diameter

diameter = ophalen_diameter()

diameter_km = diameter / 100000.0


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

def reset():

        global totale_afstand
        global snelheid

        totale_afstand = 0
        snelheid = 0


GPIO.add_event_detect(hall_sensor, GPIO.FALLING, callback=magneet_gedetecteerd, bouncetime=20)

























