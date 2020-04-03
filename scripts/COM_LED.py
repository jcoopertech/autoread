#!/usr/bin python3
# AutoRead common
import RPi.GPIO as GPIO
import COM_CONFIG
"""This is a common file for controlling GPIO. Don't try to run this"""

def GPIO_ON(Channel):
    """Turns on the pin."""
    GPIO.output(Channel, GPIO.HIGH)
    print("COM_LED.py: Pin {0} is HIGH".format(Channel))


def GPIO_OFF(Channel):
    """Turns off the channel."""
    GPIO.output(Channel, GPIO.LOW)
    print("COM_LED.py: Pin {0} is LOW".format(Channel))


def setupGPIO(LED_def):
    GPIO.setmode(GPIO.BOARD)
    for key, value in COM_CONFIG.LED_def.items():
        GPIO.setup(value, GPIO.OUT)
        print("COM_LED: {0} has been set up on PIN {1}".format(key,value))
