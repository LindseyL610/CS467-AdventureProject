from Utilities import say
import Utilities


class Room:
    """Basic Room class"""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.long_description = ""
        self.short_description = ""
        self.exits = {}

        self.has_been_visited = False
        self.contents = []

        self.msg_cannot_go_direction = "You cannot go that direction."

    def get_status(self):
        """returns the status of a thing in JSON format"""
        pass

    def set_status(self, status):
        """uses the JSON data in status to update the thing"""
        pass

    def get_description(self):
        say(self.name)
        if self.has_been_visited:
            description_string = self.short_description
            listed_things = []
            # self.get_all_accessible_contents()
            for thing in self.get_all_accessible_contents():
                if thing.has_dynamic_description:
                    description_string += " " + thing.get_dynamic_description()

                if thing.is_listed:
                    listed_things.append(thing)

            num_listed_things = len(listed_things)

            if num_listed_things > 0:
                list_string = " There is"
                list_string += Utilities.list_to_words([o.list_name for o in listed_things])
                list_string += "."
                description_string += list_string

            say(description_string)


        else:
            say(self.long_description)
            self.has_been_visited = True

    def look(self, game, actionargs):
        self.get_description()

    def go(self, game, actionargs):

        direction = actionargs.get("dobj")
        if self.exits.get(direction):
            self.exits[direction].go(game, actionargs)
        else:
            say(self.msg_cannot_go_direction)

    def add_thing(self, thing):
        self.contents.append(thing)

    def remove_thing(self, thing):
        self.contents.remove(thing)

    def get_all_contents(self):
        """return ALL contents, including those that are not accessible"""
        all_contents_list = self.contents.copy()
        for item in self.contents:
            if hasattr(item, "contents"):
                all_contents_list.extend(item.contents)

        return all_contents_list

    def get_all_accessible_contents(self):
        """return ALL contents, including those that are not accessible"""
        all_contents_list = []
        for item in self.contents:
            if item.is_accessible:
                all_contents_list.append(item)
                if hasattr(item, "contents") and item.contents_accessible:
                    for subitem in item.contents:
                        if subitem.is_accessible:
                            all_contents_list.append(subitem)
        return all_contents_list

# OLD Room.py just in case
#
# import os
# import json
# import Exit
# import Feature
#
# class Room:
# 	def __init__(self, data, state):
# 		self.data = data.copy()
# 		self.state = state.copy()
#
# 	def get_prompt(self, game):
# 		if not self.state['visited']:
# 			prompt = self.data["long_description"]
# 			self.state['visited'] = True
# 		else:
# 			prompt = self.data["short_description"]
#
# 		for itm in self.state["items"]:
# 			obj = game.objects[itm]
#
# 			if obj.data["static"] == False:
# 				if obj.state["current_state"] in obj.data["message"]:
# 					prompt += ("\n" + obj.data["message"][obj.state["current_state"]])
# 				else:
# 					prompt += ("\n" + obj.data["message"]["default"])
#
# 		return prompt
#
# 	def check_item(self, item):
# 		for itm in self.state["items"]:
# 			if itm == item:
# 				return True
#
# 		return False
#
# 	def remove_item(self, item):
# 		if item in self.state["items"]:
# 			self.state["items"].remove(item)
#
# 	def add_dropped_item(self, item):
# 		self.state["items"].append(item)
#
# 	def get_state_data(self):
# 		return self.state
