import COM_LED
import COM_CONFIG
import RPi.GPIO as GPIO
import time

# AutoRead Project - GPIO LED Test

def main():
    for key,value in COM_CONFIG.LED_def.items():
        COM_LED.GPIO_ON(value)
        print("Item {0} pin {1} is on".format(key,value))


if __name__ == "__main__":
    try:
        COM_LED.setupGPIO(LED_def)
        main()
        input("Press enter to continue")
        GPIO.cleanup()
    except:
        print("Error condition")
        for key, value in LED_def:
            COM_LED.GPIO_OFF(value)
        print("cleaning up GPIO")
        GPIO.cleanup()
        raise
