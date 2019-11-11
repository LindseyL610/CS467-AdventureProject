import os
import json

class Exit:
	def __init__(self, data, state):
		#TEMPORARILY REMOVING THIS
		#self.data = data.copy()
		#self.state = state.copy()

		# ATTRIBUTES FROM THING-- need to figure out how to make this inherit
		# id
		# long description - used for look() and first time room visited
		# short description - used for second time room visited
			# also used by Room for Things in Room when look() is called for Room
			# can be based on different statuses, or just default
		# responses : {
		#				[verb] : RESPONSE_TEXT,
		#				[verb] : RESPONSE_TEXT
		#					etc
		#			}
		
		# SPECIAL EXIT ATTRIBUTES		
		# locked: True/False
		# openable : True/False
		# open: True/False
		# key_needed: some_item
		# rooms {"north" : "room1", "south": "room2" }
		# exit_message : {
		#					room1: "You climb up the stairs to room1.",
		#					room2: "You climb down the stairs to room2."
		#				}
		
		# BEGIN SAMPLE DATA
		self.id = "stairs"
		self.type = "exit"
		self.locked = False
		self.openable = True
		self.key_needed = "key"
		self.rooms = ["room1", "room2"]
		self.exit_message = dict()
		self.exit_message["room1"] = "You climb up the stairs to room1"
		self.exit_message["room2"] = "You climb down the stairs to room2."

	def get_destination(self, origin):
		for room in rooms:
			if room == "origin" is False:
				return room

	#TODO: ADD THESE FUNCTIONS
	# open() - OVERRIDES GENERIC- just to give a sense of realism
		# can Exit be opened?
			# if not openable
				# say "You can't open the [Exit]!"
				# return false
			# if openable
				# is Exit locked?
					# if locked, say "The [Exit] is locked!"
						# return false
					# if unloacked
						# is already open?
							# say "The [Exit] is already open!"
							# return false
						# else
							# open = true
							# say "You opened the [Exit]."
							# return true
			
	# unlock(key) - OVERRIDES GENERIC
		# is Exit unlocked already?
			# if unlocked
				# say "The [Exit] is already unlocked!"
				# return false
			# if locked
				# is it correct key?
					# if key matches key_needed
						# locked = False
						# say "You unlocked the [Exit]"!
						# return true
					# if key does not match
						# say "The [key] does not unlock the [Exit]!"
						# return false

	# TODO: REMOVE THESE
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

	def get_state_data(self):
		return self.state
