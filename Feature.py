import os
import json

class Feature:
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()


	def perform_action(self, game, act):
		self.state["current_state"] = self.data["actions"][act]
		
		if self.state["current_state"] in self.data["display"]:
			print(self.data["display"][self.state["current_state"]])

		if self.state["current_state"] in self.data["items"]:
			game.objects[game.get_current_room()].add_dropped_item(self.data["items"][self.state["current_state"]])

	def unlock_door():
		print("You unlocked the door.")

	def get_state_data(self):
		return self.state