#!/bin/env python

import time, sys, random, optparse

hour_name = ["Midnight", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Noon",  "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "midnight"]

date_name = ["ZEEROTH","First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", "Nineteenth", "Twentieth", "Twenty-first", "Twenty-second", "Twenty-third", "Twenty-fourth", "Twenty-fifth", "Twenty-sixth", "Twenty-seventh", "Twenty-eighth", "Twenty-ninth", "Thirtieth", "Thirty-first"]

parser = optparse.OptionParser()

parser.set_defaults(date_opt=False, time_opt=False )
parser.add_option("-d", "--date", action="store_true", dest="date_opt")
parser.add_option("-t", "--time", action="store_true", dest="time_opt")

(options, args) = parser.parse_args()

if (options.date_opt == False):
	if (options.time_opt == False):
		options.date_opt = True
		options.time_opt = True

datenum = time.localtime()
if datenum[4] + datenum[5]/60 > 57:
	datenum = time.localtime(time.time() + 150)
date = {"year": datenum[0], "month": datenum[1], "mday": datenum[2], "hour": datenum[3], "min": datenum[4], "sec": datenum[5], "wday": datenum[6], "yday": datenum[7], "isdst": datenum[8]}

random_seed = ""
for x in datenum[0:3]:
	random_seed += str(x)
random.seed(random_seed)

timestring = ""

if (options.date_opt == True):

	timestring += time.strftime("%A, ", datenum)

	timestring += "the " + date_name[date["mday"]] + " of "

	timestring += time.strftime("%B, %Y", datenum)

if (options.date_opt and options.time_opt == True):
	timestring += ", "

if (options.time_opt == True):
	min_after = date["min"] + date["sec"]/60

	if min_after <= 2.5:
		choices = ["About " + hour_name[date["hour"]], "Around " + hour_name[date["hour"]], "Roughly " + hour_name[date["hour"]]]
	elif min_after <= 7.5:
		choices = ["A little after " + hour_name[date["hour"]], "Just past " + hour_name[date["hour"]], "Five after " + hour_name[date["hour"]], "Five past " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["Around " + hour_name[date["hour"]] + " oh five"]
	elif min_after <= 12.5:
		choices = ["Ten after " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["Around " + hour_name[date["hour"]] + " ten"]
	elif min_after <= 17.5:
		choices = ["Quarter past " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["About " + hour_name[date["hour"]] + " fifteen"]
	elif min_after <= 22.5:
		choices = ["About twenty after " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["Roughly " + hour_name[date["hour"]] + " twenty"]
	elif min_after <= 27.5:
		choices = ["Nearly half past " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["About " + hour_name[date["hour"]] + " twenty-five"]
	elif min_after <= 32.5:
		choices = ["Half past " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["Around " + hour_name[date["hour"]] + " thirty"]
	elif min_after <= 37.5:
		choices = ["Just after half past " + hour_name[date["hour"]], "A little after half past " + hour_name[date["hour"]]]
		if not date["hour"] % 12 == 0:
			choices += ["Roughly " + hour_name[date["hour"]] + " thirty-five"]
	elif min_after <= 42.5:
		choices = ["Almost a quarter to " + hour_name[date["hour"] + 1], "Twenty 'til " + hour_name[date["hour"]+1]]
		if not date["hour"] % 12 == 0:
			choices += ["About " + hour_name[date["hour"]] + " forty"]
	elif min_after <= 47.5:
		choices = ["Quarter to " + hour_name[date["hour"] + 1], "Fifteen 'til " + hour_name[date["hour"]+1]]
		if not date["hour"] % 12 == 0:
			choices += ["Around " + hour_name[date["hour"]] + " forty-five"]
	elif min_after <= 52.5:
		choices = ["Ten to " + hour_name[date["hour"] + 1]]
		if not date["hour"] % 12 == 0:
			choices += ["Roughly " + hour_name[date["hour"]] + " fifty"]
	elif min_after <= 57.5:
		choices = ["Just shy of " + hour_name[date["hour"] + 1] , "Almost " + hour_name[date["hour"] + 1]]
		if not date["hour"] % 12 == 0:
			choices += ["About " + hour_name[date["hour"]] + " fifty-five"]
		
	timestring += random.choice(choices)
	
print("%s" % timestring)
