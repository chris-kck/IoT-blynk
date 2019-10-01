"""
Blessing Ngorima NGRBLE001 
	&
Chris Kateera KTRKUD001

EEE3096S Environment Logger Blynk Project
Date: 30 September 2019
An environment Logger using the Blynk applicaton.
"""


# import Relevant Librares
from time import time
import blynklib

BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)
# Define values.

def init_GPIO():
    b=3
    print("hi")
    while 1:
        blynk.run()

# ADC - Temperature, Potentiometer (Humidity), Light Sensor

# Buttons: interrupts, debouncing
#Start/Stop, Dismiss Alarm, Reset SYStime , Change reading interval


#Alarm Output - buzzer

#RTC- via kernel drivers.


# Main function
def main():
    a=4
    init_GPIO()
    
# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
