import time
rtc = time.clock_gettime(time.CLOCK_REALTIME)
print("System RTC={}".format(rtc))
