from os import listdir
from datetime import datetime as dt

def log():
	# TODO: Add functionality to keep track of ALL logged files in a central place
	prompt = '>'
	filename = '_log_notes'
	date_time_now = dt.now()
	message = input(prompt)
	files = [file for file in listdir()]
	
	try:
		day = date_time_now.day
		month = date_time_now.month
		hour = date_time_now.hour
		minute = date_time_now.minute

		# Ensure there are always 2 digits in these sections
		if day < 10:
			day = '0' + str(day)
		if month < 10:
			month = '0' + str(month)
		if hour < 10:
			hour = '0' + str(hour)
		if minute < 10:
			minute = '0' + str(minute)

		date = "{}-{}-{} ".format(date_time_now.year, month, day)
		time = "{}{}hrs".format(hour, minute)

		text_file = open("{}.txt".format(filename), 'a')
		text_file.write(date + time + ' : ' + message + '\n')
		text_file.close()
		print("Done")
		return
	except Exception as e:
		print('failed writing file:', e)	
		return


log()

