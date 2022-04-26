#!/usr/bin/env python
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/usbttl', 115200, timeout=1)
    ser.flush()
    while True:
        inpuut = raw_input("Ketik a untuk menghidupkan, ketik b untuk mematikan neon:")
	print("input: " + str(inpuut))
	if inpuut == "a":
            try:
	        ser.write("Neon=on\n".encode('utf-8'))
	    except e as Exception:
		print(e)
	    else:
	        print("Okee")
        if inpuut == "b":
 	    ser.write("Neon=off\n".encode('utf-8'))
	time.sleep(2)
