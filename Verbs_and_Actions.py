from Utilities import say

# parser: get input and identify parts:
# verb, dobj, prep, iobj.
# Check against *master* word list, which is generated by looking at
#  all things, rooms, and verbs, and their alternate words. translate words to their default name.
# Give feedback if prompt cannot be parsed

# action:
# make sure verb has a use case with given "parts" (e.g. dobj, iobj)
# otherwise give general error feedback (or more specific feedback if they messed up in a predicted way?)
# Look at words, make sure they are relevant (objects that are in inventory/current room and verbs that are known)
# (you can use room.get_all_accessible_contents() )
# make sure direct/indirect objects are of the correct type (e.g. IN_INVENTORY vs IN_ROOM)
# If all arguments are appropriate, call the verb on the correct object.
#  Most verbs that can be used by themselves, with no objects (like "look" or "jump")
#  will be called on the Room (Room.look() or Room.jump())
#  Otherwise the verb will be called on the direct object. (special cases exist, like "go")
# Note that when calling the method the arguments should be the current game object
#  (containing player and room/thing lists) and arguments, e.g. Thing.look(game, actionargs)
class Verb():
	def __init__(self, name):
		self.name = name
		self.alternate_names = []

		# Presposition key:value pairs-
		# The *key* is the string for the preposition itself.
		# If the verb supports using no preposition, the key is "None"
		# The *value* is the name of the "default" preposition used for that action.
		#  This is a way to have "alternate names" for prepositions that can be specific to which verb is used.
		self.supported_prepositions = {}

		#TODO Come up with better general wording
		self.msg_improper_use = "That is not how to use the verb \"{}\".".format(self.name)

	def execute(self, game, actionargs):
		### DEBUG
		print("actionargs: verb={} dobj={} prep={} iobj={}".format(
			actionargs.get("verb"),actionargs.get("dobj"),actionargs.get("prep"),actionargs.get("iobj") ))
		###

		verb_string = actionargs["verb"]
		if actionargs.get("prep") == None:
			prep_string = "NONE"
		else:
			prep_string = actionargs["prep"]

		if prep_string in self.supported_prepositions:
			# gets the "effective" preposition from supported_prepositions
			effective_prep = self.supported_prepositions[prep_string]

			# prepares the extra string to add to the verb
			#  if the prep is "NONE" nothing is added, so the final call will be to "verb"
			#  otherwise, an underscore and the prep name are added; the final call will be to "verb_prep"
			if effective_prep == "NONE":
				prep_extra = ""
			else:
				prep_extra = "_" + effective_prep

			# sending the game and action args to the proper action
			game.action_list[verb_string + prep_extra].execute(game, actionargs)

		else:
			say(self.msg_improper_use)

verb_list = {}

verb_list["look"] = Verb("look")
verb_list["look"].alternate_names.extend(["examine", "inspect"])
verb_list["look"].supported_prepositions.update({"NONE":"NONE", "at":"NONE"})

verb_list["read"] = Verb("read")
verb_list["read"].alternate_names.extend(["scan","interpret"])
verb_list["read"].supported_prepositions.update({"NONE":"NONE"})

verb_list["take"] = Verb("take")
verb_list["take"].alternate_names.extend(["grab"])
verb_list["take"].supported_prepositions.update({"NONE":"NONE"})

verb_list["drop"] = Verb("drop")
verb_list["drop"].alternate_names.extend(["leave"])
verb_list["drop"].supported_prepositions.update({"NONE":"NONE"})

verb_list["put"] = Verb("put")
verb_list["put"].alternate_names.extend(["place", "set", "store"])
verb_list["put"].supported_prepositions.update({"on":"on", "in":"in"})

verb_list["give"] = Verb("give")
verb_list["give"].alternate_names.extend([])
verb_list["give"].supported_prepositions.update({"to":"to"})

verb_list["pull"] = Verb("pull")
verb_list["pull"].alternate_names.extend(["yank"])
verb_list["pull"].supported_prepositions.update({"NONE":"NONE", "on":"NONE"})

verb_list["go"] = Verb("go")
verb_list["go"].alternate_names.extend(["walk", "run", "proceed"])
verb_list["go"].supported_prepositions.update(
	{"NONE":"NONE", "in":"NONE", "into":"NONE", "through":"NONE", "up":"NONE", "down":"NONE"})

verb_list["use"] = Verb("use")
verb_list["use"].alternate_names.extend(["activate"])
verb_list["use"].supported_prepositions.update({"NONE":"NONE"})

verb_list["open"] = Verb("open")
verb_list["open"].supported_prepositions.update({"NONE":"NONE", "up":"NONE"})

verb_list["close"] = Verb("close")
verb_list["close"].supported_prepositions.update({"NONE":"NONE"})

# not sure how we will keep track of prepositions, but here's a running list:
prep_list = ["at", "on", "in", "to", "into", "through", "up", "down"]


class Action():
	"""This class defines the unique characteristics for specific actions."""

	def __init__(self, name):
		self.name = name

		# get "base" verb (before the "_"), and steal the default improper use message.
		self.msg_improper_use = verb_list[self.name.split("_")[0]].msg_improper_use

		# do the dobj or iobj have to be in the inventory?
		self.dobj_must_be_in_inventory = False
		self.iobj_must_be_in_inventory = False

	def execute(self, game, actionargs):
		pass


