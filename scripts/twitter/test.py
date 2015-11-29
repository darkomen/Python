import os
ip = os.popen(" uptime |awk '{print$1}'")
print ip.readline()