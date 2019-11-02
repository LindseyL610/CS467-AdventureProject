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
	


# Display title screen
#print("title screen placeholder")

# Display menu screen for loading saved game or creating new game
#loaded = load_menu(True)

# Prompt for game input
#if loaded:
#	prompt()

game = Game.Game()
game.prompt()




	def get_file_names(self, type):
		type_files = list()
	
		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name.find(type) is 0:
				type_files.append(name)

		return type_files





		def create_new_game(self):
		# Create a new player --for now this is just a generic object
		self.player = {}
		self.player["name"] = input("Enter your name: ")

		# These are data attributes for the saved game --currently not saved
		self.current_save = None #index of game in "saves" list
		
		# Here the default game state data is loaded
		self.state = self.game_data["default"].copy()

		# Load up instances of all objects for a new game
		self.construct_all_objects(True)











	def get_object_names(self, type):
		object_names = list()

		files = self.get_file_names(type)

		for name in files:
			object_names.append(name[3:])

		return object_names


		def load_rooms(self, rooms_data):
		rooms = dict()
				
		room_files = self.get_file_names(ROOM)

		for filename in room_files:
			data = self.load_data_from_file(filename)
			id = data["id"]

			if rooms_data is None:
				state = None #use default room state
			else:
				state = rooms_data[id] # use saved room state

			rooms[id] = Room.Room(data, state)

		return rooms