class ActionVerbOnly(Action):
	"""this action can only be used with a verb only"""
	def execute(self, game, actionargs):
		if  "dobj" in actionargs.keys() or "iobj" in actionargs.keys():
			say(self.msg_improper_use)
		else:
			# send action to ROOM
			getattr(game.player.current_room,self.name)(game, actionargs)

class ActionDirect(Action):
	"""this action can be used only with a verb + direct object"""
	def execute(self, game, actionargs):
		if  "dobj" not in actionargs.keys() or "iobj" in actionargs.keys():
			say(self.msg_improper_use)
		else:

			# get the dobj by name, if available
			dobj_thing = game.get_thing_by_name(actionargs["dobj"],self.dobj_must_be_in_inventory)
			if dobj_thing != None:
				#self.name is the name of the action, e.g. put_in
				# so this calls dobj.action
				getattr(dobj_thing, self.name)(game, actionargs)


class ActionDirectGo(Action):
	"""a modified version of ActionDirect for Go that checks for direction vs Thing"""

	def execute(self, game, actionargs):
		if "dobj" not in actionargs.keys() or "iobj" in actionargs.keys():
			say(self.msg_improper_use)
		else:

			if actionargs["dobj"] in game.direction_list:
				getattr(game.player.current_room, self.name)(game, actionargs)
			else:
				# get the dobj by name, if available
				dobj_thing = game.get_thing_by_name(actionargs["dobj"], self.dobj_must_be_in_inventory)
				if dobj_thing != None:
					# self.name is the name of the action, e.g. put_in
					# so this calls dobj.action
					getattr(dobj_thing, self.name)(game, actionargs)

class ActionDirectAndIndirect(Action):
	"""this action can be used only with a verb, direct object, and indirect object"""
	def execute(self, game, actionargs):
		if "dobj" not in actionargs.keys() or "iobj" not in actionargs.keys():
			say(self.msg_improper_use)

		else:

			# get the dobj by name, if available
			dobj_thing = game.get_thing_by_name(actionargs["dobj"],self.dobj_must_be_in_inventory)
			if dobj_thing != None:

				# get the iobj by name, if available
				iobj_thing = game.get_thing_by_name(actionargs["iobj"], self.iobj_must_be_in_inventory)
				if iobj_thing != None:
					# note: self.name is the name of the action, e.g. put_in
					# so this calls dobj.action
					getattr(dobj_thing, self.name)(game, actionargs)


class ActionVerbOnlyOrDirect(Action):
	"""This action can be used either as a verb only, or with a direct object"""
	def execute(self, game, actionargs):

		# TODO check both cases
		if "iobj" in actionargs.keys():
			say(self.msg_improper_use)

		elif "dobj" in actionargs.keys():
			# get the dobj by name, if available
			dobj_thing = game.get_thing_by_name(actionargs["dobj"],self.dobj_must_be_in_inventory)
			getattr(dobj_thing,self.name)(game, actionargs)
		else:
			# send action to ROOM
			getattr(game.player.current_room,self.name)(game, actionargs)


# create actions
action_list = {}

# go (special case; likely needs own subclass)
# used with direction "go up" or "up" -> Room.go()
# used with Exit name "go door" or "door" -> Exit.go()
# verb + dobj(DIRECTION or ANYWHERE) "go north" -> Room.go()
# "go door" -> Thing.go()
action_list["go"] = ActionDirectGo("go")
# TODO

# look (special case; likely needs own subclass)
# only verb "look"-> Room.look()
# verb + dobj(ANYWHERE) "look door"-> Thing.look()
action_list["look"] = ActionVerbOnlyOrDirect("look")

# read
# verb + dobj(IN_INVENTORY/IN_ROOM) "read book" -> Thing.read()
action_list["read"] = ActionDirect("read")

# take
# verb + dobj(IN_ROOM) "take cheese" -> Thing.take()
action_list["take"] = ActionDirect("take")

# drop
# verb + dobj(IN_INVENTORY) "drop floppy" -> Thing.drop()
action_list["drop"] = ActionDirect("drop")
action_list["drop"].dobj_must_be_in_inventory = True

# put in
# verb + dobj(IN_INVENTORY) + iobj(ANYWHERE) "put cheese in fridge" -> Thing.put_in()
action_list["put_in"] = ActionDirectAndIndirect("put_in")
action_list["put_in"].dobj_must_be_in_inventory = True

# put on
# verb + dobj (IN_INVENTORY) + iobj(ANYWHERE) "put book on table" -> Thing.put_on()
action_list["put_on"] = ActionDirectAndIndirect("put_on")
action_list["put_on"].dobj_must_be_in_inventory = True

# give to
# verb + dobj (IN_INVENTORY) + iobj(ANYWHERE) "give cheese to mouse" -> Thing.give_to()
action_list["give_to"] = ActionDirectAndIndirect("give_to")
action_list["give_to"].dobj_must_be_in_inventory = True

# pull
# verb + dobj(ANYWHERE) "pull lever" -> Thing.pull()
action_list["pull"] = ActionDirect("pull")

# use
# verb + dobj(ANYWHERE) "use lever" -> Thing.use()
action_list["use"] = ActionDirect("use")

# open
# verb + dobj(ANYWHERE) "open door" -> Thing.open()
action_list["open"] = ActionDirect("open")

# close
# verb + dobj(ANYWHERE) "close door" -> Thing.close()
action_list["close"] = ActionDirect("close")