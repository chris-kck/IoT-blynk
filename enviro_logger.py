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
import subprocess
from time import time

BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)

ALLOWED_COMMANDS_LIST = ['ls', 'lsusb', 'ip a', 'ip abc']

@blynk.handle_event('write V6')
def write_handler(pin, values):
    for i in range(50):
        blynk.virtual_write(pin,i)

    header = ''
    result = ''
    delimiter = '{}\n'.format('=' * 30)
    if values and values[0] in ALLOWED_COMMANDS_LIST:
        cmd_params = values[0].split(' ')
        try:
            result = subprocess.check_output(cmd_params).decode('utf-8')
            header = '[output]\n'
        except subprocess.CalledProcessError as exe_err:
            header = '[error]\n'
            result = 'Return Code: {}\n'.format(exe_err.returncode)
        except Exception as g_err:
            print("Command caused '{}'".format(g_err))
    elif values and values[0] == 'help':
        header = '[help -> allowed commands]\n'
        result = '{}\n'.format('\n'.join(ALLOWED_COMMANDS_LIST))

    # communicate with terminal if help or some allowed command
    if result:
        output = '{}{}{}{}'.format(header, delimiter, result, delimiter)
        print(output)
        blynk.virtual_write(pin, output)
        blynk.virtual_write(pin, '\n')






















# Define values.

btns = {'sstop_btn':3,'dismiss_btn':5, 'reset_time_btn':6, 'interval_btn':8} #dict of output pins

def init_GPIO():
    
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering  
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
        
