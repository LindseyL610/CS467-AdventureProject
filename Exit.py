import os
import json

class Exit:
	def __init__(self, id):
		prefix = "EX_"

		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name == (prefix + str(id)):
				file = open(name, "r")
				break

		if file.mode is 'r':
			data = json.load(file)

		file.close()

		self.id = data['id']
		self.rooms = data['rooms']