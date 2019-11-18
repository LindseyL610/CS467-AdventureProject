from Utilities import say
import Utilities
import Room
import Thing
import json

class Player:

	def __init__(self):
		"""Initialize player"""
		self.name = "NAME"
		self.inventory = []
		self.current_room = None	# Room

	def get_status(self):
		"""returns the status of player in JSON format"""
		
		# Returns the appropriate export value based on whether value is a Room or Thing
		def get_export_value(value):
			if isinstance(value, Room.Room):
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
			if value.find("<R:") == 0:
				list = room_list
			elif value.find("<T:") == 0:
				list = thing_list
			else:
				list = None

			if list is not None:
				id = value[3:(value.find(">"))]
				return list[id]

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

	def add_to_inventory(self, thing):
		"""removes an item from the player inventory"""
		# place holder message
		say("[[player removes {} from inventory]]".format(thing.name))
		# remove thing from inventory
		self.inventory.append(thing)

	def remove_from_inventory(self, thing):
		"""removes an item from the player inventory"""
		# place holder message
		say("[[player removes {} from inventory]]".format(thing.name))
		# remove thing from inventory
		self.inventory.remove(thing)

	def take(self, thing):
		"""Remove an item from the environment and add it to your inventory"""
		# place holder message
		say("[[player takes {}]]".format(thing.name))

		# remove thing from its current location (room or storage)
		self.current_room.remove_thing(thing)
		# add thing to inventory
		self.add_to_inventory(thing)

	def drop(self, thing):
		"""Drop an item in the players inventory and leave it in the current room"""
		# place holder message
		say("[[player drops {}]]".format(thing.name))
		# remove thing from inventory (can use player.remove_from_inventory)
		self.remove_from_inventory(thing)
		# add thing to current room contents (use room.add_thing())
		self.current_room.add_thing(thing)

	def go(self, destination):
		"""changes the location of the player, and displays description
		of new destination"""
		# place holder message
		say("[[player goes to room {}]]".format(destination.name))
		self.current_room = destination
		destination.get_description()


	def is_in_inventory(self, thing):
		"""returns whether or not the given thing is in the Player's inventory
		thing: the object itself (not the id?)
		"""
		return thing in self.inventory