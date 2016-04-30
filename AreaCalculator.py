# This is the code for a calculator which can tell the area of the following shapes, circle and triangle.

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print 'The calculator has been ready to start!'
current_time = 'current_time: %s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)
print current_time

sleep(1)

hint = "Don/'t forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle:").upper()

def user_choice(option):
	if option == "C":
		radius = float(raw_input("Enter a radius:"))
		area = pi * (radius ** 2)
		print "The pie is baking..."
		sleep(1)
		return "Area: %.2f. \n%s" % (area, hint)

	elif option == "T": 
		base = float(raw_input("Enter a base:"))
		height = float(raw_input("Enter a height:"))
		area = 0.5 * (base * height)
		print "Uni Bi Tri..."
		sleep(1)
		return "Area: %.2f. \n%s" % (area, hint)
  
	else:
		print "Error! Invalid shape selector specified. Exiting."	 
    
print user_choice(option)