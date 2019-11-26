from Verbs_and_Actions import verb_list, action_list
from Utilities import say

class Parser:
	def __init__(self, game):
		self.user_input = ""
		self.dictionary = game.get_game_dictionary()
		self.lc_dictionary = self.get_lc_dictionary()
		self.speech_dict = game.get_parts_of_speech_dictionary()
		self.action_args = []
		self.parts_of_speech = []
		self.action_dict = dict()
		self.verbs_list = ["drop", "eat", "go", "open", "take", "unlock", "read"]
		self.exits = ["door"]
		self.debug = False # Temporary for debugging

	# Temporary method for debugging
	def print_parsed(self):
		print("action_dict:")
		for item in self.action_dict:
			print(item + ": " + self.action_dict[item])

	def get_lc_dictionary(self):
		lc_dictionary = dict()

		for word in self.dictionary:
			lc_dictionary[word.lower()] = word

		return lc_dictionary

	def parse_input(self, game, user_input):
		print()
		self.init_input(user_input)

		if self.check_basic_verbs(game) == 1: 
			if self.set_input(game) == 1:
				print()
				return
			else: 
				if self.debug == True:
					self.print_parsed()
				else:
					game.say(verb_list[self.action_dict["verb"]].execute(game, self.action_dict))

		print()

	def init_input(self, user_input):
		self.user_input = user_input.lower()
		self.action_args = []
		self.parts_of_speech = []
		self.action_dict.clear()

	def check_basic_verbs(self, game):
		if self.user_input == "look":
			self.action_dict["verb"] = "look"
			game.say(verb_list[self.action_dict["verb"]].execute(game, self.action_dict))
		elif self.user_input == "help":
			game.say("I understand the following verbs:")
			for verb in self.verbs_list:
				game.say(verb)
		elif self.user_input == "inventory":
			game.say("Your bag contains the following items:")
			for item in game.player.inventory:
				game.say(item.name)
		elif self.user_input == "loadgame":
			game.load_menu(False)
		elif self.user_input == "savegame":
			game.save_game()
		elif self.user_input == "quit":
			game.quit()
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
			if self.set_parts_of_speech(idx, game) == 1:
				return 1

			idx += 1

		#self.set_objects(game) # Commented out since we aren't currently using multiple objects of same general type in one room
		self.set_action_dict()

	def tokenize_input(self):
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

		if(self.lc_dictionary.get(self.user_input[idx], None) == None):
			for prefix in prefixes:
				if self.user_input[idx].startswith(prefix):
					self.user_input[idx] = self.user_input[idx][len(prefix):len(self.user_input[idx])]

			for suffix in suffixes:
				if self.user_input[idx].endswith(suffix):
					self.user_input[idx] = self.user_input[idx][0:len(suffix)+1]

	def get_synonyms(self, idx):
		word = self.lc_dictionary.get(self.user_input[idx], self.user_input[idx])
		self.user_input[idx] = self.dictionary.get(word, word)

	def set_parts_of_speech(self, idx, game):
		if self.user_input[idx] in self.dictionary:
			self.action_args.append(self.user_input[idx])
			self.parts_of_speech.append(self.speech_dict[self.user_input[idx]])

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

	def set_action_dict(self):
		verb = None
		dobj = None
		prep = None
		iobj = None

		idx = 0

		while idx < len(self.parts_of_speech):
			if (self.parts_of_speech[idx] == "verb") and (verb == None):
				verb = self.action_args[idx]
			elif self.parts_of_speech[idx] == "object":
				if dobj == None:
					dobj = self.action_args[idx]
				elif iobj == None:
					iboj = self.action_args[idx]
			elif (self.parts_of_speech[idx] == "preposition") and (prep == None):
				prep = self.action_args[idx]

			idx += 1

		if (prep is not None) and (dobj is None):
			if (prep is "up") or (prep is "down"):
				dobj = prep
				prep = None	

		if verb is not None:
			self.action_dict["verb"] = verb

		if dobj is not None:
			self.action_dict["dobj"] = dobj

		if prep is not None:
			self.action_dict["prep"] = prep

		if iobj is not None:
			self.action_dict["iobj"] = iobj

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
			"read": "verb",
			"pull": "verb",
			"lever": "object",
			"plaque": "object",
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
			"on": "preposition",
			"in": "preposition",
			"with": "preposition",
			"under": "preposition",
			"stone": "adjective",
			"grand": "adjective"
		}	

		return parts_of_speech
