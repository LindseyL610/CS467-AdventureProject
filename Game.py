from Utilities import say
from Create import all_things, all_rooms

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