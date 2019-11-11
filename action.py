class Action:
	#staticmethod
	def perform_action(game, action_args, parts_of_speech):
		print(str(action_args))
		if len(parts_of_speech) == 1:	
			if parts_of_speech[0] == "verb": # verb only
				Action.verb_action(game, action_args)
			elif parts_of_speech[0] == "object": # object only
				Action.obj_action(game, action_args)
			elif parts_of_speech[0] == "direction": # direction only
				Action.go_action(game, action_args)	
		elif len(parts_of_speech) == 2:
			if parts_of_speech[0] == "verb" and parts_of_speech[1] == "object": # verb object
				Action.verb_obj_action(game, action_args)
			elif action_args[0]  == "go" and parts_of_speech[1] == "direction": # verb direction
				action_args[0] = action_args[1]
				Action.go_action(game, action_args)
		elif len(parts_of_speech) == 3:
			if parts_of_speech[0] == "verb" and parts_of_speech[1] == "preposition"\
			and parts_of_speech[2] == "object":
				# verb preposition object
				Action.verb_prep_obj_action(game, action_args)

	#staticmethod
	def has_item(game, item):
		if item in game.state["bag"]:
			return True
		elif item in game.objects[game.get_current_room()].state["items"]:
			return True
		elif Action.has_exit(game, item):
			return True
		else:
			return False

	#staticmethod
	def has_exit(game, item):
		cur_room = game.objects[game.get_current_room()]
		for exit in cur_room.data["exits"]:
			if cur_room.data["exits"][exit] == item:
				return True

		return False

	#staticmethod
	def verb_action(game, action_args):
		#WHEN ONLY A VERB IS RECOGNIZED

		#look
		if action_args[0] == "look":
			Action.look_action(game, action_args)

		else:
			Action.default_verb(game, action_args)

	#staticmethod	
	def default_verb(game, action_args):
		if action_args[0] == "go":
			game.say("I don't know where you want to go to.")
		else:
			game.say("Nothing happens.")

	#staticmethod
	# WHEN ONLY A NON-VERB IS RECOGNIZED
	def obj_action(game, action_args):
		object = action_args[0]

		# is object a direction
		if Action.is_direction(object):
			# if so, this is a "go" action
			Action.go_action(game, action_args)

		elif not Action.has_item(game, action_args[0]):
			game.say("The " + action_args[0] + " is not in your bag or the current room.")
		else:
			game.say("I don't know what you want to do with the " + action_args[0])

	def is_direction(destination):
		if destination == "north" or destination == "south" or destination == "east" or destination == "west":
			return True
		else:
			return False


	#staticmethod
	def verb_obj_action(game, action_args):
		# WHEN THERE IS A VERB AND A SINGLE OBJECT

		if not Action.has_item(game, action_args[1]):
			game.say("The " + action_args[1] + " is not in your bag or the current room.")

		# look [Thing]
		elif action_args[0] == "look":
			Action.look_action(game, action_args)
		
		# go [Thing] / go [direction]
		elif action_args[0] == "go":
			Action.go_action(game, action_args)
		
		# take [Thing]	
		elif action_args[0] == "take":
			Action.take_action(game, action_args)

		# drop [Thing]
		elif action_args[0] == "drop":
			Action.drop_action(game, action_args)


		elif Action.perform_special_action(game, action_args):
			return
		else:
			game.say("You cannot " + action_args[0] + " the " + action_args[1] + ".")

	#staticmethod
	def go_action(game, action_args):
		object = ""
		current_room = game.objects[game.get_current_room()]
		origin = game.get_current_room()
		exits = game.objects[game.get_current_room()].exits
		exit_id = None
		destination = None

		#get the object - either a direction or destination
		if len(action_args[0]) == 1:
			object = action_args[0]
		elif len(action_args[0]) > 1:
			object = action_args[1]

		# if object is a direction
		if Action.is_direction(object):
			# and if that direction does not have a valid Exit in the current room
			if exits[object] is None:
				game.say("There is no exit in that direction!")
				return
			else:
				exit_id = exits[object]
		
		# if object is not a direction
		else:
			# is object a valid exit from the current room?
			for direction in exits:
				if exits[direction] == object:
					exit_id = object

		# if no match is found
		if exit_id is None:
			game.say("You can't go there!")
			return

		# at this point, we have a valid exit_id

		# if the Exit is locked
		if game.objects[exit_id].locked:
			game.say("That exit is locked!")
			return

		# at this point we have an exit_id for an unlocked exit
		# set destination
		destination = game.objects[exit_id].get_destination(origin)

		# set current_room to destination
		game.current_room = destination

		# get prompt message from newly entered room
		message = game.objects[game.get_current_room()].prompt_message()

		# change destination Room visited status
		game.objects[destination].visited = True

		# say prompt message
		game.say(message)

	#staticmethod
	def look_action(game, action_args):

		# determine what object you're going to be looking at
		# only one arg (e.g. only "look")
		if len(action_args) == 1:
			object = game.get_current_room()

		# look [object]
		elif len(action_args) == 2:
			# look around
			if action_args[1] == "around":
				object = game.get_current_room()
			# look [object]
			else:
				object = action_args[1]

		# look at [object]
		elif len(action_args) == 3:
			if action_args[1] == "at":
				object = action_args[2]

		else:
			game.say("I don't understand.")
			return

		# if object is a Thing and is NOT the current room:
			# determine if Thing is available (in Room, on Feature surface, in open Feature container)
				# if not, say "There is no [Thing] to look at!" and return

		# call:  Thing.look()

		
	def take_action(game, action_args):
		current_room = game.objects[game.get_current_room()]

		# determine what the object is
		# take [Thing]
		if len(action_args) > 1:
			object = action_args[1]
		else:
			game.say ("I know what you want to take.")
			return

		# determine if Thing is available (in Room, on Feature surface, in open Feature container)
		# if not available
		if not Action.is_available(game, object):
			game.say("There is no " + object + " to take!")
			return

		# if available
		else:
			current_room.take(object)
			game.bag.append(object)
			game.say("The " + object + " is now in your bag.")

	def drop_action(game, action_args):
		object = action_args[1]
		current_room = game.objects[game.get_current_room()]

		# determine if object is in bag
		if not object in game.bag:
			game.say("You don't have the " + object + "!")
			return
		else:
			game.bag.remove(object)
			current_room.add_item(object)
			game.say("You dropped the " + object ".")

	# The following are "action" functions that need to be developed

		# put - place, insert, drop [into]
			# put [Thing1] [on/in] [Thing2]
				# determine if [Thing1] is available (is_available([id]) 
					# if not, say "There is no [Thing1] to put [on/in] the [Thing2]!"
					# if Thing1 is available
						# determine if Thing2 is available
							# if not, say "There is no [Thing2] to put the [Thing1] [on/in]!"
							# if both available:
								# call [Thing2].put(Thing1, [on/in])
									#if it returns true, call [current room].take(Thing1)
										# this ensures that the item is removed from wherever it was
			   		 								
		# open [Feature]
			# determine if Feature is available (is_available(Feature))
				# if not available, say "There is no [Feature] to open!"
				# if available, call Feature.open()

		# unlock [Thing1] with [Thing2]
			# determine if Thing1 is available (is_availabe(Thing1))
				# if not available, say "There is no [Thing1] to unlock!"
				# if available, determine if Thing2 is available
					# if not available, say "There is no [Thing2] to use to unlock the [Thing1]!"
					# if BOTH available
						# call Thing1.unlock(Thing2)

		# use [Thing]
			# determine if Thing is available (is_availabe(Thing))
				# if not available, say "There is no [Thing] to use!"
				# if Thing is available
					# determine if Thing is a key for any Exit or Container in the current room
						# if not
							# call Thing.perform_action(use)
						# if it is a key for an Exit or Container in the current room,
							# call Exit/Container.unlock(Thing)
		
		# type TEXT
			# determine if there is a KeyboardPuzzle in the Room
				# if not
					# say "There is nothing to type on!"
				# if there is a keyboard puzzle
					# call KeyboardPuzzle.type(TEXT)
						# if result returns true
							# check if the Puzzle is completed
							# call KeyboardPuzzle.check_status()
								# if result returns true
									# get prize from puzzle and add to Bag
								
		# [other verb] [Thing]
			# Is there a Thing specified?
				# if not
					# use current room for action sequence (see below)
				# if Thing is specified
					# is Thing available? call is_available()
							# if not available, say "There is no [Thing] to [verb]!"
								# return
							# if available,
								# use Thing for action sequence (see below)
			# proceed to action sequence (see below)

			# action sequence - using either CurrentRoom or Thing as OBJECT (to call the function)
				# is [other verb] a SPELL?
					# if yes, 
						# has Player learned SPELL?
						# if SPELL is not learned
							# say "You don't know that spell."
							# return / (DONT CONTINUE)

				# call OBJECT.perform_action(verb)
					# if result returns true
						# call OBJECT.check_status()
							# if result returns true
								# add prize to Bag or learn skill
						
		# cast SPELL (on [Thing])
			# is SPELL available?
				# check Player.spells
					# if spell is not learned
						# say "You don't know that spell."
					# if spell is learned
						# Is there a Thing specified?
							# if not, call [current room].perform_action(SPELL)
								# if result returns false, say "Nothing happens."
							# if there is a Thing specified,
								# is Thing available? call is_available()
									# if not available, say "There is no [Thing] to [verb]!"
									# if available,
										# call Feature.perform_action(SPELL)
										# if result returns false, say "Nothing happens."

	#staticmethod
	def verb_prep_obj_action(game, action_args):
		if not Action.has_item(game, action_args[2]):
			game.say("The " + action_args[2] + " is not in your bag or the current room.")

		# look (at) [Thing]
		elif action_args[0] == "look":
			Action.look_action(game, action_args)



		elif action_args[0] == "take":
			if action_args[1] == "up":
				game.take_item(action_args[2])
			else:
				game.say("You cannot do that.")	
		elif action_args[0] == "drop":
			if action_args[1] == "down":
				game.drop_item(action_args[2])
			else:
				game.say("You cannot do that.")
		else:
			game.say("You cannot do that.")	

	#staticmethod
	def perform_special_action(game, action_args):
		special_action = False
		ob = action_args[1]
	
		for obj in game.objects[game.get_current_room()].state["items"]:
			if game.objects[obj].data["id"] == ob:
				ob = obj
				special_action = True
				break
		
		if special_action == False:
			for obj in game.state["bag"]:
				if game.objects[obj].data["id"] == ob:
					ob = obj
					special_action = True
					break

		if special_action == False:
			cur_room = game.get_current_room()
			for direction in game.objects[cur_room].data["exits"]:
				if game.objects[cur_room].data["exits"][direction] == action_args[1]:
					special_action = True
					break

		if special_action == False:
			return False
		else:
			for act in game.objects[ob].data["actions"]:
				if act == action_args[0]:
					game.say(game.objects[ob].perform_action(game, action_args[0]))
					return True

		return False

	def is_available(game, thing):
		ret_val = False
		current_room = game.objects[game.get_current_room()]

		# if Thing is available in Bag
		if thing in game.bag:
			ret_val = True
		else:
			# Room.search() function will go through each item in the Room or in any Room Feature
			# NOTE: if it finds the item, the item will be removed!
			ret_val = current_room.search(thing)

		return ret_val