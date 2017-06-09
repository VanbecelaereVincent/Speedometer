import time
import RPi.GPIO as GPIO
import LCD

hall_sensor = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(hall_sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)

diameter = 45
afstand = 0
gedetecteerd = 0

starttijd = time.time()



def magneet_gedetecteerd(getal):

        global afstand, gedetecteerd

        afstand += diameter

def get_afstand():


GPIO.add_event_detect(hall_sensor, GPIO.FALLING, callback=magneet_gedetecteerd, bouncetime=500)


while True:
    distance = get_afstand()
    LCD.write(distance)
















