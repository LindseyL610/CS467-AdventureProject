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
