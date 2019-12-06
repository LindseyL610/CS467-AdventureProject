from Utilities import say
import Utilities
import json
import Room

class Thing:
	"""The basic class for all non-Room objects in the game"""

	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.adjectives = []
		self.alternate_names = []
		# how the item should appear in a list. A book. An apple. A piece of cheese.
		self.list_name = "a " + name

		# Starting Location is a Room
		self.starting_location = None

		self.can_be_taken = False
		self.can_be_read = False
		self.can_be_dropped = False
		self.has_been_taken = False
		self.can_go = False
		self.has_contents = False
		self.clock = False

		self.can_be_opened = False
		self.can_receive = False

		self.has_dynamic_description = False
		self.is_listed = True

		self.is_accessible = True

		## room or storage of current location
		self.current_location = None  # Room

		self.description = "This is a thing."
		self.dynamic_description_text = "There is a thing."

		# Default Text for all messages
		self.msg_take_first = "You take the {}.".format(self.name)
		self.msg_take = "You take the {}.".format(self.name)
		self.msg_cannot_take = "You cannot take the {}.".format(self.name)
		self.msg_already_in_inventory = "You already have the {}.".format(self.name)

		self.msg_cannot_read = "There is nothing to read on the {}.".format(self.name)
		self.msg_cannot_be_opened = "The {} cannot be opened".format(self.name)
		self.msg_cannot_be_closed = "The {} cannot be closed".format(self.name)

		self.msg_drop = "You drop the {}.".format(self.name)
		self.msg_cannot_drop = "You cannot drop the {}".format(self.name)

		self.msg_cannot_go = "That is not a way you can go."
		self.msg_go = "You go that way."

		self.msg_cannot_pull = "You cannot pull that."

		self.msg_has_no_contents = "The {} can't store anything.".format(self.name)
		self.msg_cannot_look_in = "You cannot look in the {}".format(self.name)

		self.msg_nothing_happens = "Nothing happens"

		self.msg_cannot_eat = "You cannot eat that."

		self.msg_cannot_drink = "You cannot drink that."

		self.msg_cannot_play = "You cannot play that."

		self.msg_cannot_dance = "You cannot dance with that."

		self.msg_cannot_spray = "You cannot spray that."

		self.msg_cannot_talk = "You cannot talk to that."

		self.msg_cannot_sit = "You cannot sit there."

	def get_status(self, type):
		"""returns the status of a thing in JSON format"""

		# Returns the appropriate export value based on whether value is a Room or Thing
		def get_export_value(value):
			if isinstance(value, Room.Room):
				return "<R:" + value.id + ">"
			elif isinstance(value, Thing):
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

	def get_desc(self):
		"""returns the description to be used when looking at the room"""
		return self.description

	def get_dynamic_description(self):
		"""returns the description to be used when looking at the room"""
		return self.dynamic_description_text

	def get_list_name(self):
		return self.list_name

	# ACTION for look (and look at)
	def look(self, game, actionargs):
		cannot_see = False
	
		if  game.player.current_room.id == "roomI":
			if not game.player.current_room.is_lit\
			and self.name != "cobwebs":
				cannot_see = True
			
		if cannot_see:
			say("You don't see {}.".format(self.list_name))
			say("But then again you can't really see much of anything...")
		else:
			say(self.get_desc())

	def look_in(self, game, actionargs):
		say(self.msg_cannot_look_in)


	# ACTION for read
	def read(self, game, actionargs):
		if self.can_be_read:
			self.look(game, actionargs)
		else:
			say(self.msg_cannot_read)

	def open(self, game, actionargs):
		say(self.msg_cannot_be_opened)

	def close(self, game, actionargs):
		say(self.msg_cannot_be_closed)

	# ACTION for take
	def take(self, game, actionargs):
		if self.can_be_taken:
			if game.player.is_in_inventory(self):
				say(self.msg_already_in_inventory)
			else:
				game.player.take(self)
				if not self.has_been_taken:
					self.has_been_taken = True
					say(self.msg_take_first)
				else:
					say(self.msg_take)
		else:
			say(self.msg_cannot_take)

	# ACTION for "drop"
	def drop(self, game, actionargs):
		if self.can_be_dropped:
			say(self.msg_drop)
			# TODO make sure game function is used properly
			game.player.drop(self)
		else:
			say(self.msg_cannot_drop)

	def put_down(self, game, actionargs):
		self.drop(game, actionargs)

	def give_to(self, game, actionargs):
		if self.can_be_dropped:
			thing_to_receive = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
			if thing_to_receive is game.thing_list["shiftyMan"]:
				say("The shifty man does not want the {}.".format(self.name))
			elif thing_to_receive.can_receive:
				# TODO better define default action?
				say("")
			else:
				say("You cannot give anything to the {}".format(thing_to_receive.name))
		else:
			say("You cannot give the {}.".format(self.name))

	def go(self, game, actionargs):
		"""Default response for "cannot go" """
		say(self.msg_cannot_go)

	def put_in(self, game, actionargs):
		if not self.can_be_dropped:
			say(self.msg_cannot_drop)
		else:
			storage_object = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
			storage_object.receive_item(game, self, "in")

	def put_on(self, game, actionargs):
		if not self.can_be_dropped:
			say(self.msg_cannot_drop)
		else:
			storage_object = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
			storage_object.receive_item(game, self, "on")

	def pull(self, game, actionargs):
		say(self.msg_cannot_pull)

	def receive_item(self, game, item, prep):
		say("You can't put things {} the {}.".format(prep, self.name))

	def use(self, game, actionargs):
		say(self.msg_nothing_happens)

	def dance(self, game, actionargs):
		say(self.msg_cannot_dance)

	def eat(self, game, actionargs):
		say(self.msg_cannot_eat)

	def drink(self, game, actionargs):
		say(self.msg_cannot_drink)

	def play(self, game, actionargs):
		say(self.msg_cannot_play)

	def spray(self, game, actionargs):
		say(self.msg_cannot_spray)

	def spray_with(self, game, actionargs):
		say(self.msg_cannot_spray)

	def talk(self, game, actionargs):
		say(self.msg_cannot_talk)

	def hit(self, game, actionargs):
		say(self.msg_nothing_happens)

	def sit(self, game, actionargs):
		say(self.msg_cannot_sit)

	# Special Functions
	def ram(self, game, actionargs):
		say(self.msg_nothing_happens)

	def kin(self, game, actionargs):
		say(self.msg_nothing_happens)

	def tic(self, game, actionargs):
		say(self.msg_nothing_happens)


class Exit(Thing):
	"""Class for object that transports the player to another room."""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_go = True
		self.is_listed = False

		self.destination = None  # Room

	def go(self, game, actionargs):
		if self.can_go:
			say(self.msg_go)
			# TODO make sure game function is used properly
			game.player.go(self.destination)
			game.new_room = True
		else:
			say(self.msg_cannot_go)

	def use(self, game, actionargs):
		self.go(game, actionargs)

	def get_status(self, type=None):
		if type is None:
			type = "Exit"
		return super().get_status(type)


class Door(Exit):
	"""A special Exit, doors can be closed, locked, and unlocked"""

	def get_status(self, type=None):
		if type is None:
			type = "Door"
		return super().get_status(type)

	def open(self, game, actionargs):
		self.go(game, actionargs)

