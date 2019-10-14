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
import time, datetime

#Global Variables
ADC_readings=ADC_3008.readings()
index=0
start_time = time.time()


#blynk Authentication
BLYNK_AUTH = 'iPK7gVGF1PsbmT0de_TKOmmSUsIkSB50'
blynk = blynklib.Blynk(BLYNK_AUTH)

#V6 is Terminal
@blynk.handle_event('write V6')
def write_handler(pin, values):
    blynk.virtual_write(pin,"Welcome to the EnviroLogger\n")
    blynk.virtual_write(pin,"|Time     |Sys_Time|Humid \t|Temp \t|Light \t|Alarm|\n")
    while 1:
        interval=[1,3,5]
        elapsed_time = round(time.time() - start_time)
        blynk.virtual_write(pin,"|{}|{} \t|{} \t|{} \t|{} \t| \t|\n".format(xtime.RTC_time()[11:20],str(datetime.timedelta(seconds=elapsed_time)),ADC_readings[0], ADC_readings[1], ADC_readings[2]))
        time.sleep(interval[index]) #interval - to be set only once
        blynk.set_property(pin, 'color', '#ACACAC')


#V0 is Start/Stop
@blynk.handle_event('write V0')
def write_virtual_pin_handler(pin, value):
    print("pin{} value{}".format(pin,value))

#V1 is Dismiss Alarm
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print("pin{} value{}".format(pin,value))
    GPIO.output(18,0)
#V2  is Reset sys
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    print("pin{} value{}".format(pin,value))
    global start_time
    start_time=time.time()

#V3 is interval
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    interval(1)
    print("Int pin{} value{}".format(pin,value))

#V4 is Gauge
@blynk.handle_event('read V4')
def read_virtual_pin_handler(pin):
    #Call Analogue read here.
    Vout = (ADC_readings[2]/float(1023))*ADC_readings[0]
    blynk.virtual_write(pin, Vout) #random.randint(0, 255))
    print("Gauge Vout:{}".format(Vout))

    if (Vout<0.65 or Vout>2.65):
        blynk.set_property(pin, 'color', '#FF0000')
        blynk.virtual_write(pin,"Alarm Sounded")
        GPIO.output(18,1)
    else:
        blynk.set_property(pin, 'color', '#00FF00')

# Define values.

#btns = {'sstop':31,'dismiss_a':33, 'reset_t':35, 'interval':37, 'buzzer':18} #dict of input  pins
btns = [31,33,35,37]
def init_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BOARD GPIO numbering
    GPIO.setup(btns, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Wire the button to +3.3V, then enable an internal pulldown. 
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
        print("SS BTN")
        #ss= not ss
        pass

#btn callback to dismiss the alarm
def dismiss_a(pin):
    if GPIO.input(pin):
        print("Dismiss")
        GPIO.output(18,0)
        pass

#callback rto reset the system time
def reset_t(pin):
    if GPIO.input(pin):
        global start_time
        start_time=time.time()
        print("Reset")
        pass

#callback to change readint interval
def interval(pin):
    if GPIO.input(pin):
        global index
        index=(index+1)%3
        print("Interval")
        pass


#Main Driver skrrrrrrrrrr function
def main():
    #GPIO.output(12, GPIO.LOW)
    init_GPIO()
    print("Blynk Authenticated, Pins Initialized")

    #Listening for connections
    while 1:
        blynk.run()
        global ADC_readings
        ADC_readings=ADC_3008.readings()


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
