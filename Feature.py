import os
import json

class Feature:
	def __init__(self, id):
		self.id = id

		prefix = "FE_"

		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name == (prefix + str(id)):
				file = open(name, "r")
				break

		if file.mode is 'r':
			data = json.load(file)

		file.close()

		self.id = data['id']
		self.state = data['state']
		
		self.actions = dict()

		for act in data["actions"]:
			if data["actions"][act] is not None:
				self.actions[act] = data["actions"][act]
			else:
				self.actions[act] = None

		self.items = dict()
		for itm in data["items"]:
			if data["items"][itm] is not None:
				self.items[itm] = data["items"][itm]
			else:
				self.items[itm] = None

		self.display = dict()

		for disp in data["display"]:
			if data["display"][disp] is not None:
				self.display[disp] = data["display"][disp]
			else:
				self.display[disp] = None

		#load default data

	def perform_action(self, game, act):
		self.state = self.actions[act]
		
		if self.state in self.display:
			print(self.display[self.state])

		if self.state in self.items:
			game.rooms[game.current_room].add_dropped_item(self.items[self.state])

	def unlock_door():
		print("You unlocked the door.")