class BlockedDoor(Door):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_go = False
		self.locked = False
		self.msg_unlock = "The door is unlocked."
		self.msg_cannot_go = "You cannot go through the door."
		self.alt_msg_cannot_go =  None
		self.msg_go = "You go through the door."

	def get_status(self):
		return super().get_status("BlockedDoor")

	def go(self, game, actionargs):
		if self.id == "clockRoomDoor":
			if game.room_list["roomJ"].shifty_man in game.room_list["roomJ"].contents\
			and not self.can_go and self.alt_msg_cannot_go is not None:
				say(self.alt_msg_cannot_go)
			else:
				super().go(game, actionargs)
		else:
			super().go(game, actionargs)	
				

class MetaDoor(Door):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_go = False
		self.locked = True

		self.num_lights = 0
		self.msg_unlock = "The fifth and final orb along the top of the ornate door begins to glow. " \
						  "You hear clanging and whirring sounds as if some internal mechanism is " \
						  "operating inside the door."
		self.msg_cannot_go = "You try to open the door, but it will not budge."
		self.msg_go = "You approach the door, and with the slightest touch, it slowly swings open. " \
					  "You walk through."

	def get_status(self):
		return super().get_status("MetaDoor")

	def add_light(self):
		self.num_lights += 1
		if self.num_lights == 5:
			say(self.msg_unlock)
			self.can_go = True
			self.locked = False
		elif self.num_lights == 1:
			say("One of the orbs along the top of the ornate door suddenly begins to glow bright white.")
		else:
			say("Another orb on the door begins to glow. Now {} of the five orbs are shining "
				"bright.".format(self.num_to_word(self.num_lights)))

	def num_to_word(self, num):
		"""takes an integer 1 through 5 and returns it spelled out"""
		if num == 0:
			return "none"
		elif num == 1:
			return "one"
		elif num == 2:
			return "two"
		elif num == 3:
			return "three"
		elif num == 4:
			return "four"
		elif num == 5:
			return "five"

	def get_desc(self):
		description_text = "A towering ornate door. It is intricately decorated, and seems to be connected via " \
						   "various cords to the large computer. "
		if self.num_lights == 5:
			description_text += "All five orbs along the top of the door are glowing brightly."
		elif self.num_lights == 0:
			description_text += "There are five dark orbs along the top of the door."
		else:
			description_text += "There are five orbs along the top of the door, {} of which are " \
								"glowing white.".format(self.num_to_word(self.num_lights))
		say(description_text)


# class Door(Exit):
#     is_lockable = False
#     is_locked = False
#     is_open = True
#     will_unlock = []
#     message_unlocked = "The door is already unlocked."
#     message_locked = "The door is locked"
#     message_cant_unlock = "That can't unlock the door."
#     message_unlocked = "The door is unlocked."
#     message_not_lockable = "This door does not lock."
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name= name
#         self.adjectives = []
#         self.alternate_names = []
#         self.actions = {}
#
#     def unlock(self, object_id):
#         if not self.is_lockable:
#             say(self.message_not_lockable)
#         elif not self.is_locked:
#             say(self.message_unlocked)
#         elif object not in self.will_unlock:
#             say(self.message_cant_unlock)
#         else:
#             say(self.message_unlocked)
#             self.is_locked = False
#
#     def go(self):
#         if self.is_locked:
#             say(self.message_locked)
#


# class MultiKeyDoor(Door):
#     number_of_keys = 0
#     keys_to_unlock = 5
#
#
#     def get_description(self):
#         if
#
#

class Item(Thing):
	"""Takable, Dropable thing"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_taken = True
		self.can_be_dropped = True

	def get_status(self, type=None):
		if type is None:
			type = "Item"
		return super().get_status(type)


class RubberDuck(Item):
	def __init__(self, id, name):
		super().__init__(id, name)
	
	def get_status(self, type=None):
		if type is None:
			type = "RubberDuck"
		return super().get_status(type)

	def give_to(self, game, actionargs):
		recipient = game.get_thing_by_name(actionargs["iobj"], False)

		if recipient is not game.thing_list["shiftyMan"]:	
			recipient = Utilities.find_by_name(actionargs["iobj"], game.thing_list)

			if recipient.can_receive:
				say("The {} doesn't want the rubber duck.".format(recipient.name))
			else:
				say("You cannot give anything to the {}".format(recipient.name))
		else:
			door = game.thing_list["clockRoomDoor"]
			print(door.msg_unlock)
			door.locked = False
			door.can_go = True
			game.player.remove_from_inventory(self)

class Book(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_read = True
		self.can_be_dropped = False
		self.msg_cannot_drop = "This book of documentation seems too important to leave behind."

	def get_status(self, type=None):
		if type is None:
			type = "Book"
		return super().get_status(type)

	def read(self, game, actionargs):
		if not game.player.is_in_inventory(self):
			say("You pick up the book, and flip through its pages.")
			game.player.current_room.remove_thing(self)
			game.player.add_to_inventory(self)
		else:
			say("You flip through the \"Tome of Documentation\"...")
		book_text = "<WRITTEN_TEXT>"
		book_text += "Notes on the " + game.player.current_room.name + "\n"
		book_text += game.player.current_room.documentation + "\n"
		at_least_one_func = False
		for func in game.player.special_functions.values():
			if func["learned"] == True:
				if at_least_one_func == False:
					at_least_one_func = True
					book_text += "Special functions (used with 'call'): \n"

				book_text += func["name"].upper() + ": " + func["description"] + "\n"
		book_text += "</>"
		say(book_text)

	def open(self, game, actionargs):
		self.read(game, actionargs)


class Cheese(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_cannot_eat = "As you bring the cheese to your lips, the smell makes you gag." \
							  "You decide it isn't fit for human consumption."

	def get_status(self, type=None):
		if type is None:
			type = "Cheese"
		return super().get_status(type)

	def give_to(self, game, actionargs):
		thing_to_receive = Utilities.find_by_name(actionargs["iobj"], game.thing_list)

		if game.player.current_room.id == "roomI" and\
		game.player.current_room.is_lit == False and\
		thing_to_receive.id is not "cobwebs":	
			print("You don't see {}.".format(thing_to_receive.list_name))
			print("Then again you can't really see much of anything...")
			return

		if thing_to_receive is game.thing_list["hungryMouse"]:
			message = "As you hold out the cheese, the mosue's eyes widen. " \
					  "It snatches it from your hand, and runs to the opposite corner of the room. " \
					  "It begins nibbling away."
			say(message)
			self.mouse_eats_cheese(game, actionargs)
		else:
			thing_to_receive = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
			if thing_to_receive.can_receive:
				say("The {} doesn't want the cheese.".format(thing_to_receive.name))
			else:
				say("You cannot give anything to the {}".format(thing_to_receive.name))

	def drop(self, game, actionargs):
		if game.player.current_room is game.room_list["roomD"]:
			message = "You drop the cheese, and the mouses's eyes widen. " \
					  "It quickly darts over, grabs the cheese, and runs to the opposite corner of the room. " \
					  "It begins nibbling away."
			say(message)
			self.mouse_eats_cheese(game, actionargs)
		else:
			Thing.drop(self, game, actionargs)

	def mouse_eats_cheese(self, game, actionargs):
		game.player.remove_from_inventory(self)
		game.room_list["roomD"].remove_thing(game.thing_list["hungryMouse"])
		game.room_list["roomD"].add_thing(game.thing_list["eatingMouse"])
		game.thing_list["lever"].become_reachable()


class Ticket(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.dispensed = False

	def get_status(self, type=None):
		if type is None:
			type = "Ticket"
		return super().get_status(type)

	def take(self, game, actionargs):
		if not self.dispensed:
			say(self.msg_blocked)
		else:
			super().take(game, actionargs)

	def use(self, game, actionargs):
		accessible = game.player.current_room.get_all_accessible_contents()
		if game.thing_list["driverDaemon"] in accessible:
			args = actionargs.copy()
			args["iobj"] = "daemon"
			self.give_to(game, args)
		else:
			super().use(game, actionargs)

	def give_to(self, game, actionargs):
		thing_to_receive = game.get_thing_by_name(actionargs["iobj"], False)
		if thing_to_receive is game.thing_list["driverDaemon"]:
			message = "The DAEMON nods, takes your ticket, barely looking at you, and steps aside, granting access to the bus."
			say(message)
			self.grant_bus_access(game, actionargs)
		else:
			thing_to_receive = Utilities.find_by_name(actionargs["dobj"], game.thing_list)
			if thing_to_receive.can_receive:
				say("The {} doesn't want the ticket.".format(thing_to_receive.name))
			else:
				say("You cannot give anything to the {}".format(thing_to_receive.name))

	def grant_bus_access(self, game, actionargs):
		accessible = game.player.current_room.get_all_accessible_contents()
		if self in accessible:
			game.player.current_room.remove_thing(self)
		elif game.player.is_in_inventory(self):
			game.player.remove_from_inventory(self)
		game.room_list["roomG"].remove_thing(game.thing_list["busLocked"])
		game.room_list["roomG"].add_thing(game.thing_list["bus"])
		game.room_list["roomG"].bus = game.thing_list["bus"]


class Key(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_no_lock = "There is nothing to use the " + self.name + " with!"
		self.lock = None

	def get_status(self, type=None):
		if type is None:
			type = "Key"
		return super().get_status(type)

	def use(self, game, actionargs):
		# Determine if the applicable lock is accessible
		accessible = game.player.current_room.get_all_accessible_contents()
		if self.lock in accessible:
			args = actionargs.copy()
			args["iobj"] = self.lock.name
			self.put_in(game, args)
		else:
			say("There isn't anything that works with the " + self.name + "!")


class Drink(Item):

	def __init__(self, id, name):
		super().__init__(id, name)

	def get_status(self, type=None):
		if type is None:
			type = "Drink"
		return super().get_status(type)

	def use(self, game, actionargs):
		self.drink(game, actionargs)

	def drink(self, game, actionargs):
		message = "You take a sip of the {}.".format(self.name)
		say(message)


class Wine(Drink):
	def __init__(self, id, name):
		super().__init__(id, name)

	def get_status(self, type=None):
		if type is None:
			type = "Wine"
		return super().get_status(type)

	def drink(self, game, actionargs):
		if game.player.current_room is not game.room_list["roomE"] or game.thing_list["piano"].tip_received:
			super().drink(game, actionargs)
		else:
			say("You drink some wine and start to loosen up...")
			game.player.drunk = True


class Newspaper(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_read = True

	def get_status(self, type=None):
		if type is None:
			type = "Newspaper"
		return super().get_status(type)

	#def read(self, game, actionargs):								#COMMENTING THIS OUT, BECAUSE DESCRIPTION HAS CONTENT
		#contents = "The newspaper has an article about bugs."
		#say(contents)

	def open(self, game, actionargs):
		self.read(game, actionargs)


class Debugger(Item):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_sprayed = True

	def get_status(self, type=None):
		if type is None:
			type = "Debugger"
		return super().get_status(type)

	def spray(self, game, actionargs):
		say("You spray the Debugger in the air. Nothing happens.")


class Feature(Thing):
	"""Not-Takable, Not-Dropable thing"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_taken = False
		self.can_be_dropped = False
		self.msg_cannot_take = "The {} is fixed in place.".format(self.name)

	def get_status(self, type=None):
		if type is None:
			type = "Feature"
		return super().get_status(type)


