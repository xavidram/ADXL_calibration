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


cleanUp()
axes = adxl345.getAxes(True)
print "ADXL345 on address 0x%x:" % (adxl345.address)
print "   x = %.3fG" % ( axes['x'] )
print "   y = %.3fG" % ( axes['y'] )
print "   z = %.3fG" % ( axes['z'] )

