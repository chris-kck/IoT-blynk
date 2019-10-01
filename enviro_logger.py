#!/usr/bin/python3
"""
NGRBLE001   -	Blessing Ngorima 	
KTRKUD001   -	Chris Kateera 	
EEE3096S Environment Logger Blynk Project A
Date: 30 September 2019
Blynk applicaton
"""



# import Relevant Librares

import RPi.GPIO as GPIO
import blynklib
from time import time

BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)
# Define values.

def init_GPIO():
    b=3
    

# ADC - Temperature, Potentiometer (Humidity), Light Sensor

# Buttons: interrupts, debouncing
#Start/Stop, Dismiss Alarm, Reset SYStime , Change reading interval

#Alarm Output - buzzer

#RTC- via kernel drivers.


# Main function
def main():
    a=4
    print("hi")
    while 1:
        blynk.run()
    
# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