class Seat(Feature):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_sit = "You sit on the {}. After resting for some time "\
				"on the comfortable {}, you get back up, ready "\
				"to continue exploring.".format(self.name, self.name)

	def get_status(self, type=None):
		if type is None:
			type = "Seat"
		return super().get_status(type)

	def sit(self, game, actionargs):
		say(self.msg_sit)	


class Lock(Feature):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.item_dispenser = False
		self.door_lock = False
		self.toggled = False
		self.controlled_exit = None
		self.open_exit = None
		self.key = None
		self.receive_preps = []
		self.already_used_msg = "The " + self.name + " has already been used!"
		self.incompatible_msg = "The " + self.name + " can not receive that item!"
		self.msg_toggled = ""
		self.key_consumed = False

	def get_status(self, type=None):
		if type is None:
			type = "Lock"
		return super().get_status(type)

	def receive_item(self, game, item, prep):
		if prep in self.receive_preps:
			if self.toggled:
				say(self.already_used_msg)
			elif item == self.key:
				say("You put the {} {} the {}.".format(item.name, prep, self.name))
				self.toggle(game)
				if self.key_consumed:
					accessible = game.player.current_room.get_all_accessible_contents()
					if item in accessible:
						game.player.current_room.remove_thing(item)
					elif game.player.is_in_inventory(item):
						game.player.remove_from_inventory(item)
		else:
			say("You can't put things {} the {}.".format(prep, self.name))

	# use
	def use(self, game, actionargs):
		# Determine if the key is accessible in the Room or in the Player's inventory
		accessible = game.player.current_room.get_all_accessible_contents()
		if self.key in accessible or game.player.is_in_inventory(self.key):
			self.receive_item(game, self.key, "in")
		else:
			say("You don't have anything that works with the " + self.name + "!")

	def unlock_exit(self, game):
		# Find direction(s) of the Exit
		directions = list()
		for dir in game.player.current_room.exits:
			if game.player.current_room.exits[dir] == self.controlled_exit:
				directions.append(dir)

		# Remove the Exit from the current room
		game.player.current_room.remove_exit(self.controlled_exit)

		# Add the "opened" Exit to the current room in the directions of the previous Exit
		for dir in directions:
			game.player.current_room.add_exit(self.open_exit, dir)

	def toggle(self, game):
		if self.door_lock:
			self.unlock_exit(game)
		elif self.item_dispenser:
			self.dispense_item(game)

		self.toggled = True
		say(self.msg_toggled)

	def dispense_item(self, game):
		game.player.add_to_inventory(self.item)


class Input(Feature):
	"""A feature that you can input text into (like a keyboard)
	By default they have one correct answer which performs one function.
	"""

	def __init__(self, id, name):
		super().__init__(id, name)
		# True if the input only functions once
		self.one_time_use = True
		self.triggers_once = True
		# True if the correct answer has already been triggered
		self.triggered = False

		self.msg_prompt = "What do you input?"
		self.msg_yn_prompt = "Would you like to input something? (y/n)"
		self.answer = "ANSWER"
		self.msg_correct_answer = "Correct!"
		self.msg_incorrect_answer = "Nothing happens."
		self.msg_already_triggered = "Nothing happens."
		self.msg_already_used = "There is nothing left to use it for."

	def get_status(self, type=None):
		if type is None:
			type = "Input"
		return super().get_status(type)

	def look(self, game, actionargs):
		say(self.get_desc())
		if not (self.one_time_use and self.triggered):
			yes_or_no = game.get_yn_answer(self.msg_yn_prompt)
			if yes_or_no:
				self.get_input(game, actionargs)

	def use(self, game, actionargs):
		say(self.get_desc())
		self.get_input(game, actionargs)

	def get_input(self, game, actionargs):
		if self.one_time_use and self.triggered:
			say(self.msg_already_used)
		else:
			response = game.get_word_answer(self.msg_prompt, self.answer)
			if (response):
				if self.triggers_once and self.triggered:
					say(self.msg_already_triggered)
				else:
					self.triggered = True
					say(self.msg_correct_answer)
					self.carry_out_action(game, actionargs)
			else:
				say(self.msg_incorrect_answer)

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		print("[[default action...]]")


