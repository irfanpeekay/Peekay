import calendar

year = int(input())
if calendar.isleap(year) is True:
	print ("yes")
else:
	print ("no")
