# Connect the sensor hub (arduino nano) through serial
# By Bowen & Tao
# 05/24/2016
############################################################

import math
import time
import serial
import serial.tools.list_ports

def WIN_SERIAL_CONNECT():
	PortsList = list(serial.tools.list_ports.comports())	# list all the ports connected
	PortsNum = len(PortsList)	# count all the ports connected
	for i in range(PortsNum):
		PortsList[i] = str(PortsList[i])
		if "Arduino" in PortsList[i]:
			print ("COM Sequence:",i,"Device Info:",PortsList[i])
			COMtoConnect = i
			break
		else:
			print ("No Arduino Detected")
	print("Trying to connect to", PortsList[COMtoConnect][:4])
	return PortsList[COMtoConnect][:4]
	

def UBUNTU_SERIAL_CONNECT():
	PortsList = list(serial.tools.list_ports.comports())
	PortsNum = len(PortsList)
	for i in range(PortsNum):
		print("COM Sequence:",i,"Device Info:",PortsList[i])
	COMtoConnect = input("Choose the right COM sequence for RMR control (Arduino)...")
	COMtoConnect = int(COMtoConnect)
	print("Trying to connect to", PortsList[COMtoConnect][0])
	return PortsList[COMtoConnect][0]

def PI_SERIAL_CONNECT():
	# Scan the com port list, than automatically choosing the arduino port to connect. Return the port name.
	a=0


if __name__=='__main__':
	# # Unquote this part for windows
	# RMRport = WIN_SERIAL_CONNECT()
	# Unquote this part for Ubuntu
	RMRport = UBUNTU_SERIAL_CONNECT()
	# # Unquote this part for RaspBerry Pi with Raspbian
	# RMRport = PI_SERIAL_CONNECT()
	ControlRMRport = serial.Serial(RMRport, 115200)
	print("RMR Sub-Controller Connected")


