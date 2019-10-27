import Room
import os
import json
import datetime
import sys

ROOM = "RM_"
SAVE = "SV_"
EXIT = "EX_"
FEATURE = "FE_"

DEBUG_MODE = True
DEFAULT = "config"

def toggle_debug(input):
	global DEBUG_MODE

	# NOTE: The following try/except block is adapted from: https://pynative.com/python-check-user-input-is-number-or-string/
	try:
		#Turn debug mode on or off
		if int(input) == 999:
			if not DEBUG_MODE:
				DEBUG_MODE = True
				print ("Debug mode turned ON.")
			else:
				DEBUG_MODE = False
				print ("Debug mode turned OFF.")
		else:
			return False
	except ValueError:
		return False

	return True

def debug(output):
	if DEBUG_MODE is True:
		print(output)


class Game:
	def __init__(self):
#		for room in self.rooms:
#			print("id= " + self.rooms[room].id)
#			print("long_description= " + self.rooms[room].long_description)
#			print("short_description= " + self.rooms[room].short_description)
#			print("exits= " + str(self.rooms[room].exits))
#			print("actions= " + str(self.rooms[room].actions))
#			print("status= " + str(self.rooms[room].status))

		self.rooms = self.load_rooms()

		self.load_menu(True)


	def load_data_from_file(self, file_name):
		file = open(file_name, "r")
		
		if file.mode is 'r':
			data = json.load(file)

		file.close()

		return data


	def get_file_names(self, type):
		type_files = list()
	
		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name.find(type) is 0:
				type_files.append(name)

		return type_files

	def get_object_names(self, type):
		object_names = list()

		files = self.get_file_names(type)

		for name in files:
			object_names.append(name[3:])

		return object_names

	def validate_input(self, min, max):
		global DEBUG_MODE
		valid_input = False

		selection = input ("> ")

		# Validate input and activate debug mode
		while not valid_input:
			# NOTE: The following try/except block is adapted from: https://pynative.com/python-check-user-input-is-number-or-string/
			try:
				if int(selection) < min or int(selection) > max:
					#Turn debug mode on or off
					if not toggle_debug(selection):
						print("Invalid selection.")

					selection = input("> ")
				else:
					valid_input = True
			except ValueError:
				print("Invalid selection.")
				selection = input("> ")

		return selection

	def load_menu(self, initial):
		i = 1
		load_names = self.get_object_names(SAVE)

		if not initial and len(load_names) is 0:
			print("No saved games found!")
			return

		if initial:
			print("Select a saved game to load, or create a new game.")
		else:
			print("Select a saved game to load.")

		for name in load_names:
			print(str(i) + ". " + name)
			i = i + 1

		if initial:
			print(str(i) + ". Create New Game")
			i = i + 1
			print(str(i) + ". Quit")
		else:
			print(str(i) + ". Go back")

		selection = self.validate_input(1, i)

		if initial:
			if int(selection) is (i-1):
				self.create_new_game()
				return True
		
		if int(selection) is i:
				return False

		idx = int(selection) - 1
		debug("loading saved game: " + str(load_names[idx]))
		self.load_saved_game(load_names[idx])

		return True

	def load_saved_game(self, load_name):
		debug("load_saved_game()")

		files = self.get_file_names(SAVE)
		debug(files)

		for name in files:
			if name.find(load_name) is 3:
				debug("matching file: " + name)
				match = name

		if match:
			#NOTE: The following file read functionality was adapted from: https://www.guru99.com/reading-and-writing-files-in-python.html#3
			f = open(match, "r")
			if f.mode is 'r':
				data = self.load_data_from_file(match)
				self.current_file = match
			f.close()
			print("Game loaded!")
		else:
			print("Error loading game file!")
			return

		self.user_name = data['user_name']
		self.current_room = data['current_room']
		self.bag = data['bag'].copy()

		for room in data["rooms"]:
			self.rooms[room].set_state(data["rooms"][room])

		#debug("user_name=" + user_name)
		#debug("new_game=" + str(new_game))
		#debug("game_data=" + game_data)
		#debug("current_file=" + current_file)


	def create_new_game(self):
		data = self.load_data_from_file(DEFAULT)
		self.current_file = None

		self.user_name = input("Enter your name: ")
		self.current_room = data['start_room']
		self.bag = list()
		
		for room in self.rooms:
			self.rooms[room].set_state(None)

	def load_rooms(self):
		rooms = dict()
				
		room_names = self.get_object_names(ROOM)

		for name in room_names:
			rooms[name] = Room.Room(name)

		return rooms

	def save_game(self):

		data = dict()

		data["user_name"] = self.user_name
		data["current_room"] = self.current_room
		data["bag"] = self.bag.copy()

		data["rooms"] = dict()
		for room in self.rooms:
			data["rooms"][room] = self.rooms[room].state.copy()

		new_filename = "SV_" + self.user_name + ", " + str(datetime.datetime.now()).replace(":", "-")
	
		if self.current_file is None:
			retrieve_file = new_filename
			new_game = True
		else:
			retrieve_file = self.current_file
			new_game = False

		f = open (retrieve_file, "w")

		f.truncate(0)
		f.write(json.dumps(data))
		f.close()
	
		if not new_game:
			os.rename(retrieve_file, new_filename)

		self.current_file = new_filename
		print("Game saved!")


	def go(self, direction):
		origin = self.current_room
		exits = self.rooms[origin].exits

		if exits[direction] is not None:
			for room in exits[direction].rooms:
				if not (room == origin):
					destination = room

			self.current_room = destination
			print("You travel " + direction + " through the " + exits[direction].id + ".")

		else:
			print ("There is nowhere to go in that direction!")

	# checks if item is in the room, and if so, removes it from the room and adds to the bag
	def take_item(self, item):
		if self.rooms[self.current_room].check_item(item):
			#remove item from room
			self.rooms[self.current_room].remove_item(item)

			#put item in bag
			self.bag.append(item)

			print("The " + item + " is now in your bag.")

			return True

		else:
			print("You can't take the " + item + "!")

			return False

	# checks if item is in inventory and if so, removes it and adds it to the current room
	def drop_item(self, item):
		if item in self.bag:
			self.rooms[self.current_room].add_dropped_item(item)
			self.bag.remove(item)
			print("You dropped the " + item + " in the " + self.current_room + ".")

			return True

		else:
			print("You don't have the " + item + "!")

			return False

	def prompt(self):
		debug("current room: " + str(self.current_room))
		debug("room state: " + str(self.rooms[self.current_room].state))
		debug("bag: " + str(self.bag))

		print(self.rooms[self.current_room].get_prompt())
		input_str = input("> ")

		return input_str



game = Game()

#Test moving from room to room
while True:
	game.go(game.prompt())





#Test take item
#while True:
	#game.take_item(game.prompt())

#Test drop item
#game.take_item("default_item1")
#while True:
	#game.drop_item(game.prompt())

#game.save_game()

