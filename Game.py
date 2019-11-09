import Room
import os
import platform
import shutil
import json
import datetime
import sys
import parser_class
import Exit
import Feature
import textwrap

OBJECTS = "OB"
SAVES = "SV"
ROOM_PREFIX = "RM_"

DEBUG_MODE = False
WIDTH = 100
HEIGHT = 30


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

def valid_width():
	valid_size = False

	#NOTE: The following code is adapted from: http://granitosaurus.rocks/getting-terminal-size.html
	columns, rows = shutil.get_terminal_size(fallback=(80, 24))

	debug("Columns: " + str(columns))
	debug("Rows: " + str(rows))

	if columns >= WIDTH:
		valid_size = True
	else:
		print("Minimum width: " + str(WIDTH))
		print("Minimum height: " + str(HEIGHT))

	return valid_size

def get_path():
	#NOTE: The following dir_path definition is adapted from: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory#targetText=os.getcwd()%20(returns%20%22,current%20working%20directory%20to%20path%20%22)
	#debug(os.getcwd())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	#debug(dir_path)

	return dir_path

class Game:
	def __init__(self):
		self.quit_selected = False

		self.parser = parser_class.Parser()

		self.object_data = self.load_data_from_file(OBJECTS)
		self.game_data = self.load_data_from_file(SAVES)
		self.load_room_data()

		self.game_loaded = self.load_menu(True)

		self.wrapper = textwrap.TextWrapper()

		self.new_room = True

	def load_data_from_file(self, file_name):
		file = open(file_name, "r")
		
		if file.mode is 'r':
			data = json.load(file)

		file.close()

		return data

	def load_menu(self, initial):
		i = 1

		load_names = dict()

		for save in self.game_data["saves"]:
			name = self.game_data["saves"][save]["data"]["player"]["name"]
			time = self.game_data["saves"][save]["time"]

			display = name + ", " + time

			display_obj = dict()

			display_obj["display"] = display
			display_obj["id"] = save

			load_names[str(i)] = display_obj.copy()
			i += 1

		if not initial and len(load_names) is 0:
			print("No saved games found!")
			return

		create_idx = str(len(load_names))
		quit_idx = str(len(load_names)+1)

		if initial:
			print("Select a saved game to load, or create a new game.")
		else:
			print("Select a saved game to load.")

		for i in load_names:
			print(i + ". " + load_names[i]["display"])

		if initial:
			create_idx = str(len(load_names)+1)
			quit_idx = str(len(load_names)+2)
			max = len(load_names)+2
			print(create_idx + ". Create New Game")
			print(quit_idx + ". Quit")

		else:
			back_idx = str(len(load_names)+1)
			max = len(load_names)+1
			print(back_idx + ". Go back")

		selection = self.validate_input(1, max)

		if initial:
			if int(selection) is (max-1):
				debug("creating new game")
				self.create_new_game()
				return True
		
		if int(selection) is max:
				return False

		debug("loading saved game: " + str(load_names[selection]["display"]))
		self.load_saved_game(load_names[selection]["id"])

		return True

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

	def create_new_game(self):
		# Create a new player --for now this is just a generic object
		self.player = {}
		self.player["name"] = input("Enter your name: ")

		# These are data attributes for the saved game --currently not saved
		self.current_save = None #index of game in "saves" list
		self.timestamp = None #timestamp for when game was last saved
		
		# Here the default game state data is loaded
		self.state = self.game_data["default"].copy()

		# Load up instances of all objects for a new game
		self.construct_all_objects(True)

	def load_room_data(self):
		#get room file names
		filenames = list()
		files = os.listdir(get_path())

		for name in files:
			if name.find(ROOM_PREFIX) is 0:
				filenames.append(name)

		#for each room file
		for room_file in filenames:
			#retrieve data from room file
			data = self.load_data_from_file(room_file)

			#append data to object_data
			self.object_data.append(data)

	def construct_all_objects(self, new):
		self.objects = dict()
		
		# for each object
		for object in self.object_data:
			# get the object type
			type = object["type"]

			# get the object data
			data = object["data"]

			# get the object id
			id = data["id"]

			# if this is a new game
			if new:
				# use the default state provided in the object data
				state = object["default_state"]
			# if this game is loaded from a saved game
			else:
				# use the saved state data
				state = self.game_data["saves"][self.current_save]["data"]["object_state"][id].copy()

			# construct an instance of that object
			self.objects[id] = self.construct_single_object(type, data, state)

	def construct_single_object(self, type, data, state):
		ret_obj = None
		
		# Call the appropriate constructor for the object type
		if type == "room":
			ret_obj = Room.Room(data, state)
		elif type == "exit":
			ret_obj = Exit.Exit(data, state)
		elif type == "feature":
			ret_obj = Feature.Feature(data, state)

		return ret_obj

	def load_saved_game(self, id):
		debug("load_saved_game()")

		# Load player object from saved game data based on ID
		self.player = self.game_data["saves"][id]["data"]["player"].copy()

		# These are data attributes for the saved game 
		self.current_save = id #index of game in "saves" list
		self.timestamp = self.game_data["saves"][id]["time"]
		
		# Here the saved game state data is loaded
		self.state = self.game_data["saves"][id]["data"]["game_state"].copy()

		# Load up instances of all objects for the saved game
		self.construct_all_objects(False)

	def save_game(self):
		data = dict()

		new_save = dict()

		# Get the game data that is going to be saved
		data["player"] = self.player.copy()
		data["game_state"] = self.state.copy()
		data["object_state"] = {}

		# For each object
		for obj in self.objects:
			# Add object state data
			data["object_state"][obj] = self.objects[obj].get_state_data().copy()

		# if this is a game that hasn't been previously saved
		if self.current_save is None:
			# assign a new save ID
			self.current_save = self.game_data["save_ctr"]
			
			# increment the save ID counter
			self.game_data["save_ctr"] += 1

		# write or overwrite the game data into the saves list
		self.game_data["saves"][str(self.current_save)] = {}
		self.game_data["saves"][str(self.current_save)]["data"] = data.copy()
		self.game_data["saves"][str(self.current_save)]["time"] = str(datetime.datetime.now()).replace(":", "-")
	
		# write the game data to the save file
		f = open (SAVES, "w")

		f.truncate(0)
		f.write(json.dumps(self.game_data))
		f.close()
	
		print("Game saved!")

	def get_current_room(self):
		return self.state["current_room"]

	def go(self, direction):
		origin = self.get_current_room()
		exits = self.objects[origin].data["exits"].copy()

		if exits[direction] is not None:
			if self.objects[exits[direction]].state["locked"]:
				print("That exit is locked!")
				return

			for room in self.objects[exits[direction]].data["rooms"]:
				if not (room == origin):
					destination = room

			self.state["current_room"] = destination
			print("You travel " + direction + " through the " + exits[direction] + ".")
			self.new_room = True

		else:
			print ("There is nowhere to go in that direction!")

	# checks if item is in the room, and if so, removes it from the room and adds to the bag
	def take_item(self, item):
		if self.objects[self.get_current_room()].check_item(item):
			#remove item from room
			self.objects[self.get_current_room()].remove_item(item)

			#put item in bag
			self.state["bag"].append(item)

			print("The " + item + " is now in your bag.")

			return True

		else:
			print("You can't take the " + item + "!")

			return False

	# checks if item is in inventory and if so, removes it and adds it to the current room
	def drop_item(self, item):
		if item in self.state["bag"]:
			self.objects[self.get_current_room()].add_dropped_item(item)
			self.state["bag"].remove(item)
			print("You dropped the " + item + " in the " + self.get_current_room() + ".")

			return True

		else:
			print("You don't have the " + item + "!")

			return False

	def prompt(self):
		debug("\ncurrent room: " + str(self.get_current_room()))
		debug("room state: " + str(self.objects[self.get_current_room()].get_state_data()))
		debug("game: " + str(self.state))

		if self.new_room:
			#NOTE: The following clear screen code adapted from: https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
			if platform.system() == "Windows":
				os.system('cls')  # For Windows
			elif platform.system() == "Linux" or platform.system() == "Darwin":
				os.system('clear')  # For Linux/OS X
			self.say(self.objects[self.get_current_room()].get_prompt(self))
			self.new_room = False

		input_str = input("> ")
		self.parser.parse_input(self, input_str)


	def quit(self):
		valid_input = False
		input_str = ""

		while not valid_input:
			input_str = input("Do you want to save before you quit? (y/n) ")

			if input_str == "y" or input_str == "yes":
				input_str = "y"
				valid_input = True
			elif input_str == "n" or input_str == "no":
				input_str = "n"
				valid_input = True
			else:
				print("Invalid input!")

		if input_str == "y":
			self.save_game()

		self.quit_selected = True

	def play(self):
		while not self.quit_selected:
			self.prompt()

