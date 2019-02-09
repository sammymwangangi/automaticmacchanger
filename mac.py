#!/usr/bin/python

import os
import time

print """

***************************************************************************
                    AUTOMATIC MAC ADDRESS CHANGER
                            CREATED BY:
                        SAMMY MWANGANGI
****************************************************************************

"""
time.sleep(3)

while True:
    os.system("service network-manager stop")
    os.system("ifconfig wlan0 down")
    print(os.popen("macchanger wlan0 -r").read())
    os.system("ifconfig wlan0 up")
    os.system("service network-manager start")
    time.sleep(300)
