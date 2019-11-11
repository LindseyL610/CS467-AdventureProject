import os
import json

class Feature:
	def __init__(self, data, state):
		# REMOVING FOR NOW
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
		
		# SPECIAL FEATURE ATTRIBUTES
		# takeable: True/False
		# surface: [item1, item2, etc] OR None
		# container: [item1, item2, etc] OR None
		# surface_capacity: (int)
		# container_capacity (int)
		# container_locked : True/False
		# key_needed : some_item
		# container_open : True/False
		# container_closeable: True/False
		# keyboard : True/False

	# FUNCTIONS:
	# take(item)
		# determine if item is on surface
			# if is_surface
				# if item is in [surface]
					# remove item from [surface]
					# return True
		# determine if item is in container
			# if is_container
				# if not container_locked AND if container_open:
					# remove item from [container]
					# return True
		# otherwise return False

	# put(item_id, preposition)
		# if preposition is "on"
			# if is_surface
				# if len(surface) is less than surface_capacity
					# add item to [surface]
					# say "You put the [item] on the [Feature].
					# return true
				# else
					# say "There is no room for the [item]!"
					# return false
			# else
				# say "You can't put the [item] there!"
				# return false
		# if preposition is "in"
			# if is_container
				# if len(container) is less than container_capacity
					# if container_open
						# add item to [container]
						# say "You put the [item] in the [Feature]"
						# return true
					# else if container is not open
						# say "The [Feature] is not open!"
						# return false
				# else
					# say "There is no room for the [item]!"
					# return false
			# else
				# say "You can't put the [item] there!"
				# return false
				
	# open() - OVERRIDES GENERIC
		# if is_container is False
			# say "You can't open the [Feature]!"
			# return false
		# else if is_container is True
			# if container_open is True:
				# say "The [Feature] is already open!"
				# return False
			# else
				# if container_locked is True:
					# say "The [Feature] is locked!"
					# return False
				# else if container_locked is False
					# container_open = True
					# say "You opened the [Feature]."
					# return True
			
	# unlock(key) - OVERRIDES GENERIC
		# if not is_container
			# say "You can't unlock the [Feature]!"
			# return false
		# else
			# is container already open?
				# if already open
					# say "The [Feature] is already open!"
					# return false
				# if not open
					# is the container locked?
						# if not locked
							# if key_needed is None
								# say "There is no lock on the [Feature]."
								# return false
							# if a key is needed
								# say "The [Feature] is already unlocked!"
								# return false
						# if locked
							# does the key match?
								# if key does not match
									# say "The [key] does not work on the [Feature]!"
									# return false
								# if key matches
									# locked = False
									# say "You unlocked the [Feature]."
									# return true


	# TODO REMOVE and replace with above functions:
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


	def unlock_door():
		ret_str = "You unlocked the door."
		return ret_str

	def get_state_data(self):
		return self.state
