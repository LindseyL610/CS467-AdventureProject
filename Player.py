from Utilities import say
from Create import all_things, all_rooms

# TODO its possible we will want the player class in it's own file
# Temporary Player and Game classes for testing
class Player:

	# PLAYER
	# id
	# name
	# bag ["item1", "item2" ... ]
	# spells ["spell1", "spell2" ... ]
	# current_location = [id of Room]

	# check_bag([id])
		# if [bag] contains [id], return True
			#else return False

	# destination must be a valid Room ID
	def go(self, destination):
		# is destination a direction?
		# if not, see if it matches any exits
		if not self.is_direction(destination):
			for direction in self.exits:
				if self.exits[direction] == destination:
					new_room = destination
					break

		# if destination IS a direction
		else:
			origin = self.get_current_room()
			exits = self.objects[origin].data["exits"].copy()

			if exits[direction] is not None:
				if self.objects[exits[direction]].state["locked"]:
					self.say("That exit is locked!")
					return

				for room in self.objects[exits[direction]].data["rooms"]:
						if not (room == origin):
							destination = room

				self.state["current_room"] = destination
				self.say("You travel " + direction + " through the " + exits[direction] + ".")
				self.new_room = True



	"""This class stores and manages all data related to the player."""
	def __init__(self, state):
		"""Initialize player"""
		self.name = state["name"]
		self.bag = state["bag"]
		self.current_room = state["current_room"]
		self.spells = state["spells"]

	def do(self, action):
		#if player can do the action
		#(player has ability)
		#(dobj and/or iobj exists in room or bag)
		#(send action to dobj.perform_action and get effect)
			#(if no dobj, send to room)
		

    def take(self, thing):
        """Remove an item from the environment and add it to your inventory"""
        # place holder message
        say("[[player takes {}]]".format(thing.name))
        # remove thing from its current location (room or storage)
        # add thing to inventory

    def drop(self, thing):
        """Drop an item in the players inventory and leave it in the current room"""
        # place holder message
        say("[[player drops {}]]".format(thing.name))
        # remove thing from inventory (can use player.remove_from_inventory)
        # add thing to current room contents (use room.add_thing())

    def go(self, destination):
        """changes the location of the player, and displays description
        of new destination"""
        # place holder message
        say("[[player goes to room {}]]".format(destination.name))
        destination.get_description()

    def remove_from_inventory(self, thing):
        """removes an item from the player inventory"""
        # place holder message
        say("[[player removes {} from inventory]]".format(thing.name))
        # remove thing from inventory

    def get_state(self):
		state = {}
		state["name"] = self.name
		state["bag"] = self.bag.copy()
		state["current_room"] = self.current_room
		state["actions"] = self.actions.copy()

		return state

class Game:
    def __init__(self):
        """initialized Game, creates player and loads in room_list and thing_list"""
        self.player = Player()
        self.room_list = all_rooms
        self.thing_list = all_things

        # initialize starting location with roomA
        self.player.current_room = "roomA"


# TODO
#  Game can get all_things and all_rooms from Create.py
#  For saving/loading:
#  use thing.get_status() and room.get_status() to get JSON for that thing
#  use thing.set_status(status) and room.set_status(status) to update room using saved JSON
#  can use similar status methods for player