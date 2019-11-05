class Action:
	#staticmethod
	def perform_action(game, action_args, parts_of_speech):
		if len(parts_of_speech) == 1:	
			if parts_of_speech[0] == "verb":
				Action.verb_action(game, action_args)
			elif parts_of_speech[0] == "object":
				Action.obj_action(game, action_args)
			elif parts_of_speech[0] == "direction":
				Action.go_action(game, action_args)	
		elif len(parts_of_speech) == 2:
			if parts_of_speech[0] == "verb" and parts_of_speech[1] == "object":
				Action.verb_obj_action(game, action_args)
			elif action_args[0]  == "go" and parts_of_speech[1] == "direction":
				action_args[0] = action_args[1]
				Action.go_action(game, action_args)
		elif len(parts_of_speech) == 3:
			if parts_of_speech[0] == "verb" and parts_of_speech[1] == "preposition"\
			and parts_of_speech[2] == "object":
				Action.verb_prep_obj_action(game, action_args)

	#staticmethod
	def get_exit_direction(game, action_args):
		exit_name = ""

		if len(action_args) == 1:	
			exit_name = action_args[0]
		elif len(action_args) == 2:
			exit_name = action_args[1]

		current_room = game.objects[game.get_current_room()]

		for direction in current_room.data["exits"]:
			if current_room.data["exits"][direction] == exit_name:
				return direction
		
		return None	

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
		Action.default_verb_action(game, actionargs)

	#staticmethod	
	def default_verb(game, action_args):
		if action_args[0] == "go":
			print("I don't know where you want to go to.")
		else:
			print("Nothing happens.")

	#staticmethod
	def obj_action(game, action_args):
		exit_direction = Action.get_exit_direction(game, action_args)

		if exit_direction != None:
			action_args[0] = exit_direction
			Action.go_action(game, action_args)
		elif not Action.has_item(game, action_args[0]):
			print("The " + action_args[0] + " is not in your bag or the current room.")
		else:
			print("I don't know what you want to do with the " + action_args[0])

	#staticmethod
	def verb_obj_action(game, action_args):
		if not Action.has_item(game, action_args[1]):
			print("The " + action_args[1] + " is not in your bag or the current room.")
		elif action_args[0] == "go":
			exit_direction = Action.get_exit_direction(game, action_args)
		
			if exit_direction != None:
				action_args[0] = exit_direction
				Action.go_action(game, action_args)
			else:
				print("You cannot go there.")
		elif action_args[0] == "take":
			if game.objects[action_args[1]].data["static"] == False:
				game.take_item(action_args[1])
			else:
				print("You can't take the " + action_args[1] + "!")
		elif action_args[0] == "drop":
			game.drop_item(action_args[1])
		elif Action.perform_special_action(game, action_args):
			return
		else:
			print("You cannot " + action_args[0] + " the " + action_args[1] + ".")

	#staticmethod
	def go_action(game, action_args):
		game.go(action_args[0])

	#staticmethod
	def verb_prep_obj_action(game, action_args):
		if not Action.has_item(game, action_args[2]):
			print("The " + action_args[2] + " is not in your bag or the current room.")
		elif action_args[0] == "look":
			if action_args[1] == "at":
				print(game.objects[action_args[2]].data["description"])
			else:
				print("You cannot do that.")
		elif action_args[0] == "take":
			if action_args[1] == "up":
				game.take_item(action_args[2])
			else:
				print("You cannot do that.")	
		elif action_args[0] == "drop":
			if action_args[1] == "down":
				game.drop_item(action_args[2])
			else:
				print("You cannot do that.")
		else:
			print("You cannot do that.")	

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
					game.objects[ob].perform_action(game, action_args[0])
					return True

		return False
