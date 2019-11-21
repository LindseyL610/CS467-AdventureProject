from Utilities import say
import Utilities
import Thing
import json


class Room:
	"""Basic Room class"""

	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.long_description = ""
		self.short_description = ""
		self.exits = {}

		self.has_been_visited = False
		self.contents = []

		self.msg_cannot_go_direction = "You cannot go that direction."

	def get_status(self):
		"""returns the status of a room in JSON format"""
		
		# Returns the appropriate export value based on whether value is a Room or Thing
		def get_export_value(value):
			if isinstance(value, Room):
				return "<R:" + value.id + ">"
			elif isinstance(value, Thing.Thing):
				return "<T:" + value.id + ">"
			else:
				return value

		str_dict = self.__dict__

		#print ("str_dict before: " + str(str_dict))

		for attr in str_dict:
			if isinstance(str_dict[attr], list):
				i = 0
				for x in str_dict[attr]:
					str_dict[attr][i] = get_export_value(x)
					i += 1
			elif isinstance(str_dict[attr], dict):
				for i in str_dict[attr]:
					str_dict[attr][i] = get_export_value(str_dict[attr][i])
			else:
				str_dict[attr] = get_export_value(str_dict[attr])

		#print ("str_dict after: " + str(str_dict))

		return json.dumps(str_dict)

	def set_status(self, status, thing_list, room_list):
		"""uses the JSON data in status to update the thing"""

		# Returns the appropriate import value based on whether value is Room or Thing
		def get_import_value(value, thing_list, room_list):
			list = None

			if isinstance(value, str):
				if value.find("<R:") == 0:
					list = room_list
				elif value.find("<T:") == 0:
					list = thing_list

				if list is not None:
					id = value[3:(value.find(">"))]
					return list[id]
			
			return value

		status_obj = json.loads(status)

		for attr in status_obj:
			if isinstance(status_obj[attr], list):
				imp_val = list()
				for x in status_obj[attr]:
					imp_val.append(get_import_value(x, thing_list, room_list))
			elif isinstance(status_obj[attr], dict):
				imp_val = dict()
				for i in status_obj[attr]:
					imp_val[i] = get_import_value(status_obj[attr][i], thing_list, room_list)
			else:
				imp_val = get_import_value(status_obj[attr], thing_list, room_list)
		
			setattr(self, attr, imp_val)

	def get_description(self):
		say(self.name)
		if self.has_been_visited:
			description_string = self.short_description
			listed_things = []
			# self.get_all_accessible_contents()
			for thing in self.get_all_accessible_contents():
				if thing.has_dynamic_description:
					description_string += " " + thing.get_dynamic_description()

				if thing.is_listed:
					listed_things.append(thing)

			num_listed_things = len(listed_things)

			if num_listed_things > 0:
				list_string = " You see"
				list_string += Utilities.list_to_words([o.list_name for o in listed_things])
				list_string += "."
				description_string += list_string

			say(description_string)


		else:
			say(self.long_description)
			self.has_been_visited = True

	def look(self, game, actionargs):
		self.get_description()

	def go(self, game, actionargs):

		direction = actionargs.get("dobj")
		if self.exits.get(direction):
			self.exits[direction].go(game, actionargs)
		else:
			say(self.msg_cannot_go_direction)

	def add_thing(self, thing):
		self.contents.append(thing)

	def remove_thing(self, thing):
		# TODO also handle removing thing from a storage object in the room
		self.contents.remove(thing)

	def get_all_contents(self):
		"""return everything in a room (accessible or not) from contents, storage, and exits"""
		all_contents_list = self.contents.copy()
		for item in self.contents:
			if hasattr(item, "contents"):
				all_contents_list.extend(item.contents)

		for exit in self.exits.values():
			all_contents_list.append(exit)

		return all_contents_list

	def get_all_accessible_contents(self):
		"""return everything in a room that IS accessible, from contents, storage, and exits"""
		all_contents_list = []
		for item in self.contents:
			if item.is_accessible:
				all_contents_list.append(item)
				if hasattr(item, "contents") and item.contents_accessible:
					for subitem in item.contents:
						if subitem.is_accessible:
							all_contents_list.append(subitem)

		for exit in self.exits.values():
			if exit.is_accessible:
				all_contents_list.append(exit)

		return all_contents_list


# OLD Room.py just in case
#
# import os
# import json
# import Exit
# import Feature
#
# class Room:
# 	def __init__(self, data, state):
# 		self.data = data.copy()
# 		self.state = state.copy()
#
# 	def get_prompt(self, game):
# 		if not self.state['visited']:
# 			prompt = self.data["long_description"]
# 			self.state['visited'] = True
# 		else:
# 			prompt = self.data["short_description"]
#
# 		for itm in self.state["items"]:
# 			obj = game.objects[itm]
#
# 			if obj.data["static"] == False:
# 				if obj.state["current_state"] in obj.data["message"]:
# 					prompt += ("\n" + obj.data["message"][obj.state["current_state"]])
# 				else:
# 					prompt += ("\n" + obj.data["message"]["default"])
#
# 		return prompt
#
# 	def check_item(self, item):
# 		for itm in self.state["items"]:
# 			if itm == item:
# 				return True
#
# 		return False
#
# 	def remove_item(self, item):
# 		if item in self.state["items"]:
# 			self.state["items"].remove(item)
#
# 	def add_dropped_item(self, item):
# 		self.state["items"].append(item)
#
# 	def get_state_data(self):
# 		return self.state
