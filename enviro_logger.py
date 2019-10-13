#!/usr/bin/python2.7
"""
NGRBLE001   -	Blessing Ngorima 	
KTRKUD001   -	Chris Kateera 	
EEE3096S Environment Logger Blynk Project A
Date: 30 September 2019
Blynk applicaton
"""



# import Relevant Librares
import xtime, ADC_3008
import RPi.GPIO as GPIO
import blynklib
import subprocess
import time

#Global Variables
ALLOWED_COMMANDS_LIST = ['ls', 'lsusb', 'ip a', 'ip abc']

#blynk Authentication
BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('write V6')
def write_handler(pin, values):
    blynk.virtual_write(pin,"Welcome to the EnviroLogger \n")

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

#btns = {'sstop':31,'dismiss_a':33, 'reset_t':35, 'interval':37, 'buzzer':18} #dict of input  pins
btns = [31,33,35,37]
def init_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BOARD GPIO numbering
    GPIO.setup(btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Wire the button to +3.3V, then enable an internal pulldown. 
    GPIO.setup(18, GPIO.OUT, initial=0) #buzzer output initially off
    
    GPIO.add_event_detect(btns[0], GPIO.BOTH, callback=sstop, bouncetime=200) #count up event detection
    GPIO.add_event_detect(btns[1], GPIO.BOTH, callback=dismiss_a, bouncetime=200) #count down event detection
    GPIO.add_event_detect(btns[2], GPIO.BOTH, callback=reset_t, bouncetime=200) #count up event detection
    GPIO.add_event_detect(btns[3], GPIO.BOTH, callback=interval, bouncetime=200) #count up event detection


# ADC - Temperature, Potentiometer (Humidity), Light Sensor done
# Buttons: interrupts, debouncing done
#Start/Stop, Dismiss Alarm, Reset SYStime , Change reading interval xxxxxxxxxxx
#Alarm Output - buzzer done xxxxxxxxxx
#RTC- via kernel drivers. done

#btn callback to start/stop the system
def sstop(pin):
    if GPIO.input(pin):
        pass

#btn callback to dismiss the alarm
def dismiss_a():
    if GPIO.input(pin):
        pass

#callback rto reset the system time
def reset_t():
    if GPIO.input(pin):
        pass

#callback to change readint interval
def interval():
    if GPIO.input(pin):
        pass


#Main Driver skrrrrrrrrrr function
def main():
    #GPIO.output(12, GPIO.LOW)
    init_GPIO()
    print("Blynk Authenticated, Pins Initialized")
    blynk.virtual_write("V6","Welcome to the EnviroLogger \n")

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
