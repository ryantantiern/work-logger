import os

def log():
	prompt = '>'
	filename = '_log_notes.txt'
	message = input(prompt)
	files = [file for file in os.listdir]
	
	if filename in files:
		try:

		except Exception as e:
			print('failed writing file', e)	