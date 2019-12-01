from Utilities import say
import Utilities
from Create import thing_list, room_list
from Verbs_and_Actions import action_list, verb_list

# TODO its possible we will want the player class in it's own file
# Temporary Player and Game classes for testing
class Player:

    def __init__(self):
        """Initialize player"""
        self.name = "NAME"
        self.inventory = []
        # Room object
        self.current_room = None
        self.special_functions = {"pro":
                                      {"name": "pro",
                                       "learned": False,
                                       "description": "Gain extreme coordination.",
                                       "action": "verb_only"},
                                  "ram":
                                      {"name": "ram",
                                       "learned": False,
                                       "description": "Applies a great force.",
                                       "action": "direct_object"},
                                  "kin":
                                      {"name": "kin",
                                       "learned": False,
                                       "description": "Duplicates something.",
                                       "action": "direct_object"},
                                  "tic":
                                      {"name": "tic",
                                       "learned": False,
                                       "description": "Make a machine malfucntion.",
                                       "action": "direct_object"},
                                  "led":
                                      {"name": "led",
                                       "learned": False,
                                       "description": "Powers a room's lights.",
                                       "action": "verb_only"}
                                  }
    def add_to_inventory(self, thing):
        """removes an item from the player inventory"""
        # place holder message
        say("[[player adds {} to inventory]]".format(thing.name))
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
        self.direction_list = ["north", "east", "south", "west", "up", "down"]

        # initialize starting location with roomA
        self.player.current_room = self.room_list["roomA"]
        self.game_time = None

    def get_thing_by_name(self, thing_name, must_be_in_inventory):
        # first, look for thing with given name in player inventory
        # default_thing = Utilities.find_by_name()
        thing_in_inventory = self.find_by_name(thing_name, self.player.inventory)
        if (thing_in_inventory != None):
            # found it
            return thing_in_inventory
        else:
            if (must_be_in_inventory):
                default_thing = self.find_by_name(thing_name, self.thing_list)
                say("You don't have {}.".format(default_thing.list_name))
                return None
            else:
                # look in room's accessible contents:
                thing_in_room = self.find_by_name(thing_name, self.player.current_room.get_all_accessible_contents())
                if (thing_in_room != None):
                    # found it
                    return thing_in_room
                else:
                    default_thing = self.find_by_name(thing_name, self.thing_list)
                    say("You don't see {}.".format(default_thing.list_name))
                    return None

        def advance_time(self):
            time = self.game_time

            if time is None:
                time = 0
            else:
                time += 1
                if time > 11:
                    time = 0

            self.game_time = time

        def get_word_answer(self, prompt, answer):
            # displays the prompt
            # gets input from player
            # compares input to answer, and returns True or False if it matches
            # matches should ignore case? or extra whitespace?
            # NOTE I included the prompt in case we want to re-display the prompt after an invalid input
            say(prompt)
            input_str = input("> ")

            input_str_lc = input_str.lower()
            answer_lc = answer.lower()

            input_words = input_str_lc.split()
            answer_words = answer_lc.split()

            if input_words == answer_words:
                return True
            else:
                return False

        def get_yn_answer(self, prompt):
            # displays the prompt
            # gets a yes or no from the player
            # returns True for yes, False for no
            # NOTE I included the prompt in case we want to re-display the prompt after an invalid input
            # NOTE2 it would probably make sense to have the other y/n questions in the game options use the same method
            valid_input = False
            input_str = ""

            while not valid_input:
                say(prompt)
                input_str = input("> ")

                if input_str.lower() == "y" or input_str.lower() == "yes":
                    ret_val = True
                    valid_input = True
                elif input_str.lower() == "n" or input_str.lower() == "no":
                    ret_val = False
                    valid_input = True
                else:
                    self.say("Invalid input!")

            return ret_val

# TODO
#  Game can get all_things and all_rooms from Create.py
#  For saving/loading:
#  use thing.get_status() and room.get_status() to get JSON for that thing
#  use thing.set_status(status) and room.set_status(status) to update room using saved JSON
#  can use similar status methods for player