class InputBalconyWindow(Input):
	"""the class for the input device on the balcony that opens the window"""

	# This status function is not working on its own
	def get_status(self):
		return super().get_status("InputBalconyWindow")

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# Open window...
		game.room_list["roomA"].remove_exit(game.thing_list["balconyWindowClosed"])
		game.room_list["roomA"].add_exit(game.thing_list["balconyWindowOpen"], "north")
		if not game.player.is_in_inventory(game.thing_list["book"]):
			book_message = "The force of the window opening has left the book on the floor. " \
						   "Curious, you decide to pick it up."
			say(book_message)
			game.player.current_room.remove_thing(game.thing_list["book"])
			game.player.add_to_inventory(game.thing_list["book"])


class InputPuzzle1(Input):
	"""the class for the input device in puzzle 1"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_prompt = "What do you input into the control panel?"
		self.answer = "gone"
		self.msg_correct_answer = \
			"The Control Panel displays this message: \n" \
			"<DIGITAL_TEXT>Crystals are gone, shutting down and switching to manual monitoring system.</>\n" \
			"All of the monitors in the room turn off, and it is now pitch black. \n" \
			"Your Documentation Tome begins to glow. Opening it, you see a new function appear: LED. " \
			"To use this function, input \"call LED\". You try it, and the lights in the room turn back on."

	# "The light from the tome fades away, and the room is again completely dark."

	def get_status(self):
		return super().get_status("InputPuzzle1")

	def get_desc(self):
		if not self.triggered:
			desc = \
				"The Control Panel has a large screen and a keyboard below it. On the screen is this message: \n" \
				"<DIGITAL_TEXT>Error: Crystals have disappeared without a TRACE. " \
				"Before turning offline, the monitoring system detected " \
				"four distinct paths the crystals took: \n" \
				"Path 1: FFFFF0 -> FFFF99 -> FF69B4 -> C19A6B -> 2A3439 -> 614051\n" \
				"Path 2: FFFF99 -> FF69B4 -> C19A6B -> FFFFF0 -> FFFF99\n" \
				"Path 3: 007FFF -> 800020 -> C19A6B -> FFFFF0\n" \
				"Path 4: 800020 -> FFFF99 -> 228B22 -> 614051 -> 228B22 -> FF69B4 -> 007FFF\n" \
				"Please input the current location of the crystals...</>"
		else:
			desc = "The control panel's screen is now blank."
		say(desc)

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# learn function
		game.player.learn_function("led")
		game.player.current_room.remove_thing(game.thing_list["puzzle1MonitorsBroken"])
		game.player.current_room.add_thing(game.thing_list["puzzle1MonitorsFixed"])


class InputPuzzle2(Input):
	"""the class for the input device in puzzle 2"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_prompt = "What do you type to complete the email?"
		self.answer = "alone"
		self.msg_correct_answer = \
			"You type the final word and send the email. You feel better now that this apology " \
			"has been sent to those who deserve to hear it. As you reflect on your bizarre adventure, " \
			"and dream of being free of this tower, you wonder when you will next see your own family. " \
			"Just then, your Tome of Documentation starts to get very warm. You open it and see a new function " \
			"has appeared: KIN. You can use it by saying \"call KIN on _____\". It will reconnect something with " \
			"it's relatives."
		self.msg_incorrect_answer = "You think harder, and realize that is not the right word to complete the email."

	def get_status(self):
		return super().get_status("InputPuzzle2")

	def get_desc(self):
		if not self.triggered:
			desc = "The computer is on, and on the screen it appears as though someone was composing an email. " \
				   "Here is what is says: \n" \
				   "<DIGITAL_TEXT>Dear family, \n" \
				   "I'm sorry for disrupting our relationship database. " \
				   "My actions have caught up to me. Now I must confess that my fears have become reality, " \
				   "for, now I am ...</> \n" \
				   "The email is missing a final word. What should you type before sending the email?"
		else:
			desc = "The computer's screen is now blank."
		say(desc)

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# learn function
		game.player.learn_function("kin")


class InputPuzzle3(Input):
	"""the class for the input device in puzzle 3"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_prompt = "What book do you search for?"
		self.answer = "hackers assets"
		self.msg_correct_answer = \
			"After entering the book title, you hear a buzzing as a drone flys from behind the table. " \
			"It zooms through the shelves before a small claw extends out and grasps a book. " \
			"The drone clumsily delivers the book onto the table. You flip through \"Hackers Assets\" " \
			"and learn about many tools for manipulating hardware and software. " \
			"You discover that sometimes, the best answer is brute force. " \
			"Just then your Tome of Documentation begins to thrash wildly. " \
			"It falls on the table and opens, and you see a new function appear: RAM. " \
			"This will apply a great force to something. " \
			"To use it, say \"call RAM on _____\". The drone is startled, grabs the hackers book and flies away."
		self.msg_incorrect_answer = "The search comes up empty, there are no books by that name."

	def get_status(self):
		return super().get_status("InputPuzzle3")

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# learn function
		game.player.learn_function("ram")

	def get_desc(self):
		if not self.triggered:
			desc = \
				"This touchscreen is used to search for books in the library. " \
				"Most are separated into two categories: <CLUE>hardware</> or <CLUE>software</>."
		else:
			desc = \
				"This touchscreen is used to search for books in the library. " \
				"A message comes up saying you have reached your maximum rentals."
		say(desc)


class InputPuzzle4(Input):
	"""the class for the input device in puzzle 3"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_prompt = "What status do you enter?"
		self.answer = "bricked"
		self.msg_correct_answer = \
			"The computer reads: \n" \
			"<DIGITAL_TEXT>\"BRICKED\" status detected. Initializing troubleshooting procedure.</> \n" \
			"Just then a small robot on wheels emerges from the computer! Startled, you jump back. " \
			"The tiny robot rolls over towards a large plug which seems to be powering the entire system. " \
			"With it's mechanical arms, it grabs the plug and yanks it from the wall. " \
			"The processors and computer shut down, and all of the awful noises and smoke stop. " \
			"After five seconds, the robot plugs the computer back in, and rolls back into the computer." \
			"The computer screen reads: <DIGITAL_TEXT>Booting up...</>. It appears you've fixed the system! " \
			"You suddenly feel a jolt, as if your Tome of Documentation just shocked you. " \
			"Opening its pages you see a new function appear: TIC. This function will make a machine malfunction; " \
			"to use it, say \"call TIC on _____\". "
		self.msg_incorrect_answer = "The computer reads: <DIGITAL_TEXT>You've entered an unknown status. " \
									"Please enter correct status.</>"

	def get_status(self):
		return super().get_status("InputPuzzle4")

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# learn function
		game.player.learn_function("tic")
		game.player.current_room.remove_thing(game.thing_list["puzzle4ProcessorsBroken"])
		game.player.current_room.add_thing(game.thing_list["puzzle4ProcessorsFixed"])

	def get_desc(self):
		if not self.triggered:
			desc = \
				"This large computer seems to be controlling the whole mechanical system in this room. It has keyboard, " \
				"and a large screen displaying this message: \n" \
				"<DIGITAL_TEXT>ERROR! Processing system is malfunctioning. Must diagnose problem. " \
				"Check error messages from processors, and input system status below to initiate troubleshooting."
		else:
			desc = \
				"This large computer seems to be controlling the whole mechanical system in this room. It has keyboard, " \
				"and a large screen displaying this message: \n" \
				"<DIGITAL_TEXT>Booting up...</>"
		say(desc)


