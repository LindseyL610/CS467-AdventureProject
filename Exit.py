import os
import json

class Exit:
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()

	def perform_action(self, game, act):
		if act == "unlock":
			if "key" not in game.state["bag"]:
				print("The door needs a key to be unlocked.")
				return

			if act in self.data["display"]:
				print(self.data["display"][act])

			self.state["locked"] = False
		elif act == "open":
			if self.state["locked"] == True and\
			"key" not in game.state["bag"]:
				print("The door is locked.")
				return

			if act in self.data["display"]:
				print(self.data["display"][act])

			if self.state["locked"] == True:
				self.state["locked"] = False

	def get_state_data(self):
		return self.state
