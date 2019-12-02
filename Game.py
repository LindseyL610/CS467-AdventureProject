import Room
import os
import shutil
import json
import datetime
import sys
import parser_class
import Thing
import Player
from Utilities import say, find_by_name
from Verbs_and_Actions import verb_list, action_list, prep_list
import platform

OS = platform.system()

SAVES = "SV"
ROOM_PREFIX = "RM_"
THINGS = "TH"

DEBUG_MODE = False
WIDTH = 100
HEIGHT = 50

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

def valid_screen_size():
	valid_size = False

	#NOTE: The following code is adapted from: http://granitosaurus.rocks/getting-terminal-size.html
	columns, rows = shutil.get_terminal_size(fallback=(80, 24))

	debug("Columns: " + str(columns))
	debug("Rows: " + str(rows))

	if columns >= WIDTH and rows >= HEIGHT:
		valid_size = True
	else:
		print("Game has the following console screen size requirements:")
		print("Minimum width: " + str(WIDTH))
		print("Minimum height: " + str(HEIGHT))
		print("Your current width: " + str(columns))
		print("Your current height: " + str(rows))
		print("Please resize your screen and run the game again!")

	return valid_size

def get_path():
	#NOTE: The following dir_path definition is adapted from: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory#targetText=os.getcwd()%20(returns%20%22,current%20working%20directory%20to%20path%20%22)
	#debug(os.getcwd())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	#debug(dir_path)

	return dir_path

def intro():
	print()

	#Graphic display only supported on Linux/Mac
	if OS == "Linux" or OS == "Darwin":
		file = open("model", "r")
		
		for line in file:
			print(line, end="")

		file.close()

		print()
		say("Main Menu")
	else:
		say("Tower Escape - Main Menu")

	any = input("Press any key to continue...")

