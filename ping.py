from pythonping import ping     #module for send and receive ping  /for install module: pip install pythonping
import datetime
from time import sleep
import sys

data = datetime.datetime.now() 

ip_server= '192.168.0.0' #enter ip
ping( ip_server, verbose=True)
for i in range(0, 9000):
    data = datetime.datetime.now() #refresh variable
    if (data.minute==00) or (data.minute == 15) or (data.minute==30) or (data.minute==45):
        print("start")
        for i in range(0,5000):
            data = datetime.datetime.now()
            ping(ip_server, verbose=True)
            print(data.minute)
            if data.day == 12 : #date the code no longer runs 
                if data.minute == 00: #minute the code no longer runs
                    sys.exit()
            sleep(900)  #15 mins
    else:
        sleep(60)