class InputPuzzle5(Input):
    """the class for the input device in puzzle 5"""
    def __init__(self, id, name):
        super().__init__(id, name)
        self.msg_prompt = "What password do you enter?"
        self.answer = "finesse"
        self.msg_correct_answer = \
			"The computer unlocks! looking at the monitor, it appears an online course was in progress, " \
			"for increasing coordination. After skimming through a few pages, " \
			"you notice your Tome of Documentation begin to vibrate. " \
			"You open it up and see a new function has been added: PRO. " \
			"To use it, say \"call PRO\". This will temporarilty increase your skill and dexterity. " \
			"You exit the course and turn off the computer."
        self.msg_incorrect_answer = "You've entered the incorrect password."

    def get_status(self):
        return super().get_status("InputPuzzle5")

    # This is the function called on a successful answer
    def carry_out_action(self, game, actionargs):
        # learn function
        game.player.learn_function("pro")

    def get_desc(self):
        if not self.triggered:
            desc = \
				"This is a fancy computer with a large monitor and a standard US QWERTY keyboard. " \
				"The computer is on, but it appears to be stuck on a log-in screen. I" \
				"t looks like there have been a few incorrect password attempts, " \
				"and you can read them! What kind of security is that? " \
				"Who ever previously tried to log in experienced <CLUE>off-by-one-errors</> " \
				"with every key! The incorrect passwords were: \n" \
            "<DIGITAL_TEXT>COMDEXS \nGUMWEED \nROBSZED \nTUBREAR</>\n" \
            "You wonder what the actual password might be."
        else:
            desc = "The computer is turned off."
        say(desc)

class MetaPuzzleInput(Input):
	"""the class for the input device in the meta puzzle"""
	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_prompt = "What do you type?"
		self.msg_prompt2 = "What do you type?"
		self.answer = "pro ram kin tic led"
		self.answer2 = "geek"
		self.msg_correct_answer = \
			"Correct! More text appears on the screen: \n" \
			"<DIGITAL_TEXT>Now you should have learned something about yourself. What are you?</>"
		self.msg_correct_answer2 = \
			"The Mother DAEMON looks at you and silently nods. She comes over and guides your hands on the keyboard. " \
			"You press Control... then Alt... then Delete. Everything goes black.\n" \
			"When you come to, you find yourself sitting in front of your computer at home. " \
			"You have escaped the tower! And now you have a craving for cheese..."
		self.msg_incorrect_answer = "<DIGITAL_TEXT>Incorrect sequence.</>"
		self.msg_incorrect_answer2 = "<DIGITAL_TEXT>Incorrect. Look deeper.</>"

		self.description = \
			"This computer is identical to your computer at home. It is displaying a simple message: \n" \
			"<DIGITAL_TEXT>Enter in all five special functions (separated by spaces) in the correct order.</>"

	def get_status(self):
		return super().get_status("MetaPuzzleInput")

	# This is the function called on a successful answer
	def carry_out_action(self, game, actionargs):
		# learn function
		game.game_over = True
		game.end()

	def get_input(self, game, actionargs):
		response1 = game.get_word_answer(self.msg_prompt, self.answer)
		if (response1):
				say(self.msg_correct_answer)
				response2 = game.get_word_answer(self.msg_prompt2, self.answer2)
				if (response2):
					say(self.msg_correct_answer2)
					self.carry_out_action(game, actionargs)
				else:
					say(self.msg_incorrect_answer2)

		else:
			say(self.msg_incorrect_answer)


class Sign(Feature):
	"""Readable Feature"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_read = True

	def get_status(self):
		return super().get_status("Sign")


class Lever(Feature):
	"""Readable Feature"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.is_reachable = False

	def get_status(self):
		return super().get_status("Lever")

	def use(self, game, actionargs):
		self.pull(game, actionargs)

	def pull(self, game, actionargs):
		if self.is_reachable:
			lever_text = "You pull the lever. You hear a rumbling sound behind you and turn as a section of " \
						 "the west wall slides away, revealing a tunnel leading off to the west."
			say(lever_text)
			game.player.current_room.remove_exit(game.thing_list["secretWall"])
			game.player.current_room.add_exit(game.thing_list["mousepadTunnel"], "west")

		else:
			say("You cannot reach the lever, the mouse is in the way.")

	def become_reachable(self):
		self.is_reachable = True

	def get_desc(self):
		if self.is_reachable:
			say("A large lever is attatched to the wall. It is not clear what it is connected to.")
		else:
			say("Some kind of lever is attached to the wall. You can't get a closer look with the mouse in the way.")


class Computer(Feature):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.key_items = ["floppyDisk", "cartridge", "tape", "cd", "flashdrive"]
		self.inserted_things = list()
		self.description_text = \
			"This massive machine takes up most of the east wall. It is some sort of system of large rectangular devices all " \
			"connected with various wires. There are lights blinking, and you hear whirring and clicking sounds. " \
			"You can only assume it functions as some type of computer. " \
			"There appears to be a handful of unique ports in the machine where something could be inserted."

	def get_status(self):
		return super().get_status("Computer")

	def receive_item(self, game, item, prep):
		if prep == "in":
			if item.id in self.key_items:
				game.player.remove_from_inventory(item)
				self.inserted_things.append(item)
				say("You find an appropriate looking place to insert the {} into the "
					"computer.".format(item.name, prep, self.name))
				game.thing_list["lobbyOrnateDoor"].add_light()
			else:
				say("You can't find anywhere in the computer to put the {}.".format(item.name))
		else:
			say("You can't put things {} the computer.".format(prep))

	def get_desc(self):
		text = self.description_text
		if self.inserted_things:
			text += " You have inserted"
			text += Utilities.list_to_words([o.get_list_name() for o in self.inserted_things])
			text += "."
		say(text)


class Clock(Feature):
	"""Readable Feature that can tell game time"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_read = True

	def get_status(self):
		return super().get_status("Clock")

	def look(self, game, actionargs):
		say("The time is <DIGITAL_TEXT>t=" + str(game.game_time) + "</>")


class ComplexClock(Feature):
	"""For the clock in the Clock Room"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_read = True

	def get_status(self, type=None):
		if type is None:
			type = "ComplexClock"
		return super().get_status(type)

	def look(self, game, actionargs):
		say(self.description)
		say("The time is <DIGITAL_TEXT>t=" + str(game.game_time) + "</>")

