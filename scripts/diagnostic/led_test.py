import ../common/LED as AR_LED

import RPi.GPIO as GPIO
import time

# AutoRead Project - GPIO LED Test

# Note these are header pins 16 and 18 - GPIO23 and GPIO24
LED_def = {"led1":16,"led2":18}


def setupGPIO(LED_def):
    GPIO.setmode(GPIO.BOARD)
    for key, value in LED_def.items():
        GPIO.setup(value, GPIO.OUT)
        print("{0} has been set up on PIN {1}".format(key,value))


def GPIO_ON(Channel):
    GPIO.output(Channel, GPIO.HIGH)
    print("Pin {0} is HIGH".format(Channel))


def GPIO_OFF(Channel):
    GPIO.output(Channel, GPIO.LOW)
    print("Pin {0} is LOW".format(Channel))


def main():
    for key,value in LED_def.items():
        GPIO_ON(value)
        print("Item {0} pin {1} is on".format(key,value))


if __name__ == "__main__":
    try:
        AR_LED.checkimport()
        setupGPIO(LED_def)
        main()
        input("Press enter to continue")
        GPIO.cleanup()
    except:
        print("Error condition")
        for key, value in LED_def:
            GPIO_OFF(value)
        print("cleaning up GPIO")
        GPIO.cleanup()
        raise
