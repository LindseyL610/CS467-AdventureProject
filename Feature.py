import os
import json

class Feature:
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()


	def perform_action(self, game, act):
		if self.state["current_state"] != self.data["actions"][act]:
			self.state["current_state"] = self.data["actions"][act]
		
			if self.state["current_state"] in self.data["display"]:
				ret_str = self.data["display"][self.state["current_state"]]

			if self.state["current_state"] in self.data["items"]:
				game.objects[game.get_current_room()].add_dropped_item(self.data["items"][self.state["current_state"]])

			if self.data["id"] == "key" and act == "use":
				game.objects["stone door"].state["locked"] = False

			if self.data["id"] == "cheese":
				if "cheese" in game.state["bag"]:
					game.state["bag"].remove("cheese")
				else:
					game.objects[game.get_current_room()].state["items"].remove("cheese")

		else:
			ret_str = "You already did that."

		return ret_str

	def take(self, game):
		if self.data["can_be_taken"]:
			game.take_item(self.data["id"])
		else:
			game.say("You cannot take the " + self.data["id"] + ".")

	def drop(self, game):
		game.drop_item(self.data["id"])

	def read(self, game):
		if self.data["can_be_read"]:
			game.say(self.data["read_msg"])
		else:
			game.say("You cannot read the " + self.data["id"] + ".")

	def unlock(self, game):
		if self.data["can_be_unlocked"]:
			game.say("You unlocked the " + self.data["id"] + ".")
		else:
			game.say("You cannot unlock the " + self.data["id"] + ".")

	def eat(self, game):
		eaten = False

		if self.data["can_be_eaten"]:
			if self.data["id"] in game.state["bag"]:
				game.state["bag"].remove(self.data["id"])
				eaten = True
			elif self.data["id"] in game.objects[game.get_current_room()].state["items"]:
				game.objects[game.get_current_room()].state["items"].remove(self.data["id"])
				eaten = True

		if eaten == True:
			game.say("You ate the " + self.data["id"] + ".")
		else:
			game.say("You cannot eat the " + self.data["id"] + ".")

	def get_state_data(self):
		return self.state
