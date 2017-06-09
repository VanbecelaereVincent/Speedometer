import smbus #dit is een library om met de i2c bus te communiceren
import time
#op de pi instaleren: i2c-tools, python-smbus en zeker ook de i2c enablen in de raspi-config

I2C_ADDR  = 0x27 #i2cdetect -y 1
LCD_WIDTH = 20 #breedte van mijn scherm

LCD_CHR = 1 #om data door te sturen
LCD_CMD = 0 #om een command door te sturen

LCD_LINE1 = 0x80 #adres van mijn eerste lijn
LCD_LINE2 = 0xC0 #adres van mijn tweede lijn
LCD_LINE3 = 0x94 #adres van mijn derde lijn
LCD_LINE4 = 0xD4 #adres van mijn vierde lijn

LCD_BACKLIGHT = 0x08 # uit = 0x00

ENABLE = 0b00000100 #enable bit


#tijdsconstanten
E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus.SMBus(1) #de smbus van mijn pi 'openen'

def lcd_init():

    lcd_byte(0x33, LCD_CMD)  # 110011 Initialise
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialise
    lcd_byte(0x06, LCD_CMD)  # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # 000001 Clear display
    time.sleep(E_DELAY)


def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)


def lcd_toggle_enable(bits):
    # Toggle enable
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)


def lcd_string(message, line):

    message = message.ljust(LCD_WIDTH, " ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


def write(distance):

    lcd_init()

    while True:


        lcd_string('{0}'.format(distance), LCD_LINE1)
        lcd_string('een', LCD_LINE2)
        lcd_string("een", LCD_LINE3)
        lcd_string("test.", LCD_LINE4)

        lcd_byte(0x01, LCD_CMD)

        time.sleep(0.5)


#if __name__ == '__main__':

#    try:
#        write()
 #   except KeyboardInterrupt:
  #      pass
  #  finally:
   #     lcd_byte(0x01, LCD_CMD)