class Piano(Feature):
	"""Playable piano"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.tip_received = False
		self.daemon_summoned = False
		self.msg_good = "You play the piano. Thanks to the wine, you're really groovin'. It sounds good!"
		self.msg_great = "You play the piano. Thanks to the PRO effects, you're unstoppable! It sounds great!"
		self.msg_bad = "You play the piano, but you feel a little stiff. It doesn't sound great. Maybe you'll play better if you loosen up somehow..."

	def get_status(self, type=None):
		if type is None:
			type = "Piano"
		return super().get_status(type)

	def use(self, game, actionargs):
		self.play(game, actionargs)

	def play(self, game, actionargs):
		if game.player.pro:
			say(self.msg_great)
			self.play_great(game)
		elif game.player.drunk:
			say(self.msg_good)
			self.play_good(game)
		else:
			say(self.msg_bad)

	def play_good(self, game):
		if not self.tip_received:
			self.tip_received = True
			game.thing_list["tipJar"].add_item(game.thing_list["coin"])
			print()
			say("You received a tip! A coin has appeared in the tip jar.")

	def play_great(self, game):
		self.play_good(game)
		if not self.daemon_summoned:
			self.daemon_summoned = True
			game.room_list["roomE"].add_thing(game.thing_list["DancingDaemon"])
			print()
			say("Your playing has attracted one of the tower's DAEMONs!")
			say(game.thing_list["DancingDaemon"].description)


class DancingDaemon(Feature):
	"""Daemon that appears"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.floppy_received = False
		self.floppy = None
		self.msg_dance = "You dance with the DAEMON!"

	def get_status(self, type=None):
		if type is None:
			type = "DancingDaemon"
		return super().get_status(type)

	def dance(self, game, actionargs):
		say(self.msg_dance)
		if not self.floppy_received:
			message = "The DAEMON gives you a " + self.floppy.name + "!"
			game.player.add_to_inventory(self.floppy)
			self.floppy_received = True
			say(message)


