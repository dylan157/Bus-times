#!/usr/bin/env python

#This program works out when the next bus will arrive at my local bus stop.

import time
import os
from datetime import datetime
from sys import platform
now = datetime.now()

times = {
    "7": [18, 48],
    "8": [18, 48],
    "9": [18, 48],
    "10": [18, 48],
    "11": [18, 48],
    "12": [18, 48],
    "13": [18, 48],
    "14": [18, 48],
    "15": [18, 48],
    "16": [18, 48],
    "17": [18, 48],
    "18": [18, 48] # I didn't expect the bus times to be this generic. Still leaving as dictionary in case times get changed#

    }

hour = str(now.hour)

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')
while 1 == 1:
        clear()
        print "" 
        now = datetime.now()
        hour = str(now.hour)
        end = 0
        if now.hour == 18:
            if now.minute > 48:
                end = True
        elif now.hour < 7:
            print "busses not available untill 7:18"
            end = True
        elif now.hour >= 19:
            print "No busses available until tomorrow :("
            end = True
        
        print "time = " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        if end == False:
            if now.minute > times[hour][0]:
                if now.minute > times[hour][1]:
                    hour2 = str(now.hour + 1)
                    total = (times[str(hour2)][0]+60) - now.minute # EG 18 - 40
                    print "Next bus arriving in " + str(total) + " minutes #"
                else:
                    total = times[str(now.hour)][1] - now.minute
                    if total < 5:   
                        print "NEXT BUS ARRIVING IN " + str(total) + " MINUTES"
                    else:
                        print "Next bus arriving in " + str(total) + " minutes"
            else:
                    total = times[str(now.hour)][0] - now.minute
                    if total < 5:   
                        print "NEXT BUS ARRIVING IN " + str(total) + " MINUTES"
                    else:
                        print "Next bus arriving in " + str(total) + " minutes"
        time.sleep(1)




            


    
