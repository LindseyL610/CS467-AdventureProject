# !/usr/bin/python
# tower escape
# Author: Jason DiMedio
# CS467
# 
# Tower Escape - main program / functions to be built into Game class

import os

DEBUG_MODE = False

def validate_input(min, max):
	global DEBUG_MODE
	valid_input = False

	selection = input ("Enter the number of your selection: ")

	# Validate input and activate debug mode
	while not valid_input:
		if int(selection) < min or int(selection) > max:
			#Turn debug mode on or off
			if int(selection) == 999:
				if not DEBUG_MODE:
					DEBUG_MODE = True
					print ("Debug mode turned ON.")
				else:
					DEBUG_MODE = False
					print ("Debug mode turned OFF.")
			else:
				print("Invalid selection.")

			selection = input("Enter the number of your selection: ")
		else:
			valid_input = True

	return selection

def get_load_names():
	load_names = set()

	files = os.listdir(".")
	for name in files:
		if name.find("SV_") is 0:
			load_names.add(name[3:])

	return load_names

def display_load_menu(load_names):
	i = 1

	print("Select a saved game to load, or create a new game.")

	for name in load_names:
		print(str(i) + ". " + name)
		i = i + 1

	print(str(i) + ". Create New Game")

	return i

def save_game(name, data):
	f = open ("SV_"+name, "w")
	f.write("data:" + data)
	f.close()

	i = 1

# Display title screen
print("title screen placeholder")

# TO BE REMOVED - create save files for testing purposes
#save_game("game 1", "test data for save file 1")
#save_game("game 2", "test data for save file 2")
#save_game("game 3", "test for game 3")



# Display menu screen
load_names = get_load_names()

num = display_load_menu(load_names)

selection_vl = validate_input(1, num)

print("selection was:", selection_vl)
print("DEBUG_MODE: ", DEBUG_MODE)


print ("")



