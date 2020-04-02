import RPi.GPIO as GPIO
import time

# AutoRead Project - GPIO LED Test

# Note these are header pins 16 and 18 - GPIO23 and GPIO24
LED_def = {"led1":16,"led2":18}

#LED["led1"] = 16


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
        setupGPIO(LED_def)
        main()
    except:
        GPIO.cleanup()