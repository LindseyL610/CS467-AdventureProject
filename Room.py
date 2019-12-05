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

		self.documentation = ""

		self.msg_already_pro = "You are already feeling the effects of the pro function."
		self.msg_pro = "Your speed and coordination increase!"

		self.msg_dance = "You dance. Nothing happens."

		self.hints = []
		self.used_hints = 0

	def get_status(self, type=None):
		"""returns the status of a room in JSON format"""

		if type is None:
			type = "Room"

		# Returns the appropriate export value based on whether value is a Room or Thing
		def get_export_value(value):
			if isinstance(value, Room):
				return "<R:" + value.id + ">"
			elif isinstance(value, Thing.Thing):
				return "<T:" + value.id + ">"
			else:
				return value

		str_dict = self.__dict__.copy()

		# print ("str_dict before: " + str(str_dict))

		for attr in str_dict:
			if isinstance(str_dict[attr], list):
				new_list = list()
				for x in str_dict[attr]:
					new_list.append(get_export_value(x))
				str_dict[attr] = new_list
			elif isinstance(str_dict[attr], dict):
				new_dict = dict()
				for x in str_dict[attr]:
					new_dict[x] = get_export_value(str_dict[attr][x])
				str_dict[attr] = new_dict
			else:
				str_dict[attr] = get_export_value(str_dict[attr])

		# print ("str_dict after: " + str(str_dict))

		ret_val = dict()
		ret_val["type"] = type
		ret_val["data"] = str_dict

		return json.dumps(ret_val)

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

	def get_description(self, time=None):
		# print("Room.get_description()")
		# print("time = " + str(time))

		say(self.name)
		if self.has_been_visited:
			description_string = self.short_description
			listed_things = []
			already_described = [] # Stores exits that have already been described

			for exit in self.exits.values():
				# Only do this if exit hasn't already been described
				if exit.is_accessible and exit not in already_described:
					if exit.has_dynamic_description:
						description_string += " " + exit.get_dynamic_description()
						already_described.append(exit) # Append exit to described exits
					
					if exit.is_listed:
						listed_things.append(exit)


			for thing in self.contents:
				if thing.is_accessible and thing not in already_described:
					if thing.has_dynamic_description:
						description_string += " " + thing.get_dynamic_description()
						already_described.append(thing)

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
		self.get_description(game.game_time)

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

		# for exit in set(self.exits.values()):
		for exit in self.exits.values():
			all_contents_list.append(exit)

		return all_contents_list

	# returns all accessibel contents in a room
	# if deep=True (default) it also returns things inside of storage
	def get_all_accessible_contents(self, deep=True):
		"""return everything in a room that IS accessible, from contents, storage, and exits"""
		all_contents_list = set()
		for item in self.contents:
			if item.is_accessible:
				all_contents_list.add(item)
				if hasattr(item, "contents") and item.contents_accessible and deep:
					for subitem in item.contents:
						if subitem.is_accessible:
							all_contents_list.add(subitem)

		for exit in self.exits.values():
			if exit.is_accessible:
				all_contents_list.add(exit)

		return all_contents_list

	def dance(self, game, actionargs):
		say(self.msg_dance)

	def pro(self, game, actionargs):
		if game.player.pro:
			say(self.msg_already_pro)
		else:
			game.player.pro = True
			say(self.msg_pro)

	def led(self, game, actionargs):
		say("The lights are already on.")

	def sleep(self, game, actionargs):
		hours = int(-1)

		while (hours < 1) or (hours > 12):
			say("How many hours do you want to sleep for (between 1 and 12)?")
			hours = input("> ")

			try:
				hours = int(hours)
				
				if (hours < 1) or (hours > 12):
					say("You must enter an integer between 1 and 12.")
			except ValueError:
				hours = int(-1)
				say("You must enter an integer between 1 and 12.")

		count = 0

		while count < hours:
			game.advance_time()

			count += 1

		hours = str(hours)

		say("You slept for " + hours + " hours.")

		self.look(game, actionargs)

	def hint(self, game, acitonargs):
		max_hints = len(self.hints)
		if not self.hints:
			say("There are no hints for this room")
		else:
			if self.used_hints < max_hints:
				self.used_hints += 1
			for num in range(self.used_hints):
				say("Hint #{}: ".format(num+1) + self.hints[num])
			if self.used_hints == max_hints:
				say("There are no additional hints.")

