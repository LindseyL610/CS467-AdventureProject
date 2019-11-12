from Utilities import say


class Thing:
    """The basic class for all non-Room objects in the game"""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.adjectives = []
        self.alternate_names = []
        # how the item should appear in a list. A book. An apple. A piece of cheese.
        self.list_name = "a " + name

        # Starting Location is a Room
        self.starting_location = None

        self.can_be_taken = False
        self.can_be_read = False
        self.can_be_dropped = False
        self.has_been_taken = False
        self.can_go = False
        self.has_contents = False

        self.has_dynamic_description = False
        self.is_listed = True

        self.is_accessible = True

        ## room or storage of current location
        self.current_location = None

        self.description = "This is a thing."
        self.dynamic_description_text = "There is a thing."

        # Default Text for all messages
        self.msg_take_first = "You take the {} (for the first time).".format(self.name)
        self.msg_take = "You take the {}.".format(self.name)
        self.msg_cannot_take = "You cannot take the {}.".format(self.name)
        self.msg_already_in_inventory = "You already have the {}.".format(self.name)

        self.msg_cannot_read = "There is nothing to read on the {}.".format(self.name)
        self.msg_cannot_be_opened = "{} cannot be opened".format(self.name)

        self.msg_drop = "You drop the {}.".format(self.name)
        self.msg_cannot_drop = "You cannot drop the {}".format(self.name)

        self.msg_cannot_go = "That is not a way you can go."
        self.msg_go = "You go that way."

        # TODO evaluate how these messages should be worded
        self.msg_cannot_put_in = "You cannot do that."
        self.msg_cannot_put_on = "You cannot do that."

        self.msg_cannot_pull = "You cannot pull that."

    def get_status(self):
        """returns the status of a thing in JSON format"""
        pass

    def set_status(self, status):
        """uses the JSON data in status to update the thing"""
        pass

    def get_desc(self):
        """returns the description to be used when looking at the room"""
        return self.description

    def get_dynamic_description(self):
        """returns the description to be used when looking at the room"""
        return self.dynamic_description_text

    # ACTION for look (and look at)
    def look(self, game, actionargs):
        say(self.get_desc())

    # ACTION for read
    def read(self, game, actionargs):
        if self.can_be_read:
            self.look(game, actionargs)
        else:
            say(self.msg_cannot_read)

    def open(self, game, actionargs):
        say(self.msg_cannot_be_opened)

    # ACTION for take
    def take(self, game, actionargs):
        if self.can_be_taken:
            if game.player.is_in_inventory(self):
                say(self.msg_already_in_inventory)
            else:
                # TODO make sure game function is used properly
                game.player.take(self)
                if not self.has_been_taken:
                    self.has_been_taken = True
                    say(self.msg_take_first)
                else:
                    say(self.msg_take)
        else:
            say(self.msg_cannot_take)

    # ACTION for "drop"
    def drop(self, game, actionargs):
        if self.can_be_dropped:
            say(self.msg_drop)
            # TODO make sure game function is used properly
            game.player.drop(self)
        else:
            say(self.msg_cannot_drop)

    def go(self, game, actionargs):
        """Default response for "cannot go" """
        say(self.msg_cannot_go)

    def put_in(self, game, actionargs):
        say(self.msg_cannot_put_in)

    def put_on(self, game, actionargs):
        say(self.msg_cannot_put_on)
        say(self.msg_cannot_put_in)

    def pull(self, game, actionargs):
        say(self.msg_cannot_pull)


class Exit(Thing):
    """Class for object that transports the player to another room."""

    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_go = True
        self.is_listed = False

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


class Floppy(Item):
    """Floppys will need special functionality to handle multiple instances"""
    pass


class Feature(Thing):
    """Not-Takable, Not-Dropable thing"""

    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_taken = False
        self.can_be_dropped = False
        self.msg_cannot_take = "The {} is fixed in place.".format(self.name)


class Input(Feature):
    """A feature that you can input text into (like a keyboard)"""
    # NOTE: We need to decide how we want input to work.
    # Will it just be something you can do at any time with a certain action?
    # Like: "input ANSWER", or "type ANSWER"
    # Or will interacting with an input object give a special prompt?
    # Like: "look at keyboard" -> "this looks like something to type into. What do you want to type?" "ANSWER"
    pass


class Sign(Feature):
    """Readable Feature"""

    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_read = True


class Storage(Feature):
    """Thing that can store other things"""

    def __init__(self, id, name):
        super().__init__(id, name)
        self.contents = []
        self.contents_accessible = True

    def _add_item(self, item):
        self.contents.append(item)


class Container(Storage):
    """Things are stored IN the Container
    If the container is CLOSED things inside are NOT accessible.
    If the container is OPEN things inside ARE accessible
    EXAMPLES: Fridge, Chest
    """

    def __init__(self, id, name):
        super().__init__(id, name)
        self.can_be_opened = True
        self.is_open = True

    def put_in(self, game, actionargs):
        item = actionargs["dobj"]
        game.player.remove_from_inventory(item)
        self._add_item(item)


class Surface(Storage):
    """Things are stored ON the surface
    Things ARE accessible when on the surface
    EXAMPLES: Table, Shelf"""

    def put_on(self, item):
        # game.player.remove_from_inventory(item)
        self._add_item(item)
        say("you put the thing on the thing.")