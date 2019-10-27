import os
import json

class Feature:
	def __init__(self, id):
		prefix = "FE_"

		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name == (prefix + str(id)):
				file = open(name, "r")
				break

		if file.mode is 'r':
			data = json.load(file)

		file.close()

		#load default data