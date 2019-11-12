from Utilities import say
from Create import thing_list, room_list
from Verbs_and_Actions import action_list, verb_list

# TODO its possible we will want the player class in it's own file
# Temporary Player and Game classes for testing
class Player:
    """This class stores and manages all data related to the player."""
    def __init__(self):
        """Initialize player"""
        self.name = "NAME"
        self.inventory = []
        self.current_room = None

    def get_status(self):
        """returns the status of the player in JSON format"""
        pass

    def set_status(self, status):
        """uses the JSON data in status to update the player"""
        pass

    def add_to_inventory(self, thing):
        """removes an item from the player inventory"""
        # place holder message
        say("[[player removes {} from inventory]]".format(thing.name))
        # remove thing from inventory
        self.inventory.append(thing)

    def remove_from_inventory(self, thing):
        """removes an item from the player inventory"""
        # place holder message
        say("[[player removes {} from inventory]]".format(thing.name))
        # remove thing from inventory
        self.inventory.remove(thing)

    def take(self, thing):
        """Remove an item from the environment and add it to your inventory"""
        # place holder message
        say("[[player takes {}]]".format(thing.name))

        # remove thing from its current location (room or storage)
        self.current_room.remove_thing(thing)
        # add thing to inventory
        self.add_to_inventory(thing)

    def drop(self, thing):
        """Drop an item in the players inventory and leave it in the current room"""
        # place holder message
        say("[[player drops {}]]".format(thing.name))
        # remove thing from inventory (can use player.remove_from_inventory)
        self.remove_from_inventory(thing)
        # add thing to current room contents (use room.add_thing())
        self.current_room.add_thing(thing)

    def go(self, destination):
        """changes the location of the player, and displays description
        of new destination"""
        # place holder message
        say("[[player goes to room {}]]".format(destination.name))
        self.current_room = destination
        destination.get_description()


    def is_in_inventory(self, thing):
        """returns whether or not the given thing is in the Player's inventory
        thing: the object itself (not the id?)
        """
        return thing in self.inventory


class GameData:
    def __init__(self):
        """initialized Game, creates player and loads in room_list and thing_list"""
        self.player = Player()
        self.room_list = room_list
        self.thing_list = thing_list
        self.action_list = action_list
        self.verb_list = verb_list

        # initialize starting location with roomA
        self.player.current_room = self.room_list["roomA"]


# TODO
#  Game can get all_things and all_rooms from Create.py
#  For saving/loading:
#  use thing.get_status() and room.get_status() to get JSON for that thing
#  use thing.set_status(status) and room.set_status(status) to update room using saved JSON
#  can use similar status methods for player