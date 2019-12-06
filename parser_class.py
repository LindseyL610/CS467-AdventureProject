from Verbs_and_Actions import verb_list, action_list
from Utilities import say

class Parser:
	def __init__(self, game):
		self.user_input = ""
		self.original_input = ""
		self.dictionary = game.get_game_dictionary()
		self.lc_dictionary = self.get_lc_dictionary()
		self.speech_dict = game.get_parts_of_speech_dictionary()
		self.action_args = []
		self.parts_of_speech = []
		self.action_dict = dict()
		self.verbs_list = ["drop", "eat", "go", "open", "take", "unlock", "read"]
		self.exits = game.get_all_exits()
		self.unrecognized_words = []
		self.debug = False # For debugging
		self.special_function = False
		self.doubles = False

	# Method for debugging
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
		self.update_dictionaries(game)

		if self.check_basic_verbs(game) == 1: 
			if self.set_input(game) == 1:
				print()
				return
			else: 
				if self.doubles == True:
					say("I don't understand that. Please try a different command.")
					print()	
					return

				if len(self.unrecognized_words) != 0:
					self.print_unrecognized()

				if self.debug == True:
					self.print_parsed()
				elif self.special_function:
					self.check_special_function(game)
				elif self.action_dict.get("verb", None) != None:
					say(verb_list[self.action_dict["verb"]].execute(game, self.action_dict))
				else:
					say("I don't understand that. Please try a different command.")

		print()

	def init_input(self, user_input):
		self.user_input = user_input.lower()
		self.original_input = ""
		self.action_args = []
		self.parts_of_speech = []
		self.action_dict.clear()
		self.special_function = False
		self.unrecognized_words = []
		self.doubles = False

	def update_dictionaries(self, game):
		for function in game.player.special_functions:
			if game.player.special_functions[function]["learned"] == False:
				name = game.player.special_functions[function]["name"]

				if name not in self.dictionary:
					self.dictionary[name] = name

				if name not in self.speech_dict:
					self.speech_dict[name] = "object"

	def check_basic_verbs(self, game):
		if self.user_input == "look":
			self.action_dict["verb"] = "look"
			say(verb_list[self.action_dict["verb"]].execute(game, self.action_dict))
		elif self.user_input == "help":
			game.help()
		elif self.user_input == "inventory":
			game.inventory()
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
		self.original_input = self.user_input

		idx = 0

		while idx < len(self.user_input):
			self.remove_punctuation(idx)
			self.stem_input(idx)
			self.get_synonyms(idx)
			if self.set_parts_of_speech(idx, game) == 1:
				return 1

			idx += 1

		self.set_action_dict(game)

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
			if self.speech_dict[self.user_input[idx]] != "adjective":
				self.action_args.append(self.user_input[idx])
				self.parts_of_speech.append(self.speech_dict[self.user_input[idx]])
		else:
			self.unrecognized_words.append(self.original_input[idx])

	def set_action_dict(self, game):
		verb = None
		dobj = None
		prep = None
		iobj = None
		direction = None

		idx = 0

		while idx < len(self.parts_of_speech):
			if (self.parts_of_speech[idx] == "verb"):
				if verb == None:
					verb = self.action_args[idx]
				else:
					self.doubles = True
			elif self.parts_of_speech[idx] == "object":
				if dobj == None:
					dobj = self.action_args[idx]
				elif iobj == None:
					iobj = self.action_args[idx]
				else:
					self.doubles = True
			elif (self.parts_of_speech[idx] == "preposition"):
				if prep == None:
					prep = self.action_args[idx]
				else:
					self.doubles = True
			elif (self.parts_of_speech[idx] == "direction"):
				if direction == None:
					direction = self.action_args[idx]
				else:
					self.doubles = True

			idx += 1

		if (prep is not None) and (dobj is None):
			if (prep == "up") or (prep == "down"):
				dobj = prep
				prep = None	

		if (direction is not None) and (dobj is None):
			dobj = direction

		if (verb is None) and (dobj is not None):
			if (dobj in self.exits) or (dobj in game.direction_list)\
			or (dobj == "up") or (dobj == "down"):
				verb = "go"

		if verb is not None:
			self.action_dict["verb"] = verb

		if dobj is not None:
			self.action_dict["dobj"] = dobj

		if prep is not None:
			self.action_dict["prep"] = prep

		if iobj is not None:
			self.action_dict["iobj"] = iobj

		for function in game.player.special_functions:
			if game.player.special_functions[function]["name"] == dobj:
				self.special_function = True
				break

	def check_special_function(self, game):
		if self.action_dict.get("verb", None) == None\
		or self.action_dict["verb"] is not "call":
			say("You must use 'call' with " + self.action_dict["dobj"] + ".")
		else:
			say(verb_list[self.action_dict["verb"]].execute(game, self.action_dict))

	def print_unrecognized(self):
		message = "WARNING - I did not recognized the following words: "

		idx = 0

		while idx < len(self.unrecognized_words):
			message += self.unrecognized_words[idx]

			if len(self.unrecognized_words) == 2:
				if idx < (len(self.unrecognized_words) - 1):
					message += " and "
			elif idx < (len(self.unrecognized_words) - 2):
				message += ", "
			elif idx == (len(self.unrecognized_words) - 2):
				message += ", and "

			idx += 1

		say(message)
		print()
