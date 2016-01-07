#!/usr/bin/env python
import os


temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
temp = int(str(temp.read()).rsplit('\n')[0])/1000.0
print(temp)