#def say(self, text):
def say(text):

	keywords = {"one", "two", "three"}
		
	color_code = "\033[1;32;40m"
	default_code = "\033[0m"

	#find each instance of each key word
	for word in keywords:
		start_idx = 0
		start = 0

		while start is not -1:
			start = text.find(word, start_idx)
			end = start + len(word) - 1

			#insert color cords before and after each instance
			if start is not -1:
				text = text[0:start] + color_code + word + default_code + text[end+1:]

			start_idx = text.find(word,start_idx) + len(word)

	#print(self.wrapper.fill(text))
	wrapper = textwrap.TextWrapper()
	print(wrapper.fill(text))

#if valid_width():
#	game = Game()
#	if game.game_loaded:
#		game.play()

test_string = "This sentence has keyword one and keyword two. This next sentence has kewyord three. And here is a repeat of one."
say(test_string)

#game = Game()
#debug("game data= " + str(game.game_data))
#debug("object data= " + str(game.object_data))
#debug("player= " + str(game.player))
#debug("current save= " + str(game.current_save))
#debug("state= " + str(game.state))
#debug("objects= " + str(game.objects))

#game.save_game()
#debug("game data= " + str(game.game_data))
#debug("object data= " + str(game.object_data))
#debug("player= " + str(game.player))
#debug("current save= " + str(game.current_save))
#debug("state= " + str(game.state))
#debug("objects= " + str(game.objects))

#game.play()
