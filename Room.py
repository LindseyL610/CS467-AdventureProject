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
		self.msg_nothing_happens = "Nothing happens."

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
			# TESTING BEGIN
			print("room contents:")
			for c in self.contents:
				print(type(c))
			# TESTING END
			description_string = self.short_description
			listed_things = []

			# for thing in self.get_all_accessible_contents():
			for thing in self.contents:
				if thing.is_accessible:
					if thing.has_dynamic_description:
						description_string += " " + thing.get_dynamic_description()

					if thing.is_listed:
						listed_things.append(thing)

			num_listed_things = len(listed_things)

			if num_listed_things > 0:

				list_string = " You see"
				list_string += Utilities.list_to_words([o.get_list_name() for o in listed_things])
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
		if thing in self.contents:
			self.contents.remove(thing)
		else:
			for content in self.contents:
				if content.has_contents:
					if thing in content.contents:
						content.remove_item(thing)

	def add_exit(self, exit, direction):
		if direction not in self.exits.keys():
			self.exits[direction] = exit
		else:
			say("ERROR: THAT DIRECTION ALREADY HAS AN EXIT")

	def remove_exit(self, exit_to_remove):
		# redefine exits without exit_to_remove
		# self.exits = {dir: ex for dir, ex in self.exits if ex is not exit_to_remove}

		remove_exits = [dir for dir in self.exits if self.exits[dir] == exit_to_remove]
		for dir in remove_exits: del self.exits[dir]

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

	def pro(self, game, actionargs):
		say(self.msg_nothing_happens)

	def led(self, game, actionargs):
		say(self.msg_nothing_happens)

class DarkWeb(Room):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.is_lit = False

		self.msg_already_lit = "The room is already lit."
		self.msg_lit = "You here a faint buzzing sound, and then a light at the opposite " \
					   "end of the room suddenly turns on. Then another light, turns on, and another, " \
					   "until the whole room is fully lit. You sheild your eyes until they have time to adjust. " \
					   "When you finally look around, you see a room completely filled with spider webs, " \
					   "and at the far end of the room... a large spider."
		self.alternate_description = "A long room filled with cobwebs. There is an opening to the north."

	def get_status(self):
		return super().get_status("DarkWeb")

	def led(self, game, actionargs):
		if self.is_lit is False:
			self.is_lit = True

			say(self.msg_lit)
			self.short_description = self.alternate_description

			# add floppy
			# change properties of stuff in room (floppy, cobwebs, spider?)
		else:
			say(self.msg_already_lit)