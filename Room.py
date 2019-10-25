import os
import json
import Exit

class Room:
	def __init__(self, id):
		prefix = "RM_"

		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name == (prefix + id):
				file = open(name, "r")
				break

		if file.mode is 'r':
			data = json.load(file)

		file.close()

		self.id = data['id']
		self.long_description = data['long_description']
		self.short_description = data['short_description']
		

		self.exits = dict()				

		print(data["exits"])

		for dir in data["exits"]:
			if data["exits"][dir] is not None:
				self.exits[dir] = Exit.Exit(data["exits"][dir])
			else:
				self.exits[dir] = None

		self.actions = {}

		self.status = {"visited" : False,
                     "objects" : []
                    }