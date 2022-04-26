import serial
import time

leonardo = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
    try:
	data = leonardo.readline()
	if data:
	    print(data)
	    print('HI LEONARDO')
    except:
	leonardo.close()
