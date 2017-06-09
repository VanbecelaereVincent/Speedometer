import time
import RPi.GPIO as GPIO
import LCD
import HallSensor

knop_aan_uit = 21

vorigestatus = 0
wissel = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(knop_aan_uit, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while True:

    status = GPIO.input(knop_aan_uit)

    afstand = HallSensor.get_afstand()

    if (status == 1 and vorigestatus == 0):
        if wissel == 1:
            wissel = 0
        else:
            wissel = 1
    if wissel == 0:

        while True:

           afstand = HallSensor.get_afstand()
           LCD.lcd_byte(0x01, LCD.LCD_CMD)
           LCD.lcd_byte(0x08, LCD.LCD_CMD)
           LCD.write(afstand)
           break

    if wissel == 1:

        LCD.lcd_byte(0x01, LCD.LCD_CMD)
        LCD.lcd_byte(0x08, LCD.LCD_CMD)
        LCD.write('test')

    vorigestatus = status





