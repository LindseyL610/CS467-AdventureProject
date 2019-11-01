import action

class Parser:
	def __init__(self):
		self.user_input = ""
		self.dictionary = self.init_dictionary()
		self.speech_dict = self.init_parts_of_speech()
		self.action_args = []
		self.parts_of_speech = []
		self.debug = False # Temporary for debugging

	# Temporary method for debugging
	def print_parsed(self):
		print("\nParsed input:")
		print(self.action_args)
		print("\nParts of speech:")
		print(self.parts_of_speech)
		print("\n")

	def parse_input(self, game, user_input):
		self.init_input(user_input)
		self.set_input()

		if self.debug == True:
			self.print_parsed()

		if len(self.action_args) == 0:
			print("I don't understand that.")
		else:
			action.Action.perform_action(game, self.action_args, self.parts_of_speech)

	def init_input(self, user_input):
		self.user_input = user_input
		self.action_args = []
		self.parts_of_speech = []

	def set_input(self):
		self.tokenize_input()

		idx = 0

		while idx < len(self.user_input):
			self.remove_punctuation(idx)
			self.stem_input(idx)
			self.get_synonyms(idx)
			self.set_parts_of_speech(idx)

			idx += 1

	def tokenize_input(self):
		self.user_input = self.user_input.lower()
		self.user_input = self.user_input.split()

	def remove_punctuation(self, idx):
		self.user_input[idx] = self.user_input[idx].strip('!,.?;:"')
		self.user_input[idx] = self.user_input[idx].replace("'", "")

	def stem_input(self, idx):
		prefixes = ["re"]
		suffixes = ["ing"]

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

	def init_dictionary(self):
		gamedict = {
			"look": "look",
			"look at": "look at",
			"go": "go",
			"walk": "go",
			"run": "go",
			"take": "take",
			"help": "help",
			"inventory": "inventory",
			"jump": "jump",
			"drop": "drop",
		}

		return gamedict

	def init_parts_of_speech(self):
		parts_of_speech = {
			"look": "verb",
			"look at": "verb",
			"go": "verb",
			"take": "verb",
			"help": "verb",
			"jump": "verb",
			"drop": "verb",
			"open": "verb",
			"use": "verb",
			"book": "object",
			"door": "object",
			"key": "object",
			"north": "direction",
			"south": "direction",
			"east": "direction",
			"west": "direction"
		}	

		return parts_of_speech
