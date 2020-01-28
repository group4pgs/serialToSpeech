import serial
import pyttsx3
import time

#Instal packages - serial, pyttsx3



def sayIt(p):
	print("-----------Starting to speak------------")	
	engine=pyttsx3.init()
	engine.say(p)
	engine.runAndWait()	

def serialObtain():
	ser = serial.Serial('/dev/ttyACM0', 9600) #port of ARDUINO and also baud rate
	while True :
		try:
			state=serial.readline()
			return state
		except:
        	pass

def readSerial():
	time.sleep(1)
	sayIt(serialObtain)
	
