####
#	Author: Xavid Ramirez
#	Email:	xavidram@hotmail.com
#	Alt Email: xavid.ramirez01@utrgv.edu
#	Script Summary:	This script will sample values
#					from a vibration sensors at a 
#					desired sampling fequency.
#	License:		MIT  =>   https://tldrlegal.com/license/mit-license
####
from adxl345 import ADXL345
import os
import platform
import time

#initialize adxl
adxl345 = ADXL345()

#Global Variables
Frequency = 0
TimeCount = 0
Runtime = 0

# Function definitions:
def cleanUp():
	"""
		Function:	cleanUp
		Params:		NONE
		Libraries:	os
		Desc:		Detect which system is running the
					script and run the os's clear command
					to clear the screan.
	"""
	if 'Windows' in platform.system():
		os.system('cls')
	elif 'Linux' in platform.system():
		os.system('clear')
	elif 'OSX' in platform.system():
		os.system('clear')

def Calibrate1():
	Timestart = time.time()
	Duration = int(Runtime)
	print "Time \t X-axis \t Y-axis \t Z-axis"
	Timestamps = []
	AxesList = []
	while (time.time() - Timestart) < Duration:
		Timestamps.append(time.time() - Timestart)
		AxesList.append(adxl345.getAxes(True))
		time.sleep(Frequency)

	#write out the data
	with open(FileName,'a') as textfile:
		j = 0
		textfile.write("Timestamp \t X-Axis \t Y-Axis \t Z-Axis\n")
		while j < len(Timestamps):
			print "%.4f \t %.3f \t %.3f \t %.3f" % ((Timestamps[j]) , AxesList[j]['x'] , AxesList[j]['y'], AxesList[j]['z'])
			textfile.write(str(Timestamps[j]) + '\t' + str(AxesList[j]['x']) + '\t' + str(AxesList[j]['y']) + '\t' + str(AxesList[j]['z']) + '\n')
			j += 1

def updateFileName():
	if fileindex < 10:
		FileName = 'Trial_0%d_%ds_%.4fhz.txt' % (fileindex,Runtime,Frequency)
	elif fileindex >= 10:
		FileName = 'Trial_%d_%ds_%.4fhz.txt' % (fileindex,Runtime,Frequency)

cleanUp()
print " ---Vibration Sensor Collection---\n "
H = raw_input("What frequency would you like to capture values at? (hz):  ")
Runtime = raw_input("how long would you like each trials to last?(seconds) : ")
Frequency = 1 / float(H)	#get the sampling frequency by dividing the value one by the given Frequency (H)
print "Sampling rate set to: %s" % (Frequency)
print "REMEMBER: In order to stop script, use key combinations ctrl + c or script will run until stopped!"
print "Please double check that your sensor is connected on the proper channels: |  Analog VS, Analog Ground, AIN0  | \n"
print "Starting.....\n"
time.sleep(2)
cleanUp()
fileindex = 1

while True:
	Calibrate1()
	fileindex += 1