class Game:
	def __init__(self):
		self.action_list = action_list
		self.verb_list = verb_list
		self.game_data = self.load_data_from_file(SAVES)

		self.keywords = set()

		self.end_game = False

		self.parser = parser_class.Parser(self)

		#self.load_room_data()

		self.game_loaded = self.load_menu(True)

		self.new_room = True

		self.direction_list = ["north", "east", "south", "west", "up", "down"]

		self.find_by_name = find_by_name

	def get_word_answer(self, prompt, answer):
		# displays the prompt
		# gets input from player
		# compares input to answer, and returns True or False if it matches
		# matches should ignore case? or extra whitespace?
		# NOTE I included the prompt in case we want to re-display the prompt after an invalid input
		say(prompt)
		input_str = input("> ")

		input_str_lc = input_str.lower()
		answer_lc = answer.lower()

		input_words = input_str_lc.split()
		answer_words = answer_lc.split()

		print()

		if input_words == answer_words:
			return True
		else:
			return False


	def get_yn_answer(self, prompt):
		# displays the prompt
		# gets a yes or no from the player
		# returns True for yes, False for no
		# NOTE I included the prompt in case we want to re-display the prompt after an invalid input
		# NOTE2 it would probably make sense to have the other y/n questions in the game options use the same method
		valid_input = False
		input_str = ""

		while not valid_input:
			say(prompt)
			input_str = input("> ")

			if input_str.lower() == "y" or input_str.lower() == "yes":
				ret_val = True
				valid_input = True
			elif input_str.lower() == "n" or input_str.lower() == "no":
				ret_val = False
				valid_input = True
			else:
				say("Invalid input!")

		print()
		
		return ret_val

	def get_thing_by_name(self, thing_name, must_be_in_inventory):
		# first, look for thing with given name in player inventory
		# default_thing = Utilities.find_by_name()
		thing_in_inventory = self.find_by_name(thing_name, self.player.inventory)
		if(thing_in_inventory != None):
			#found it
			return thing_in_inventory
		else:
			if(must_be_in_inventory):
				default_thing = self.find_by_name(thing_name, self.thing_list)
				say("You don't have {}.".format(default_thing.list_name))
				return None
			else:
				# look in room's accessible contents:
				thing_in_room = self.find_by_name(thing_name, self.player.current_room.get_all_accessible_contents())
				if(thing_in_room != None):
					# found it
					return thing_in_room
				else:
					default_thing = self.find_by_name(thing_name, self.thing_list)
					say("You don't see {}.".format(default_thing.list_name))
					return None	

	def get_game_dictionary(self):
		dictionary = self.add_directions(0)

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

		# for each room

		#get room file names
		filenames = list()
		files = os.listdir(get_path())

		for name in files:
			if name.find(ROOM_PREFIX) == 0:
				filenames.append(name)

		#for each room file
		for room_file in filenames:
			#retrieve data from room file
			data = self.load_data_from_file(room_file)["data"]

			room_name = data["name"]

			if room_name not in dictionary:
				dictionary[room_name] = room_name

		return dictionary

	def get_parts_of_speech_dictionary(self):
		dictionary = self.add_directions(1)

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

	def add_directions(self, speech_dict):
		directions = [ "north", "south", "east", "west" ]
		dictionary = dict()

		for direction in directions:
			if speech_dict == 0:
				dictionary[direction] = direction
			else:
				dictionary[direction] = "direction"

		return dictionary

	# Gets a list containing the name and alternate names of each exit
	def get_all_exits(self):
		exits = list()

		things = self.load_data_from_file(THINGS)

		# For each thing
		for thing in things:
			thing_type = things[thing]["type"] # Get the type of the thing

			# If the thing is an exit
			if thing_type.lower() == "exit":
				name = things[thing]["data"]["name"] # Get the thing's name
				
				if name not in exits:
					exits.append(name) # Add the name of the exit to "exits"

				# For each alternate name of the exit
				for alternate_name in things[thing]["data"]["alternate_names"]:
					if alternate_name not in exits:
						exits.append(alternate_name) # Add the alternate name to "exits"

		return exits

	def load_data_from_file(self, file_name):
		file = open(file_name, "r")
		
		if file.mode == 'r':
			data = json.load(file)

		file.close()

		return data

	def load_menu(self, initial):
		i = 1

		load_names = dict()

		for save in self.game_data["saves"]:
			name = self.game_data["saves"][save]["data"]["player"]["name"]
			time = self.game_data["saves"][save]["timestamp"]

			display = name + ", " + time

			display_obj = dict()

			display_obj["display"] = display
			display_obj["id"] = save

			load_names[str(i)] = display_obj.copy()
			i += 1

		if not initial and len(load_names) == 0:
			print("No saved games found!")
			return

		create_idx = str(len(load_names))
		quit_idx = str(len(load_names)+1)

		if initial:
			print("Select a saved game to load, or create a new game.")
		else:
			# If this is not the first game being loaded, ask user if they are sure
			if not self.get_yn_answer("Any unsaved progress will be lost. Are you sure you want to load a different game? (y/n) "):
				return False

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
		print()
		say("Game loaded!")
		print()
		#any = input("Press any key to continue...")

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
		
		self.game_time = None

	def advance_time(self):
		time = self.game_time

		if time is None:
			time = 0
		else:
			time += 1
			if time > 12:
				time = 1

		self.game_time = time

	def load_rooms(self, rooms=None):
		self.room_list = dict()

		if rooms is None:
			self.default_rooms = dict()

			#get room file names
			filenames = list()
			files = os.listdir(get_path())

			for name in files:
				if name.find(ROOM_PREFIX) == 0:
					filenames.append(name)

			#for each room file
			for room_file in filenames:
				#retrieve data from room file
				data = self.load_data_from_file(room_file)["data"]
				type = self.load_data_from_file(room_file)["type"]

				id = data["id"]
				name = data["name"]
				self.keywords.add(name)

				self.default_rooms[id] = data

				self.room_list[id] = getattr(Room, type)(id, name)
		else:
			for room in rooms:
				data = rooms[room]["data"]
				type = rooms[room]["type"]

				id = data["id"]
				name = data["name"]
				self.keywords.add(name)

				self.room_list[id] = getattr(Room, type)(id, name)

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

			# if type == "exit":
			# 	self.thing_list[id] = Thing.Exit(id, name)
			# elif type == "door":
			# 	self.thing_list[id] = Thing.Door(id, name)
			# elif type == "item":
			# 	self.thing_list[id] = Thing.Item(id, name)
			# elif type == "floppy":
			# 	self.thing_list[id] = Thing.Floppy(id, name)
			# elif type == "feature":
			# 	self.thing_list[id] = Thing.Feature(id, name)
			# elif type == "input":
			# 	self.thing_list[id] = Thing.Input(id, name)
			# elif type == "sign":
			# 	self.thing_list[id] = Thing.Sign(id, name)
			# elif type == "storage":
			# 	self.thing_list[id] = Thing.Storage(id, name)
			# elif type == "container":
			# 	self.thing_list[id] = Thing.Container(id, name)
			# elif type == "surface":
			# 	self.thing_list[id] = Thing.Surface(id, name)

			# This line assumes "type" is the exact name of the constructor for the Thing
			# NOTE this will fail if the type does not match a constructor;
			# we could consider using hasattr to verify an existing type
			self.thing_list[id] = getattr(Thing, type)(id, name)

	def load_saved_game(self, id):
		debug("load_saved_game()")

		self.load_rooms(self.game_data["saves"][id]["data"]["room_list"])
		self.load_things(self.game_data["saves"][id]["data"]["thing_list"])

		# Set status for each room
		for room in self.room_list:
			self.room_list[room].set_status(json.dumps(self.game_data["saves"][id]["data"]["room_list"][room]["data"]), self.thing_list, self.room_list)

		# Set status for each thing
		for thing in self.thing_list:
			self.thing_list[thing].set_status(json.dumps(self.game_data["saves"][id]["data"]["thing_list"][thing]["data"]), self.thing_list, self.room_list)

		# Load player object from saved game data based on ID
		player_obj = self.game_data["saves"][id]["data"]["player"]
		self.player = Player.Player()
		self.player.set_status(json.dumps(player_obj), self.thing_list, self.room_list)

		# These are data attributes for the saved game 
		self.current_save = id #index of game in "saves" list
		self.timestamp = self.game_data["saves"][id]["timestamp"]

		# Load game time
		self.game_time = self.game_data["saves"][id]["game_time"]

		self.new_room = True


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
		self.game_data["saves"][str(self.current_save)]["timestamp"] = str(datetime.datetime.now()).replace(":", "-")
		self.game_data["saves"][str(self.current_save)]["game_time"] = self.game_time
	
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
			self.player.clear_effects()
			self.advance_time()
			self.player.current_room.get_description(self.game_time)
			print()
			self.new_room = False

		input_str = input("> ")
		self.parser.parse_input(self, input_str)

	def help(self):
		say("Commands:")
		say("{:>10}{:^5}{}".format("inventory", ":", "display a list of all of your items"))
		say("{:>10}{:^5}{}".format("loadgame", ":", "load a previously saved game"))
		say("{:>10}{:^5}{}".format("savegame", ":","save your current progress"))		
		say("{:>10}{:^5}{}".format("help", ":","display this help menu"))
		say("{:>10}{:^5}{}".format("quit", ":","close the game (with or without saving)"))
		print()
		
		verb_str = ""
		for verb in self.verb_list:
			verb_str = verb_str + "{:10}".format(verb)

		say("Actions:")
		say(verb_str)

	def inventory(self):
		item_str = ""

		for item in self.player.inventory:
			item_str = item_str + "{:15}".format(item.name)

		say("Inventory:")
		say(item_str)

	def quit(self):
		if self.get_yn_answer("Do you want to save before you quit? (y/n) "):
			self.save_game()
		self.end()

	def end(self):
		self.end_game = True

	def play(self):
		while not self.end_game:
			self.prompt()

# Temporarily turning off width validation for ease of use in my IDE
#if valid_screen_size() or True:
if valid_screen_size():
	intro()
	game = Game()
	if game.game_loaded:
		game.play()