class ClockRoom(Room):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.special_time = list()
		self.shifty_man = None

	def get_status(self):
		return super().get_status("ClockRoom")

	def get_description(self, time=-1):
		if time != -1:
			if time not in self.special_time:
				if self.shifty_man in self.contents:
					self.remove_thing(self.shifty_man)
				super().get_description()
			else:
				super().get_description()
				self.add_thing(self.shifty_man)
				say("There is a shifty man standing in front of the door.")
		else:
			super().get_description()
			 
class DarkWeb(Room):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.contains_moth = False
		self.is_lit = False
		self.msg_already_lit = "The room is already lit."
		self.msg_lit = "You here a faint buzzing sound, and then a light at the opposite " \
					   "end of the room suddenly turns on. Then another light, turns on, and another, " \
					   "until the whole room is fully lit. You shield your eyes until they have time to adjust. " \
					   "When you finally look around, you see a room completely filled with cobwebs, " \
					   "which have a tape tangled in them, "\
					   "and at the far end of the room... a large spider. "
		self.alternate_description = "A long room filled with cobwebs."
		self.moth_msg = "Looking closer, you can see the moth you sprayed earlier trapped "\
				"in the web, with the spider directly over it."
	def get_status(self):
		return super().get_status("DarkWeb")

	def get_description(self, time=None):
		say(self.name)

		if not self.has_been_visited:
			say(self.long_description)
			self.has_been_visited = True
		else:
			if not self.is_lit:
				description_string = self.short_description

				for exit in self.exits.values():
					if exit.has_dynamic_description:
						description_string += " " + exit.get_dynamic_description()

				say(description_string)

			else:
				description_string = self.short_description
				listed_things = []

				for exit in self.exits.values():
					if exit.is_accessible:
						if exit.has_dynamic_description:
							description_string += " " + exit.get_dynamic_description()

						if exit.is_listed:
							listed_things.append(exit)

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

	def led(self, game, actionargs):
		if self.is_lit is False:
			self.is_lit = True

			for item in self.contents:
				if item.name == "cobwebs":
					item.description = "Sticky cobwebs cover the walls, ceiling, "\
							   "and floors, only getting denser further into the room."
					break

			message = self.msg_lit

			if self.contains_moth:
				message += self.moth_msg

			say(message)
			self.short_description = self.alternate_description

		# add floppy
		# change properties of stuff in room (floppy, cobwebs, spider?)
		else:
			say(self.msg_already_lit)


class Ballroom(Room):
	def __init__(self, id, name):
		super().__init__(id, name)

	def get_status(self):
		return super().get_status("Ballroom")

	def dance(self, game, actionargs):
		if game.thing_list["DancingDaemon"] in self.get_all_contents():
			game.thing_list["DancingDaemon"].dance(game, actionargs)
		else:
			message = "You dance like no one's watching. Except you feel like someone is watching..."
			say(message)


class BusStation(Room):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.special_time = list()
		self.bus = None
		self.daemon = None

	def get_status(self):
		return super().get_status("BusStation")

	def get_description(self, time=-1):
		# print("BusStation.get_description()")
		# print("special_time = " + str(self.special_time))
		# print("time = " + str(time))
		# print("bus= " + self.bus.id)

		if time != -1:
			if time not in self.special_time:
				self.set_normal()
				super().get_description()
			else:
				self.set_special()
				super().get_description()
				print()
				say("You caught the bus! It is waiting at the platform...")
		else:
			super().get_description()

	def set_normal(self):
		self.remove_thing(self.bus)
		self.remove_thing(self.daemon)

	def set_special(self):
		self.add_thing(self.bus)
		self.add_thing(self.daemon)
