import os
import json
import Exit
import Feature

class Room:
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()

	def get_prompt(self, game):
		if not self.state['visited']:
			prompt = self.data["long_description"]
			self.state['visited'] = True
		else:
			prompt = self.data["short_description"]

		for itm in self.state["items"]:
			obj = game.objects[itm]

			if obj.data["can_be_taken"] == True:
				if obj.state["current_state"] in obj.data["message"]:
					prompt += ("\n" + obj.data["message"][obj.state["current_state"]])
				else:
					prompt += ("\n" + obj.data["message"]["default"])

		return prompt

	def check_item(self, item):
		for itm in self.state["items"]:
			if itm == item:	
				return True

		return False

	def remove_item(self, item):
		if item in self.state["items"]:
			self.state["items"].remove(item)

	def add_dropped_item(self, item):
		self.state["items"].append(item)

	def get_state_data(self):
		return self.state
