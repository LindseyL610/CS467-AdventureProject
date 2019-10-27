import os
import json
import Exit

class Room:
	def __init__(self, id):
		self.prefix = "RM_"
		self.id = id

		data = self.get_room_data()

		self.id = data['id']
		self.long_description = data['long_description']
		self.short_description = data['short_description']

		self.exits = dict()

		#debug(data["exits"])

		for dir in data["exits"]:
			if data["exits"][dir] is not None:
				self.exits[dir] = Exit.Exit(data["exits"][dir])
			else:
				self.exits[dir] = None

		self.default_items = data["default_items"]

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

			if self.default_items is not None:
				self.state["native_items"] = self.default_items.copy()
			else:
				self.state["native_items"] = list()

			self.state["dropped_items"] = list()

		#or use state data passed as arg
		else:
			self.state = state.copy()


	def get_prompt(self):
		if not self.state['visited']:
			prompt = self.long_description
			self.state['visited'] = True
		else:
			prompt = self.short_description

		if len(self.state["dropped_items"]) is not 0:
			for item in self.state["dropped_items"]:
				prompt = prompt + " The " + item + " is where you dropped it."

		return prompt

	def check_item(self, item):
		all_items = self.state["native_items"] + self.state["dropped_items"]

		if item in all_items:
			return True

		else:
			return False

	def remove_item(self, item):
		if item in self.state["native_items"]:
			self.state["native_items"].remove(item)
		elif item in self.state["dropped_items"]:
			self.state["dropped_items"].remove(item)

	def add_dropped_item(self, item):
		self.state["dropped_items"].append(item)
