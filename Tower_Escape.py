# !/usr/bin/python
# tower escape
# Author: Jason DiMedio
# CS467
# 
# Tower Escape - main program / functions to be built into Game class

import os
import datetime
import sys
import Game

DEBUG_MODE = False

#NOTE: The following global variables will be incorporated into the Game class once it's created
user_name = ""
new_game = False
game_data = "" # This is just a placeholder for the entire Game state data
current_file = ""

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

def validate_input(min, max):
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

def get_path():
	#NOTE: The following dir_path definition is adapted from: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory#targetText=os.getcwd()%20(returns%20%22,current%20working%20directory%20to%20path%20%22)
	#debug(os.getcwd())

	dir_path = os.path.dirname(os.path.realpath(__file__))
	#debug(dir_path)

	return dir_path

def get_save_files():
	save_files = list()
	
	files = os.listdir(get_path())
	#debug(files)

	for name in files:
		if name.find("SV_") is 0:
			save_files.append(name)

	return save_files

def get_load_names():
	load_names = list()

	files = get_save_files()

	for name in files:
		if name.find("SV_") is 0:
			load_names.append(name[3:])

	return load_names

def load_menu(initial):
	i = 1
	load_names = get_load_names()

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

	selection = validate_input(1, i)

	if initial:
		if int(selection) is (i-1):
			create_new_game()
		elif int(selection) is i:
			return False
	else:
		if int(selection) is not i:
			idx = int(selection) - 1
			load_saved_game(load_names[idx])

	return True

def save_game():
	global current_file
	global new_game
	
	new_filename = "SV_" + user_name + ", " + str(datetime.datetime.now()).replace(":", "-")
	
	if new_game:
		retrieve_file = new_filename
	else:
		retrieve_file = current_file
	
	f = open (retrieve_file, "w")

	f.truncate(0)
	f.write("data:" + game_data)
	f.close()
	
	if not new_game:
		os.rename(retrieve_file, new_filename)

	current_file = new_filename
	new_game = False
	print("Game saved!")

	debug("user_name=" + user_name)
	debug("new_game=" + str(new_game))
	debug("game_data=" + game_data)
	debug("current_file=" + current_file)

def create_new_game():
	#NOTE: Globals need to be removed once Game class is implemented
	global user_name
	global new_game
	global game_data

	user_name = input("Enter your name: ")
	time = str(datetime.datetime.now())

	new_game = True
	
	game_data = "Placeholder Game state data for " + user_name + " at " + time
	debug("user_name=" + user_name)
	debug("new_game=" + str(new_game))
	debug("game_data=" + game_data)
	debug("current_file=" + current_file)
	

def load_saved_game(load_name):
	# NOTE: Globals to be removed
	global current_file
	global game_data
	global user_name

	#debug(get_save_files())

	files = get_save_files()

	for name in files:
		if name.find(load_name) is 3:
			debug("matching file: " + name)
			match = name

	if match:
		#NOTE: The following file read functionality was adapted from: https://www.guru99.com/reading-and-writing-files-in-python.html#3
		f = open(match, "r")
		if f.mode is 'r':
			game_data = f.read()
			current_file = match
		f.close()
		user_name = match[3:match.find(",")] # This is temporary
		print("Game loaded!")
	else:
		print("Error loading game file!")
		return

	debug("user_name=" + user_name)
	debug("new_game=" + str(new_game))
	debug("game_data=" + game_data)
	debug("current_file=" + current_file)


def process_command(input):
	ret_val = True

	#savegame
	if input == "savegame":
		save_game()

	#loadgame
	elif input == "loadgame":
		#TODO: prompt are you sure
		load_menu(False)

	#help
	elif input == "help":
		print ("help toggled")

	#quit
	elif input == "quit":
		print ("quit toggled")
		#TODO: prompt to save game before quitting

	#other (e.g. game text input)
	else:
		if not toggle_debug(input):
			print ("other toggled")
			ret_val = False

	debug("input: " + input)
	debug("ret_val: " + str(ret_val))
	return ret_val
	
def prompt():
	# NOTE: Once the Game class is implemented, this will use a data attribute of the Game class instead of re-evaluating the input string
	input_str = ""

	while not (input_str == "quit"):
		print("prompt placeholder (here is where the descriptive text will be displayed)")
		input_str = input("> ")
		process_command(input_str)

# Display title screen
#print("title screen placeholder")

# Display menu screen for loading saved game or creating new game
#loaded = load_menu(True)

# Prompt for game input
#if loaded:
#	prompt()

game = Game.Game()
game.prompt()