class Moth(Feature):
	"""Moth holding the cartridge"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.floppy_received = False
		self.floppy = None
		self.been_sprayed = False
		self.msg_spray = "You spray the moth with the Debugger."
		self.msg_first_spray = "The moth flies into the opening, taking whatever is in its mouth with it " \
							   ", but leaving the door unguarded."
		self.msg_been_sprayed = "The moth flaps its wings in an attempt to get away."
		self.in_web = False
		self.msg_kin_not_in_web = "Hundreds of other moths appear. They appear to check on the "\
			       		  "giant moth before flying away."
		self.msg_kin_in_web = "Hundreds of other moths appear. They work to free the giant moth "\
				      "from the web. The giant moth comes loose from the web, dropping a "\
				      "cartridge in your hand before flying away with its family."


	def get_status(self, type=None):
		if type is None:
			type = "Moth"
		return super().get_status(type)

	def err_message(self, game):
		if game.player.current_room.id == "roomI" and\
		game.player.current_room.is_lit == False:
			say("You don't see a moth.")
			say("But then again you don't really see much of anything...")
			return True
		else:
			return False

	def look(self, game, actionargs):
		if self.err_message(game):
			return

		self.get_desc(game)

	def get_desc(self, game):
		message = self.description
		message += " It seems to be calling out for help... but to who?"

		say(message)

	def spray(self, game, actionargs):
		if self.err_message(game):
			return

		has_debugger = False

		for item in game.player.inventory:
			if item.id == "debugger":
				has_debugger = True
				break

		if has_debugger:
			say(self.msg_spray)

			if self.been_sprayed:
				say(self.msg_been_sprayed)
			else:
				say(self.msg_first_spray)
				self.been_sprayed = True
				game.room_list["roomH"].remove_thing(self)
				game.room_list["roomI"].add_thing(self)
				game.room_list["roomI"].contains_moth = True
				self.in_web = True
				game.thing_list["webDoor"].can_go = True
		else:
			say("You don't have anything to spray the moth with.")

	def spray_with(self, game, actionargs):
		if self.err_message(game):
			return

		obj = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
		
		if obj.id == "debugger":
			self.spray(game, actionargs)
		else:
			say("You cannot spray the moth with that.")

	def kin(self, game, actionargs):
		if self.err_message(game):
			return

		if not self.in_web:
			say(self.msg_kin_not_in_web)
		else:
			say(self.msg_kin_in_web)

			if not self.floppy_received:
				message = "You received a " + self.floppy.name + "!"
				game.player.add_to_inventory(self.floppy)
				self.floppy_received = True
				self.in_web = False
				game.room_list["roomI"].remove_thing(self)
				game.room_list["roomI"].contains_moth = False
				say(message)

	def look_in(self, game, actionargs):
		if not self.err_message(game):
			super().look_in(game, actionargs)

	def read(self, game, actionargs):
		if not self.err_message(game):
			super().read(game, actionargs)

	def open(self, game, actionargs):
		if not self.err_message(game):
			super().open(game, actionargs)

	def close(self, game, actionargs):
		if not self.err_message(game):
			super().close(game, actionargs)

	def take(self, game, actionargs):
		if not self.err_message(game):
			super().take(game, actionargs)

	def drop(self, game, actionargs):
		if not self.err_message(game):
			super().drop(game, actionargs)

	def put_down(self, game, actionargs):
		if not self.err_message(game):
			super().put_down(game, actionargs)

	def give_to(self, game, actionargs):
		if not self.err_message(game):
			super().give_to(game, actionargs)

	def go(self, game, actionargs):
		if not self.err_message(game):
			super().go(game, actionargs)

	def put_in(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "in")

	def put_on(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "on")

	def pull(self, game, actionargs):
		if not self.err_message(game):
			super().pull(game, actionargs)

	def receive_item(self, game, actionargs, prep):
		if not self.err_message(game):
			super().receive_item(game, actionargs, prep)

	def use(self, game, actionargs):
		if not self.err_message(game):
			super().use(game, actionargs)

	def dance(self, game, actionargs):
		if not self.err_message(game):
			super().dance(game, actionargs)

	def eat(self, game, actionargs):
		if not self.err_message(game):
			super().eat(game, actionargs)

	def drink(self, game, actionargs):
		if not self.err_message(game):
			super().drink(game, actionargs)

	def play(self, game, actionargs):
		if not self.err_message(game):
			super().play(game, actionargs)

	def talk(self, game, actionargs):
		if not self.err_message(game):
			super().talk(game, actionargs)

	def hit(self, game, actionargs):
		if not self.err_message(game):
			super().hit(game, actionargs)

	def ram(self, game, actionargs):
		if not self.err_message(game):
			super().ram(game, actionargs)

	def tic(self, game, actionargs):
		if not self.err_message(game):
			super().tic(game, actionargs)

	def sit(self, game, actionargs):
		if not self.err_message(game):
			super().sit(game, actionargs)

class Tape(Item):
	def __init__(self, id, name):
		super().__init__(id, name)

	def get_status(self, type=None):
		if type is None:
			type = "Tape"
		return super().get_status(type)

	def err_message(self, game):
		if game.player.current_room.id == "roomI" and\
		game.player.current_room.is_lit == False:
			say("You don't see a tape.")
			say("Then again you can't really see much of anything...")
			return True
		else:
			return False

	def spray(self, game, actionargs):
		if not self.err_message(game):
			super().spray(game, actionargs)

	def spray_with(self, game, actionargs):
		if not self.err_message(game):
			super().spray_with(game, actionargs)

	def look_in(self, game, actionargs):
		if not self.err_message(game):
			super().look_in(game, actionargs)

	def read(self, game, actionargs):
		if not self.err_message(game):
			super().read(game, actionargs)

	def open(self, game, actionargs):
		if not self.err_message(game):
			super().open(game, actionargs)

	def close(self, game, actionargs):
		if not self.err_message(game):
			super().close(game, actionargs)

	def take(self, game, actionargs):
		if not self.err_message(game):
			super().take(game, actionargs)

	def drop(self, game, actionargs):
		if not self.err_message(game):
			super().drop(game, actionargs)

	def put_down(self, game, actionargs):
		if not self.err_message(game):
			super().put_down(game, actionargs)

	def give_to(self, game, actionargs):
		if not self.err_message(game):
			super().give_to(game, actionargs)

	def go(self, game, actionargs):
		if not self.err_message(game):
			super().go(game, actionargs)

	def put_in(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "in")

	def put_on(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "on")

	def pull(self, game, actionargs):
		if not self.err_message(game):
			super().pull(game, actionargs)

	def receive_item(self, game, actionargs, prep):
		if not self.err_message(game):
			super().receive_item(game, actionargs, prep)

	def use(self, game, actionargs):
		if not self.err_message(game):
			super().use(game, actionargs)

	def dance(self, game, actionargs):
		if not self.err_message(game):
			super().dance(game, actionargs)

	def eat(self, game, actionargs):
		if not self.err_message(game):
			super().eat(game, actionargs)

	def drink(self, game, actionargs):
		if not self.err_message(game):
			super().drink(game, actionargs)

	def play(self, game, actionargs):
		if not self.err_message(game):
			super().play(game, actionargs)

	def talk(self, game, actionargs):
		if not self.err_message(game):
			super().talk(game, actionargs)

	def hit(self, game, actionargs):
		if not self.err_message(game):
			super().hit(game, actionargs)

	def ram(self, game, actionargs):
		if not self.err_message(game):
			super().ram(game, actionargs)

	def kin(self, game, actionargs):
		if not self.err_message(game):
			super().kin(game, actionargs)

	def tic(self, game, actionargs):
		if not self.err_message(game):
			super().tic(game, actionargs)

	def sit(self, game, actionargs):
		if not self.err_message(game):
			super().sit(game, actionargs)

class ShiftyMan(Feature):
	def __init__(self, id, name):
		super().__init__(id, name)

	def get_status(self, type=None):
		if type is None:
			type = "ShiftyMan"
		return super().get_status(type)

	def talk(self, game, actionargs):
		say("There are five DAEMONS in the Tower who stole some very important things from my computer:")
		say("One likes to play pranks.")
		say("One likes to dance - but only likes very fast music.")
		say("One got a job as a bus driver.")
		say("One has been hanging out with a spider.")
		say("One is the Tower custodian, and keeps a strange pet.")

class Spider(Feature):

	def __init__(self, id, name):
		super().__init__(id, name)
		self.msg_spray = "You spray the spider with the Debugger. "\
			    "The spider angrily lunges toward you, and "\
			    "you fall backwards, narrowly avoiding being bitten. "

	def get_status(self, type=None):
		if type is None:
			type = "Spider"
		return super().get_status(type)

	def err_message(self, game):
		if game.player.current_room.id == "roomI" and\
		game.player.current_room.is_lit == False:
			say("You don't see a spider.")
			say("But then again you don't really see much of anything...")
			return True
		else:
			return False

	def spray(self, game, actionargs):
		if self.err_message(game):
			return

		has_debugger = False

		for item in game.player.inventory:
			if item.id == "debugger":
				has_debugger = True
				break

		if has_debugger:
			say(self.msg_spray)
		else:
			say("You don't have anything to spray the spider with.")

	def spray_with(self, game, actionargs):
		if self.err_message(game):
			return

		obj = Utilities.find_by_name(actionargs["iobj"], game.thing_list)
	
		if obj.id == "debugger":
			self.spray(game, actionargs)
		else:
			say("You cannot spray the spider with that.")

	def look_in(self, game, actionargs):
		if not self.err_message(game):
			super().look_in(game, actionargs)

	def read(self, game, actionargs):
		if not self.err_message(game):
			super().read(game, actionargs)

	def open(self, game, actionargs):
		if not self.err_message(game):
			super().open(game, actionargs)

	def close(self, game, actionargs):
		if not self.err_message(game):
			super().close(game, actionargs)

	def take(self, game, actionargs):
		if not self.err_message(game):
			super().take(game, actionargs)

	def drop(self, game, actionargs):
		if not self.err_message(game):
			super().drop(game, actionargs)

	def put_down(self, game, actionargs):
		if not self.err_message(game):
			super().put_down(game, actionargs)

	def give_to(self, game, actionargs):
		if not self.err_message(game):
			super().give_to(game, actionargs)

	def go(self, game, actionargs):
		if not self.err_message(game):
			super().go(game, actionargs)

	def put_in(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "in")

	def put_on(self, game, actionargs):
		if not self.err_message(game):
			super().receive_item(game, actionargs, "on")

	def pull(self, game, actionargs):
		if not self.err_message(game):
			super().pull(game, actionargs)

	def receive_item(self, game, actionargs, prep):
		if not self.err_message(game):
			super().receive_item(game, actionargs, prep)

	def use(self, game, actionargs):
		if not self.err_message(game):
			super().use(game, actionargs)

	def dance(self, game, actionargs):
		if not self.err_message(game):
			super().dance(game, actionargs)

	def eat(self, game, actionargs):
		if not self.err_message(game):
			super().eat(game, actionargs)

	def drink(self, game, actionargs):
		if not self.err_message(game):
			super().drink(game, actionargs)

	def play(self, game, actionargs):
		if not self.err_message(game):
			super().play(game, actionargs)

	def talk(self, game, actionargs):
		if not self.err_message(game):
			super().talk(game, actionargs)

	def hit(self, game, actionargs):
		if not self.err_message(game):
			super().hit(game, actionargs)

	def ram(self, game, actionargs):
		if not self.err_message(game):
			super().ram(game, actionargs)

	def kin(self, game, actionargs):
		if not self.err_message(game):
			super().kin(game, actionargs)

	def tic(self, game, actionargs):
		if not self.err_message(game):
			super().tic(game, actionargs)

	def sit(self, game, actionargs):
		if not self.err_message(game):
			super().tic(game, actionargs)

class Fireplace(Feature):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.look_in_msg = "You look in the fireplace, but "\
				   "you don't see anything other than the "\
				   "burning fire."

	def get_status(self, type=None):
		if type is None:
			type = "Fireplace"
		return super().get_status(type)

	def look_in(self, game, actionargs):
		say(self.look_in_msg)
			
class Freezer(Feature):
	"""Freezer that manipulates chunk of ice"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.is_malfunctioned = False

	def get_status(self, type=None):
		if type is None:
			type = "Freezer"
		return super().get_status(type)

	def tic(self, game, actionargs):
		if not self.is_malfunctioned:
			self.is_malfunctioned = True
			malfunction_text = \
				"The freezer buzzes and groans. It begins to shake before finally turning off. " \
				"The chunk of ice begins to drip, and then crack. Finally, the ice falls apart, and the laptop " \
				"comes crashing down. The screen cracks and the frame gets severely bent upon impact. " \
				"A flashdrive pops out and slides across the floor."
			say(malfunction_text)
			# laptop frozenLaptop -> brokenLaptop -> drop flash drive
			game.player.current_room.remove_thing(game.thing_list["frozenLaptop"])
			game.player.current_room.add_thing(game.thing_list["brokenLaptop"])
			game.player.current_room.add_thing(game.thing_list["flashdrive"])
		else:
			say("Nothing happens.")

	def get_desc(self):
		if self.is_malfunctioned:
			desc_text = "This strange device is labeled as a \"<WRITTEN_TEXT>freezer</>\". " \
						"It is turned off, and there is now a puddle of water next to it."
		else:
			desc_text = "This strange device is labeled as a \"<WRITTEN_TEXT>freezer</>\". " \
						"Is is making a grumbling sound, and cold air is pouring from it. " \
						"It is connected to a small platform on which is a chunk of ice. " \
						"It seems to be keeping it frozen."
		say(desc_text)


