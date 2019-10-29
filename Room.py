from Game import say

class Room:
    """Basic Room class"""
    def __init__(self, id, name):
        self.id = id
        self.name= name
        self.long_description = ""
        self.short_description = ""
        self.exits = {"north" : None,
                      "east" : None,
                      "south" : None,
                      "west" : None}

        self.has_been_visited = False
        self.contents = []

        self.msg_cannot_go_direction = "You cannot go that direction."

    def description(self):
        say(self.name)
        if self.has_been_visited:
            say(self.short_description)
        else:
            say(self.long_description)
            self.has_been_visited = True

        for object in self.contents:
            say("There is a {}.".format(object.name))


    def go(self, game, actionargs):

        direction = actionargs.get("dobj")
        if self.exits.get(direction):
            self.exits[direction].go(game, actionargs)
        else:
            say(self.msg_cannot_go_direction)

    def add_thing(self, thing):
        self.contents.append(thing)

    def get_all_contents(self):
        """return ALL contents, including those that are not accessible"""
        pass

    def get_all_accessible_contents(self):
        """return all contents that are accessible"""
        pass
