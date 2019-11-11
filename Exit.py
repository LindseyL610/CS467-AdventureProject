import os
import json
import Feature

class Exit(Feature.Feature):
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()

	def perform_action(self, game, act):
		if act == "unlock":
			if "key" not in game.state["bag"]:
				ret_str = "The door needs a key to be unlocked."
				return ret_str

			if act in self.data["display"]:
				ret_str = self.data["display"][act]

			self.state["locked"] = False
			return ret_str

		elif act == "open":
			if self.state["locked"] == True and\
			"key" not in game.state["bag"]:
				ret_str = "The door is locked."
				return ret_str

			if act in self.data["display"]:
				ret_str = self.data["display"][act]

			if self.state["locked"] == True:
				self.state["locked"] = False

			return ret_str

	def unlock(self, game):
		unlock = False

		if self.data["can_be_unlocked"] == False:
			game.say ("The " + self.data["id"] + " does not need to be unlocked.")
		elif self.state["locked"] == False:
			game.say("You already unlocked the " + self.data["id"] + ".")
		elif self.data["id"] == "stone door":
			if "key" not in game.state["bag"]:
				game.say( "The door needs a key to be unlocked.")
			else:
				unlock = True

		if unlock == True:
			self.state["locked"] = False
			game.say( self.data["unlocked_msg"])

	def get_state_data(self):
		return self.state
