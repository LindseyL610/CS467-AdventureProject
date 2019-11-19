import Room
import os
import shutil
import json
import datetime
import sys
import parser_class
import Thing
import Player
from Utilities import say
from Verbs_and_Actions import verb_list, action_list, prep_list
import platform

OS = platform.system()

SAVES = "SV"
ROOM_PREFIX = "RM_"
THINGS = "TH"

DEBUG_MODE = True
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
		print("Game has the following console screen size requirements:")
		print("Minimum width: " + str(WIDTH))
		print("Minimum height: " + str(HEIGHT))
		print("Please resize your screen and run the game again!")

	return valid_size

def get_path():
	#NOTE: The following dir_path definition is adapted from: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory#targetText=os.getcwd()%20(returns%20%22,current%20working%20directory%20to%20path%20%22)
	#debug(os.getcwd())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	#debug(dir_path)

	return dir_path

class Game:
	def __init__(self):
		self.action_list = action_list
		self.verb_list = verb_list
		self.game_data = self.load_data_from_file(SAVES)

		self.keywords = set()

		self.quit_selected = False

		self.parser = parser_class.Parser()

		#self.load_room_data()

		self.game_loaded = self.load_menu(True)

		self.new_room = True

	def get_game_dictionary(self):
		dictionary = dict()	

		# for each verb
		for verb in verb_list:
			if verb not in dictionary:
				dictionary[verb] = verb # add the verb to the dict

			for alt_name in verb_list[verb].alternate_names:
				if alt_name not in dictionary:
					dictionary[alt_name] = verb # add each alternate word for the verb to the dict

		# for each preposition
		for prep in prep_list:
			if prep not in dictionary:
				dictionary[prep] = prep # add the preposition to the dict

		things = self.load_data_from_file(THINGS)

		# for each thing
		for thing in things:
			name = things[thing]["data"]["name"] # get the thing's name

			if name not in dictionary:
				dictionary[name] = name # add the name to the dict

			# for each alternate name of the thing
			for alt_name in things[thing]["data"]["alternate_names"]:
				if alt_name not in dictionary:
					dictionary[alt_name] = name # add the alternate name to the dict

			# for each adjective
			for adj in things[thing]["data"]["adjectives"]:
				if adj not in dictionary:
					dictionary[adj] = adj # add the adjective to the dict

		return dictionary

	def get_parts_of_speech_dictionary(self):
		dictionary = dict()

		# for each verb
		for verb in verb_list:
			if verb not in dictionary:
				dictionary[verb] = "verb" # add verb to dict with value "verb"

		# for each preposition
		for prep in prep_list:
			if prep not in dictionary:
				dictionary[prep] = "preposition" # add prep to dict with value "preposition"

		things = self.load_data_from_file(THINGS)

		# for each thing
		for thing in things:
			name = things[thing]["data"]["name"] # get the thing's name

			if name not in dictionary:
				dictionary[name] = "object" # add thing to dict with value "object"

			# for each adjective
			for adj in things[thing]["data"]["adjectives"]:
				if adj not in dictionary:
					dictionary[adj] = "adjective" # add adj to dict with value "adjective"

		return dictionary

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
		self.load_rooms()
		self.load_things()
		
		# Set default status for each room
		for id in self.room_list:
			self.room_list[id].set_status(json.dumps(self.default_rooms[id]), self.thing_list, self.room_list)

		# Set default status for each thing
		for id in self.thing_list:
			self.thing_list[id].set_status(json.dumps(self.default_things[id]), self.thing_list, self.room_list)

		# Create a new player --for now this is just a generic object
		player_obj = self.game_data["default"]["player"].copy()		
		player_obj["name"] = input("Enter your name: ")
		self.player = Player.Player()
		self.player.set_status(json.dumps(player_obj), self.thing_list, self.room_list)

		# These are data attributes for the saved game --currently not saved
		self.current_save = None #index of game in "saves" list
		self.timestamp = None #timestamp for when game was last saved		


	def load_rooms(self, rooms=None):
		self.room_list = dict()

		if rooms is None:
			self.default_rooms = dict()

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

				id = data["id"]
				name = data["name"]

				self.default_rooms[id] = data

				self.room_list[id] = Room.Room(id, name)

		else:
			for room in rooms:
				data = rooms[room]
				id = data["id"]
				name = data["name"]
				self.room_list[id] = Room.Room(id, name)

	def load_things(self, things=None):
		self.thing_list = dict()

		if things is None:
			things = self.load_data_from_file(THINGS)
			self.default_things = dict()

		else:
			self.default_things = None

		# for each object
		for thing in things:
			# get the object type
			type = things[thing]["type"]

			# get the object data
			data = things[thing]["data"]

			# get the object id (and add ID to ID index for color output)
			id = data["id"]
			name = data["name"]
			self.keywords.add(name)

			if self.default_things is not None:
				self.default_things[id] = data

			# Call the appropriate constructor for the object type
			if type == "exit":
				self.thing_list[id] = Thing.Exit(id, name)
			elif type == "door":
				self.thing_list[id] = Thing.Door(id, name)
			elif type == "item":
				self.thing_list[id] = Thing.Item(id, name)
			elif type == "floppy":
				self.thing_list[id] = Thing.Floppy(id, name)
			elif type == "feature":
				self.thing_list[id] = Thing.Feature(id, name)
			elif type == "input":
				self.thing_list[id] = Thing.Input(id, name)
			elif type == "sign":
				self.thing_list[id] = Thing.Sign(id, name)
			elif type == "storage":
				self.thing_list[id] = Thing.Storage(id, name)
			elif type == "container":
				self.thing_list[id] = Thing.Container(id, name)
			elif type == "surface":
				self.thing_list[id] = Thing.Surface(id, name)


	def load_saved_game(self, id):
		debug("load_saved_game()")

		self.load_rooms(self.game_data["saves"][id]["data"]["room_list"])
		self.load_things(self.game_data["saves"][id]["data"]["thing_list"])

		# Set status for each room
		for room in self.room_list:
			self.room_list[room].set_status(json.dumps(self.game_data["saves"][id]["data"]["room_list"][room]), self.thing_list, self.room_list)

		# Set status for each thing
		for thing in self.thing_list:
			self.thing_list[thing].set_status(json.dumps(self.game_data["saves"][id]["data"]["thing_list"][thing]), self.thing_list, self.room_list)

		# Load player object from saved game data based on ID
		player_obj = self.game_data["saves"][id]["data"]["player"]
		self.player = Player.Player()
		self.player.set_status(json.dumps(player_obj), self.thing_list, self.room_list)

		# These are data attributes for the saved game 
		self.current_save = id #index of game in "saves" list
		self.timestamp = self.game_data["saves"][id]["time"]

	def save_game(self):
		data = dict()

		new_save = dict()

		# Get the game data that is going to be saved
		data["player"] = json.loads(self.player.get_status())
		
		data["room_list"] = dict()
		for id in self.room_list:
			data["room_list"][id] = json.loads(self.room_list[id].get_status())
		
		data["thing_list"] = dict()
		for id in self.thing_list:
			data["thing_list"][id] = json.loads(self.thing_list[id].get_status())

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
		json.dump(self.game_data, f)
		f.close()
	
		say("Game saved!")

	def prompt(self):
		#debug("\ncurrent room: " + str(self.player.current_room.id))
		#debug("room state: " + str(self.room_list[self.player.current_room.id].get_status()))
		#debug("player: " + str(self.player.get_status()))

		if self.new_room:
			#NOTE: The following clear screen code adapted from: https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
			if OS == "Windows":
				os.system('cls')  # For Windows
			elif OS == "Linux" or OS == "Darwin":
				os.system('clear')  # For Linux/OS X
			
			self.room_list[self.player.current_room.id].get_description()
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
				self.say("Invalid input!")

		if input_str == "y":
			self.save_game()

		self.quit_selected = True

	def play(self):
		while not self.quit_selected:
			self.prompt()




if valid_width():
	game = Game()
	if game.game_loaded:
		game_dict = game.get_game_dictionary()
		speech_dict = game.get_parts_of_speech_dictionary()

		print("\nGame dictionary:")
		for x, y in game_dict.items():
			print(x, y)

		print("\nParts of speech dictionary:")
		for x, y in speech_dict.items():
			print(x, y)

#game = Game()
#debug(game.__dict__)
#debug(game.player.__dict__)


#game.save_game()
