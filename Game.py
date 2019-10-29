import textwrap

#temp function to display message
def say(string):
    print(textwrap.fill(string))
    # print string


# Temporary Player and Game classes for testing
class Player:
    def __init__(self):
        self.name = "NAME"
        self.inventory = []
        self.current_room = None

    def take(self, thing):
        say("[[player takes {}]]".format(thing.name))

    def drop(self, thing):
        say("[[player drops {}]]".format(thing.name))

    def go(self, destination):
        say("[[player goes to room {}]]".format(destination.name))
        destination.description()

class Game:
    def __init__(self):
        self.player = Player()
        self.room_list = {}
        self.thing_list = {}