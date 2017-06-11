import time
import datetime
import RPi.GPIO as GPIO
import LCD
import HallSensor

knop_aan_uit = 21

vorigestatus = 0
wissel = 0
parameter = 0

tijden_sessie = []
startijd = 0
#tijden_sessie.append(HallSensor.begin_sessie)

GPIO.setmode(GPIO.BCM)
GPIO.setup(knop_aan_uit, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while True:

    status = GPIO.input(knop_aan_uit)


    if (status == 1 and vorigestatus == 0):

        if wissel == 1:
            wissel = 0
        else:
            wissel = 1

    if wissel == 0:

        startijd = datetime.datetime
        tijden_sessie.append(startijd)

        parameter += 0.00000000000000000000001

        while True:

            speed = HallSensor.snelheid
            totale_afstand = HallSensor.totale_afstand
            LCD.write('----SPEEDMETER----',speed,totale_afstand,time.ctime(int(time.time())))
            time.sleep(1)
            #LCD.lcd_byte(0x01, 0)

            break



    if wissel == 1:

        if (parameter > 0):

            einde_sessie = datetime.datetime
            tijden_sessie.append(einde_sessie)
            LCD.write('Einde sessssssssie', '', '', '')
            parameter = 0
            time.sleep(2)



        if(parameter == 0):
            LCD.write('Begin een sesie',"","","")







    vorigestatus = status







