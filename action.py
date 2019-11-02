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

	#staticmethod
	def get_exit_direction(game, action_args):
		exit_name = ""

		if len(action_args) == 1:	
			exit_name = action_args[0]
		elif len(action_args) == 2:
			exit_name = action_args[1]

		for direction in game.rooms[game.current_room].exits:
			if game.rooms[game.current_room].exits[direction].id == exit_name:
				return direction

		return None	

	#staticmethod
	def verb_action(game, action_args):
		if game.current_room.name == "balcony":
			if action_args[0] == "jump":
				print("You fell through the floor.")
			else:
				Action.default_verb_action(game, actionargs)

	#staticmethod	
	def default_verb(game, action_args):
		if action_args[0] == "go":
			print("To where?")
		elif action_args[0] == "jump":
			print("Nothing happens.")

	#staticmethod
	def obj_action(game, action_args):
		exit_direction = Action.get_exit_direction(game, action_args)

		if exit_direction != None:
			action_args[0] = exit_direction
			Action.go_action(game, action_args)
		else:
			print("You cannot do that.")

	#staticmethod
	def verb_obj_action(game, action_args):
		if action_args[0] == "go":
			exit_direction = Action.get_exit_direction(game, action_args)
		
			if exit_direction != None:
				action_args[0] = exit_direction
				Action.go_action(game, action_args)
			else:
				print("You cannot do that.")
		elif Action.perform_special_action(game, action_args):
			return
		elif action_args[0] == "take":
			game.take_item(action_args[1])
		elif action_args[0] == "drop":
			game.drop_item(action_args[1])

	#staticmethod
	def go_action(game, action_args):
		game.go(action_args[0])

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
			return False
			
		else:
			for act in game.objects[ob].data["actions"]:
				if act == action_args[0]:
					game.objects[ob].perform_action(game, action_args[0])
