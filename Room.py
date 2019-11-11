import os
import json
import Exit
import Feature

class Room:
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
		
		# SPECIAL ROOM ATTRIBUTES
		# visited: True/False
		# Exits {"north" : [Exit] or None, "south":[Exit or None], etc }
		# items ["item1", "item2" ...]
		# features [[Feature1], [Feature2], ...]

		#SAMPLE DATA - TO BE REMOVED
		self.id = "room"
		self.long_description = "You are in a room and this description is long."
		self.short_description = "You are in the room."
		self.response = dict()
		self.response["verb1"] = "RESPONSE TEXT 1"
		self.response["verb2"] = "RESPONSE TEXT 2"
		self.visited = False
		self.exits = dict()
		self.exits["north"] = "stairs"
		self.exits["south"] = "door"
		self.exits["east"] = None
		self.exits["west"] = None
		self.items = list()
		self.items.append("item1")
		self.items.append("item2")
		self.features = list()
		self.features.append("feature1")


	# THIS MUST OVERRIDE GENERIC LOOK FUNCTION
	# look() - always says the long descripton and the description of everything else
		# say the long description
		# for each Item, Feature, or Exit, say the short description

	# prompt_message() - returns msg to display when user enters Room
		# if not visited
			# start with long description
			# for each Item, Feature, or Exit, add short descriptions
			# return combined descriptions as string
		# if visited
			# Start with: "You are in the [Room]"
			# for each Item, Feature, Exit, get short descriptions
			# return combined descriptions as string

	# search(search_id)
		# if id is in items
			# return true
		# otherwise, for each [feature]
			# does the feature id match the search_id?
				# if it matches, return true
			# if Feature is a surface
				# if Feature.surface has item matching search_id
					# return true
			# if feature is a container
				# if feature.container is OPEN and also has item matchin search_id
					# return true

	# take(id) - OVERRIDES GENERIC TAKE FUNCTION
		# if [id] is in [items]
			# remove [id] from [items]
			# return True
		# otherwise, for each [feature]
			# if the [id] is the Feature (ids match)
				# can the Feature be taken?
					# if so
						# remove [id] from [features]
						# does the Feature have anything on it?
							# If so
								# for each item in Feature.surface
									# remove item from Feature.surface
									# add the removed item to Room.items
									# say "The [item] fell on the floor!"
						# return True
					# if not, return False
			# otherwise, check if the Feature HAS the [id]
				# call Feature.take([id]) and return result

	# add_item([id])
		# add [id] to [items]

	# CODE NEEDS TO BE REPLACED WITH ABOVE
	def get_prompt(self, game):
		if not self.state['visited']:
			prompt = self.data["long_description"]
			self.state['visited'] = True
		else:
			prompt = self.data["short_description"]

		for itm in self.state["items"]:
			obj = game.objects[itm]

			if obj.data["static"] == False:
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
