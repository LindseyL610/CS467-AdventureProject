from Game import say

class Thing:
    """The basic class for all non-Room objects in the game"""

    def __init__(self, id, name):
        self.id = id
        self.name= name
        self.adjectives = []
        self.alternate_names = []

        # Starting Location is a Room
        self.starting_location = None

        self.can_be_taken = False
        self.can_be_read = False
        self.can_be_dropped = False
        self.has_been_taken = False
        self.can_go = False

        self.is_accessible = True

        ## ID of room of current location
        self.current_location = None

        self.description = "This is a thing."

        # Default Text for all messages
        self.msg_take_first = "You take the {} (for the first time).".format(self.name)
        self.msg_take = "You take the {}.".format(self.name)

        self.msg_cannot_read = "There is nothing to read on the {}.".format(self.name)
        self.msg_cannot_be_opened = "{} cannot be opened".format(self.name)

        self.msg_drop = "You drop the {}.".format(self.name)
        self.msg_cannot_drop = "You cannot drop the {}".format(self.name)

        self.msg_cannot_go = "That is not a way you can go."
        self.msg_go = "You go that way."

    def get_desc(self):
        return self.description

    def get_name(self):
        return self.name

    #ACTION for look (and look at)
    def look(self, game, actionargs):
        say(self.get_desc())

    #ACTION for read
    def read(self, game, actionargs):
        if self.can_be_read:
            self.look(game, actionargs)
        else:
            say(self.msg_cannot_read)

    def open(self, game, actionargs):
        say(self.msg_cannot_be_opened)


    #ACTION for take
    def take(self, game, actionargs):
        if self.can_be_taken:
            # TODO make sure game function is used properly
            game.player.take(self)
            if not self.has_been_taken:
                self.has_been_taken = True
                say(self.msg_take_first)
            else:
                say(self.msg_take)
        else:
            say("You cannot take {}.".format(self.name))

    #ACTION for "drop"
    def drop(self, game, actionargs):
        if self.can_be_dropped:
            say(self.msg_drop)
            # TODO make sure game function is used properly
            game.player.drop(self)
        else:
            say(self.msg_cannot_drop)

    def go(self, game, actionargs):
        say(self.msg_cannot_go)


class Exit(Thing):
    """Class for object that transports the player to another room."""
    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_go = True

        self.destination = None

    def go(self, game, actionargs):
        if self.can_go:
            say(self.msg_go)
            # TODO make sure game function is used properly
            game.player.go(self.destination)
        else:
            say(self.msg_cannot_go)

class Door(Exit):
    """A special Exit, doors can be closed, locked, and unlocked"""
    pass

# class Door(Exit):
#     is_lockable = False
#     is_locked = False
#     is_open = True
#     will_unlock = []
#     message_unlocked = "The door is already unlocked."
#     message_locked = "The door is locked"
#     message_cant_unlock = "That can't unlock the door."
#     message_unlocked = "The door is unlocked."
#     message_not_lockable = "This door does not lock."
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name= name
#         self.adjectives = []
#         self.alternate_names = []
#         self.actions = {}
#
#     def unlock(self, object_id):
#         if not self.is_lockable:
#             say(self.message_not_lockable)
#         elif not self.is_locked:
#             say(self.message_unlocked)
#         elif object not in self.will_unlock:
#             say(self.message_cant_unlock)
#         else:
#             say(self.message_unlocked)
#             self.is_locked = False
#
#     def go(self):
#         if self.is_locked:
#             say(self.message_locked)
#


# class MultiKeyDoor(Door):
#     number_of_keys = 0
#     keys_to_unlock = 5
#
#
#     def get_description(self):
#         if
#
#

class Item(Thing):
    """Takable, Dropable thing"""
    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_taken = True
        self.can_be_dropped = True

class Feature(Thing):
    """Not-Takable, Not-Dropable thing"""
    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_taken = False
        self.can_be_dropped = False

class Sign(Feature):
    """Readable Feature"""
    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_read = True

class Storage(Feature):
    """Thing that can store other things"""
    pass

class Container(Storage):
    """Things are stored IN the Container
    If the container is CLOSED things inside are NOT accessible.
    If the container is OPEN things inside ARE accessible
    EXAMPLES: Fridge, Chest
    """
    pass

class Surface(Storage):
    """Things are stored ON the surface
    Things ARE accessible when on the surface
    EXAMPLES: Table, Shelf"""
    pass
