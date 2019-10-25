import Room
import os
import json
import datetime
import sys

ROOM = "RM_"
SAVE = "SV_"
EXIT = "EX_"
DEBUG_MODE = True

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
		self.rooms = self.load_rooms()

#		for room in self.rooms:
#			print("id= " + self.rooms[room].id)
#			print("long_description= " + self.rooms[room].long_description)
#			print("short_description= " + self.rooms[room].short_description)
#			print("exits= " + str(self.rooms[room].exits))
#			print("actions= " + str(self.rooms[room].actions))
#			print("status= " + str(self.rooms[room].status))

		self.load_menu(True)

		print(str(self.rooms))

		print(str(self.current_room))

	def load_data_from_file(self, file_name):
		file = open(file_name, "r")
		
		if file.mode is 'r':
			data = json.load(file)

		file.close()

		self.user_name = data['user_name']
		self.current_room = data['current_room']


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
				self.load_data_from_file(match)
				self.current_file = match
			f.close()
			print("Game loaded!")
		else:
			print("Error loading game file!")
			return

		#debug("user_name=" + user_name)
		#debug("new_game=" + str(new_game))
		#debug("game_data=" + game_data)
		#debug("current_file=" + current_file)


	def create_new_game(self):
		#NOTE: Globals need to be removed once Game class is implemented
		global user_name
		global new_game
		global game_data

		self.user_name = input("Enter your name: ")
		time = str(datetime.datetime.now())

		self.load_data_from_file("config")

	def load_rooms(self):
		rooms = dict()
				
		room_names = self.get_object_names(ROOM)

		for name in room_names:
			rooms[name] = Room.Room(name)

		return rooms

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


	def prompt(self):
		if not self.rooms[self.current_room].status['visited']:
			print(self.rooms[self.current_room].long_description)
		else:
			print(self.rooms[self.current_room].short_description)

		input_str = input("> ")

		return input_str




game = Game()

while True:
	game.go(game.prompt())