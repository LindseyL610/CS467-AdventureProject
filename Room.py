import os
import json
import Exit
import Feature

class Room:
	def __init__(self, id):
		self.prefix = "RM_"
		self.id = id

		data = self.get_room_data()

		self.id = data['id']
		self.long_description = data['long_description']
		self.short_description = data['short_description']

		self.exits = dict()
		self.items = list()

		#debug(data["exits"])

		for dir in data["exits"]:
			if data["exits"][dir] is not None:
				self.exits[dir] = Exit.Exit(data["exits"][dir])
			else:
				self.exits[dir] = None

		for item in data["items"]:
			self.items.append(Feature.Feature(item))

	def get_room_data(self):
		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name == (self.prefix + self.id):
				file = open(name, "r")
				break

		if file.mode is 'r':
			data = json.load(file)
		else:
			data = None

		file.close()

		return data

	def set_state(self, state):
		#set default state
		if state is None:
			self.state = dict()

			self.state["visited"] = False

		#or use state data passed as arg
		else:
			self.state = state.copy()


	def get_prompt(self):
		if not self.state['visited']:
			prompt = self.long_description
			self.state['visited'] = True
		else:
			prompt = self.short_description

		return prompt

	def check_item(self, item):
		for itm in self.items:
			if itm.id == item:	
				return True

		return False

	def remove_item(self, item):
		if item in self.items:
			self.items.remove(item)

	def add_dropped_item(self, item):
		self.items.append(Feature.Feature(item))
