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

# Define values.
BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)
btns = {sstop_btn:3,dismiss_btn:5, reset_time_btn:6, interval_btn:8} #dict of output pins

def init_GPIO():
    
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
    GPIO.setup(btns, GPIO.IN, initial=0)    # set GPIO btns as inputs
    GPIO.setup(in_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Wire the button to +3.3V, then enable an internal pulldown. 
    # GPIO.setup(x, GPIO.OUT) LED- https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
    # GPIO.setup(x, GPIO.OUT) Buzzer
    b=3
    #GPIO.add_event_detect(11, GPIO.BOTH, callback=count_up, bouncetime=200) #count up event detection
    #GPIO.add_event_detect(13, GPIO.BOTH, callback=count_down, bouncetime=200) #count down event detection
    

# ADC - Temperature, Potentiometer (Humidity), Light Sensor

# Buttons: interrupts, debouncing
#Start/Stop, Dismiss Alarm, Reset SYStime , Change reading interval

#Alarm Output - buzzer

#RTC- via kernel drivers.


# Main function
def main():
    #GPIO.output(12, GPIO.LOW)
    
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
    finally:
         GPIO.cleanup()
        
