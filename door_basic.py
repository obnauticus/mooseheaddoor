import time
import serial

phone = serial.Serial("/dev/ttyACM0",  115200, timeout=5)

phone.write(b'AT H0\r')
while 1:
	line = phone.readline()
	print line	
	if "RING" in line:
		phone.flush()
		phone.write(b'AT H1\r')
        	print "I am off the hook bitch"
		time.sleep(3)
		phone.flush()
        	phone.write(b'AT D9\r')
		print "I dialed 9 bitch"
		time.sleep(1)
		phone.flush()
		phone.write(b'AT H0\r')
		print "I hung up the phone bitch"

	phone.flush()