class MotherDaemon(Feature):
	def __init__(self, id, name):
		super().__init__(id, name)
		self.talk_msg = \
			"<SPOKEN_TEXT>Greetings. I am the mother of the DAEMON's. " \
			"You've arrived here <CLUE>due to motions<SPOKEN_TEXT> out of your control. " \
			"It is surprising you have made it this far- a great <CLUE>application<SPOKEN_TEXT> of your skills. " \
			"I hope you are <CLUE>quite pleased<SPOKEN_TEXT>. " \
			"You may be upset, and you might think that revenge is a <CLUE>small dish<SPOKEN_TEXT> best served cold. " \
			"But hopefully by now you have at least learned what you truly are...</>"

	def get_status(self, type=None):
		if type is None:
			type = "MotherDaemon"
		return super().get_status(type)

	def talk(self, game, actionargs):
		say(self.talk_msg)

class Storage(Feature):
	"""Thing that can store other things"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.has_contents = True
		self.contents = []
		self.contents_accessible = True
		self.receive_preps = []
		self.contents_accessible_iff_open = True
		self.can_be_opened = False
		self.is_open = True

		self.msg_already_opened = "The {} is already open.".format(self.name)
		self.msg_already_closed = "The {} is already closed.".format(self.name)
		self.msg_open = "You open the {}.".format(self.name)
		self.msg_close = "You close the {}.".format(self.name)
		self.msg_is_closed = "The {} is closed.".format(self.name)
		self.msg_look_in = "You look in the {}.".format(self.name)

	def get_status(self, type=None):
		if type is None:
			type = "Storage"
		return super().get_status(type)

	def receive_item(self, game, item, prep):
		if self.has_contents and prep in self.receive_preps:
			if self.can_be_opened and not self.is_open:
				say(self.msg_is_closed)
			else:
				game.player.remove_from_inventory(item)
				self.add_item(item)
				say("You put the {} {} the {}.".format(item.name, prep, self.name))
		else:
			say("You can't put things {} the {}.".format(prep, self.name))

	def add_item(self, item):
		self.contents.append(item)

	def remove_item(self, item):
		self.contents.remove(item)

	def list_contents(self):
		if self.receive_preps:
			prep = self.receive_preps[0]
		else:
			prep = "in"

		extra_sentence = ""
		# if contents is not empty it returns "True"
		if self.contents and self.contents_accessible:
			extra_sentence = "{} it you see".format(prep).capitalize()
			extra_sentence = " " + extra_sentence
			extra_sentence += Utilities.list_to_words([o.get_list_name() for o in self.contents])
			extra_sentence += "."

		return extra_sentence

	def get_desc(self):
		desc_string = self.description
		desc_string += self.list_contents()

		say(desc_string)

	def get_list_name(self):
		list_string = self.list_name

		if self.receive_preps:
			prep = self.receive_preps[0]
		else:
			prep = "in"

		# if contents is not empty it returns "True"
		if self.contents and self.contents_accessible:
			list_string += " ({} which is".format(prep)
			list_string += Utilities.list_to_words([o.get_list_name() for o in self.contents])
			list_string += ")"

		return list_string

	def open(self, game, actionargs):
		if not self.can_be_opened:
			say(self.msg_cannot_be_opened)
		else:
			if self.is_open:
				say(self.msg_already_opened)
			else:
				self.set_open()
				open_text = self.msg_open
				open_text += self.list_contents()
				say(open_text)

	def set_open(self):
		self.is_open = True
		if self.contents_accessible_iff_open:
			self.contents_accessible = True

	def close(self, game, actionargs):
		if not self.can_be_opened:
			say(self.msg_cannot_be_opened)
		else:
			if not self.is_open:
				say(self.msg_already_closed)
			else:
				self.set_closed()
				say(self.msg_close)

	def set_closed(self):
		self.is_open = False
		if self.contents_accessible_iff_open:
			self.contents_accessible = False

	def look_in(self, game, actionargs):
		if "in" not in self.receive_preps or not self.can_be_opened:
			say(self.msg_cannot_look_in)
		else:
			if self.is_open:
				look_text = self.msg_look_in
				look_text += self.list_contents()
				say(look_text)
			else:
				self.open(game, actionargs)

class Container(Storage):
	"""Things are stored IN the Container
	If the container is CLOSED things inside are NOT accessible.
	If the container is OPEN things inside ARE accessible
	EXAMPLES: Fridge, Chest
	"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_opened = True
		self.is_open = False
		self.receive_preps = ["in"]
		self.contents_accessible = False
		self.contents_accessible_iff_open = True

	def get_status(self, type=None):
		if type is None:
			type = "Container"
		return super().get_status(type)


class Surface(Storage):
	"""Things are stored ON the surface
	Things ARE accessible when on the surface
	EXAMPLES: Table, Shelf"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_opened = False
		self.receive_preps = ["on"]

	def get_status(self):
		return super().get_status("Surface")


class VendingTerminal(Container):
	"""Things are stored IN the Container
	If the container is CLOSED things inside are NOT accessible.
	If the container is OPEN things inside ARE accessible
	EXAMPLES: Fridge, Chest
	"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_receive = False
		self.can_be_opened = False
		self.is_open = True
		self.contents_accessible = True
		self.contents_accessible_iff_open = True
		self.is_listed = True
		self.dispensed = False
		self.ticket = None

	def get_status(self, type=None):
		if type is None:
			type = "VendingTerminal"
		return super().get_status(type)

	def hit(self, game, actionargs):
		if self.dispensed:
			super().hit(game, actionargs)
		else:
			say(
				"You give the vending terminal a smack, but it's not enough to dislodge the ticket. Maybe something with more force...")

	def ram(self, game, actionargs):
		say("You RAM the vending terminal with tremendous force.")
		if self.dispensed:
			super().ram(game, actionargs)
		else:
			self.ticket.dispensed = True
			self.ticket.description = self.ticket.alt_description
			self.dispensed = True
			self.description = self.alt_description
			say(self.msg_rammed)

	def receive_item(self, game, item, prep):
		say("You can't put things {} the {}.".format(prep, self.name))


class Bus(Container):
	"""Not-Takable, Not-Dropable thing"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.can_be_taken = False
		self.can_be_dropped = False
		self.msg_cannot_take = "The {} is fixed in place.".format(self.name)

	def get_status(self, type=None):
		if type is None:
			type = "Bus"
		return super().get_status(type)

	def go(self, game, actionargs):
		say(self.msg_go)
		if game.thing_list["floppyDisk"] in self.contents:
			say("On your way out of the bus, you notice a floppy disk sitting on the driver's seat...")


class Document(Item):
	"""Takable, Dropable thing"""

	def __init__(self, id, name):
		super().__init__(id, name)
		self.file = "binary"


	def get_status(self, type=None):
		if type is None:
			type = "Document"
		return super().get_status(type)

	# ACTION for read
	def read(self, game, actionargs):
		file = open(self.file, "r")

		count = 0
	
		if file.mode == 'r':
			str = file.read()
			str = str.split(" ")

			display_str = ""

			for x in str:
				display_str += x
				count += 1
				if count % 10 == 0:
					say(display_str)
					display_str = ""
				if count % 100 == 0:
					ans = game.get_yn_answer("...Are you sure you want to keep reading? (y/n)")
					if not ans:
						say("That was... useful.")
						break
				if count % 1000 == 0:
					say("You stop reading in spite of yourself, lest you go mad...")
					break


		file.close()
