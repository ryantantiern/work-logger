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
		date = "{}-{}-{} ".format(date_time_now.year, date_time_now.month, date_time_now.day)
		time = "{}{}hrs ".format(date_time_now.hour, date_time_now.minute)
		if date_time_now.hour < 10:
			time = '0' + time
		text_file = open("{}.txt".format(filename), 'a')
		text_file.write(date + time + ': ' + message + '\n')
		text_file.close()
		print("Done")
		return
	except Exception as e:
		print('failed writing file', e)	
		return


log()

