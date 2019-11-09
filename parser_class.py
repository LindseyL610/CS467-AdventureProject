import action

class Parser:
	def __init__(self):
		self.user_input = ""
		self.dictionary = self.init_dictionary()
		self.speech_dict = self.init_parts_of_speech()
		self.action_args = []
		self.parts_of_speech = []
		self.verbs_list = ["drop", "eat", "go", "open", "take", "unlock"]
		self.exits = ["door"]
		self.debug = False # Temporary for debugging

	# Temporary method for debugging
	def print_parsed(self):
		print("\nParsed input:")
		print(self.action_args)
		print("\nParts of speech:")
		print(self.parts_of_speech)
		print("\n")

	def parse_input(self, game, user_input):
		print("\n")
		self.init_input(user_input)

		if self.check_basic_verbs(game) == 1: 
			if self.set_input(game) == 1:
				return
			else: 
				if self.debug == True:
					self.print_parsed()
				else:
					action.Action.perform_action(game, self.action_args, self.parts_of_speech)


		print("\n")

	def init_input(self, user_input):
		self.user_input = user_input
		self.action_args = []
		self.parts_of_speech = []

	def check_basic_verbs(self, game):
		if self.user_input == "look":
			current_room = game.objects[game.get_current_room()]
			print(current_room.data["long_description"])
			for itm in current_room.state["items"]:
				obj = game.objects[itm]

				if obj.data["static"] == False:
					if obj.state["current_state"] in obj.data["message"]:
						print(obj.data["message"][obj.state["current_state"]])
					else:
						print(obj.data["message"]["default"])
		elif self.user_input == "help":
			print("I understand the following verbs:")
			for verb in self.verbs_list:
				print(verb)
		elif self.user_input == "inventory":
			print("Your bag contains the following items:")
			for item in game.state["bag"]:
				print(item)
		elif self.user_input == "loadgame":
			game.load_menu(False)
		elif self.user_input == "savegame":
			game.save_game()
		else:
			return 1
	
	def set_input(self, game):
		self.tokenize_input()
		self.remove_articles()

		idx = 0

		while idx < len(self.user_input):
			self.remove_punctuation(idx)
			self.stem_input(idx)
			self.get_synonyms(idx)
			if self.set_parts_of_speech(idx) == 1:
				return 1

			idx += 1

		self.set_objects(game)

	def tokenize_input(self):
		self.user_input = self.user_input.lower()
		self.user_input = self.user_input.split()

	def remove_articles(self):
		for word in self.user_input:
			if (word == "the") or (word == "a") or (word == "an") or (word == "some"):
				self.user_input.remove(word)

	def remove_punctuation(self, idx):
		self.user_input[idx] = self.user_input[idx].strip('!,.?;:"')
		self.user_input[idx] = self.user_input[idx].replace("'", "")

	def stem_input(self, idx):
		prefixes = ["re"]
		suffixes = ["ing", "s"]

		if(self.dictionary.get(self.user_input[idx], None) == None):
			for prefix in prefixes:
				if self.user_input[idx].startswith(prefix):
					self.user_input[idx] = self.user_input[idx][len(prefix):len(self.user_input[idx])]

			for suffix in suffixes:
				if self.user_input[idx].endswith(suffix):
					self.user_input[idx] = self.user_input[idx][0:len(suffix)+1]

	def get_synonyms(self, idx):
		self.user_input[idx] = self.dictionary.get(self.user_input[idx], self.user_input[idx])

	def set_parts_of_speech(self, idx):
		if self.user_input[idx] in self.speech_dict:
			self.action_args.append(self.user_input[idx])
			self.parts_of_speech.append(self.speech_dict[self.user_input[idx]])	
		else:
			print("I don't understand. Please try a different command.")
			return 1

	def set_objects(self, game):
		idx = 0

		if "adjective" in self.parts_of_speech:
			while idx < len(self.parts_of_speech) - 1:
				if self.parts_of_speech[idx] == "adjective" and\
				self.parts_of_speech[idx + 1] == "object":
					self.action_args[idx + 1] = self.action_args[idx]\
					+ " " + self.action_args[idx + 1]

					self.action_args.pop(idx)
					self.parts_of_speech.pop(idx)
				
				idx += 1
		else:
			while idx < len(self.action_args):
				if self.action_args[idx] in self.exits:
					possible_objs = list()
					current_room = game.objects[game.get_current_room()]

					for exit in current_room.data["exits"]:
						if (current_room.data["exits"][exit] is not None) and (self.action_args[idx] in current_room.data["exits"][exit]):
							possible_objs.append(current_room.data["exits"][exit])

					if len(possible_objs) == 1:
						self.action_args[idx] = possible_objs[0]
					elif len(possible_objs) > 1:
						obj = None

						while(obj == None):
							print("Which of the following " + self.action_args[idx] + "s: ")
							
							for possible_obj in possible_objs:
								print(possible_obj)

							obj = input("> ")

							print()

							if obj not in possible_objs:
								print("That is not one of the options. Please try again.")
								obj = None
							else:
								self.action_args[idx] = obj
				idx += 1

	def init_dictionary(self):
		gamedict = {
			"look": "look",
			"go": "go",
			"walk": "go",
			"run": "go",
			"leave": "go",
			"move": "go",
			"travel": "go",
			"procede": "go",
			"pass": "go",
			"progress": "go",
			"exit": "go",
			"wander": "go",
			"mosey": "go",
			"meander": "go",
			"hop": "go",
			"skip": "go",
			"jump": "go",
			"leap": "go",
			"climb": "climb",
			"drop": "drop",
			"put": "drop",
			"set": "drop",
			"dump": "drop",
			"release": "drop",
			"unload": "drop",
			"take": "take",
			"pick": "take",
			"grab": "take",
			"collect": "take",
			"hold": "take",
			"acquire": "take",
			"catch": "take",
			"attain": "take",
			"obtain": "take",
			"snatch": "take",
			"fridge": "fridge",
			"refrigerator": "fridge",
			"freezer": "fridge",
			"stairs": "stairs",
			"staircase": "stairs",
			"stair": "stairs",
			"steps": "stairs",
			"hallway": "hallway",
			"hall": "hallway",
			"corridor": "hallway",
			"eat": "eat",
			"consume": "eat",
			"swallow": "eat",
			"bite": "eat",
			"chew": "eat",
			"devour": "eat",
			"ingest": "eat",
			"nibble": "eat",
			"grand": "grand",
			"enormous": "grand"
		}

		return gamedict

	def init_parts_of_speech(self):
		parts_of_speech = {
			"look": "verb",
			"go": "verb",
			"take": "verb",
			"drop": "verb",
			"open": "verb",
			"use": "verb",
			"unlock": "verb",
			"eat": "verb",
			"book": "object",
			"door": "object",
			"fridge": "object",
			"key": "object",
			"stairs": "object",
			"cheese": "object",
			"hallway": "object",
			"gate": "object",
			"north": "direction",
			"south": "direction",
			"east": "direction",
			"west": "direction",
			"at": "preposition",
			"up": "preposition",
			"down": "preposition",
			"stone": "adjective",
			"grand": "adjective"
		}	

		return parts_of_speech
