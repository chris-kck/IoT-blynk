import time

def RTC_time():
    rtc = time.clock_gettime(time.CLOCK_REALTIME)
    #print("System RTC={}".format(rtc))
    rtc_time = time.ctime(rtc)
    return rtc_time
