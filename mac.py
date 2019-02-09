#!/usr/bin/python

import os
import time
while True:
    os.system("service network-manager stop")
    os.system("ifconfig eth0 down")
    print(os.popen("macchanger eth0 -r").read())
    os.system("ifconfig eth0 up")
    os.system("service network-manager start")
    time.sleep(300)
