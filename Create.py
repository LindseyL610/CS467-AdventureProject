from Utilities import say
import Utilities
import Thing
import Room
import json
import Player

ROOM_PREFIX = "RM_"
THINGS = "TH"
SAVE = "SV"
STARTING_ROOM = "roomA"

# TODO much of this can be greatly cleaned up, even with the basic names/ids of items/exits/rooms
#  of course we also have to add in the special functionality of many elements as well
#####################################
### CREATING ALL THINGS AND ROOMS ###
#####################################

thing_list = dict()


# TODO looking at this, I'm not sure of the best format to store thing_list and room_list
#  a list? a dict? looks like I originally set it up as a dict using object id's as keys
def add_by_id(my_dict, new_thing):
    my_dict[new_thing.id] = new_thing


###################################
### CREATING ITEMS AND FEATURES ###
###################################

say("Creating things and rooms...")

# Creating book
thing_list["book"] = Thing.Book("book", "book")
thing_list["book"].description = "This ancient book has the word \"Documentation\" printed on its cover. " \
                                 "Its contents are as follows: blah blah blah"
thing_list["book"].alternate_names.append("tome")

# Creating pedestal
thing_list["pedestal"] = Thing.Surface("pedestal", "pedestal")
thing_list["pedestal"].description = "A pedestal."

# Creating balcony keyboard
thing_list["balconyKeypad"] = Thing.InputBalconyWindow("balconyKeypad", "keypad")
thing_list["balconyKeypad"].description = "A keypad is on the wall next to the window. " \
                                          "It has buttons to enter letters and spaces."
thing_list["balconyKeypad"].msg_prompt = "What do you enter on the keypad?"
thing_list["balconyKeypad"].answer = "hello world"
thing_list["balconyKeypad"].msg_correct_answer = "After a brief pause, the window swings open, " \
                                                 "narrowly missing you! You now see more of a " \
                                                 "dimly lit room within the tower."

# Creating Tower
thing_list["tower"] = Thing.Feature("tower", "tower")
thing_list["tower"].description = "It appears to be a humongous computer tower. " \
                                  "Various wires extend from behind it going all directions. " \
                                  "Several seem to connect to the large wall of circuitry containing an ornate door. " \
                                  "There are five slots on the front of the tower."

# Creating fridge
thing_list["refrigerator"] = Thing.Container("refrigerator", "refrigerator")
thing_list["refrigerator"].description = "A refrigerator"
thing_list["refrigerator"].alternate_names.append("fridge")

# Creating test table FOR TESTING
thing_list["testTable"] = Thing.Surface("testTable", "table")
thing_list["testTable"].description = "A table (for testing purposes)."


# Creating coin FOR TESTING
thing_list["coin"] = Thing.Item("coin", "coin")
thing_list["coin"].description = "A gold coin."

# Creating key FOR TESTING
thing_list["key"] = Thing.Item("key", "key")
thing_list["key"].description = "A brass key."

# Creating cheese
thing_list["cheese"] = Thing.Cheese("cheese", "cheese")
thing_list["cheese"].description = "The block of cheese smells quite potent."
thing_list["cheese"].list_name = "some cheese"

# Creating hungryMouse
thing_list["hungryMouse"] = Thing.Feature("hungryMouse", "mouse")
thing_list["hungryMouse"].description = "This mouse is longer than you are tall. It sits calmly in the corner, " \
                                        "silently watching you. Whatever the lever is that is behind it is unreachable."

# Creating eatingMouse
thing_list["eatingMouse"] = Thing.Feature("eatingMouse", "mouse")
thing_list["eatingMouse"].description = "The mouse is sitting in the corner quietly nibbling on it's cheese."

# Creating lever
thing_list["lever"] = Thing.Lever("lever", "lever")
thing_list["lever"].description = "There is some kind of lever on the wall." \
                                  "You cannot reach it with the mouse in the way."

# Creating Floppy
thing_list["floppy"] = Thing.Item("floppy", "floppy")
thing_list["floppy"].description = "This is some type of ancient storage device. It is a thin rectangle of plastic, " \
                                    "with some unkown language written across the top."

# Creating cobwebs
thing_list["cobwebs"] = Thing.Feature("cobwebs", "cobwebs")
thing_list["cobwebs"].description = "Sticky cobwebs cover the walls, celing, " \
                                    "and floors, only getting denser further into the darkness."
thing_list["cobwebs"].list_name = "some cobwebs"

# Creating plaque
thing_list["plaque"] = Thing.Sign("plaque", "plaque")
thing_list["plaque"].description = "A small ornamental plaque. It says... stuff."

######################
### CREATING EXITS ###
######################

# Creating balconyWindowClosed
thing_list["balconyWindowClosed"] = Thing.Exit("balconyWindowClosed", "window")
thing_list["balconyWindowClosed"].description = "A large window. It is too dark to see what is inside."
thing_list["balconyWindowClosed"].can_go = False
thing_list["balconyWindowClosed"].msg_cannot_go = "The window is closed, and you can't see how to open it."
thing_list["balconyWindowClosed"].has_dynamic_description = True
thing_list["balconyWindowClosed"].dynamic_description_text = "There is huge window to the north."

# Creating balconyWindowClosed
thing_list["balconyWindowOpen"] = Thing.Exit("balconyWindowOpen", "window")
thing_list["balconyWindowOpen"].description = "A large window. It is open, and you can see a large room inside."
thing_list["balconyWindowOpen"].msg_go = "You climb through the open window. As you step inside the tower, " \
                                         "the window slams behind you."
thing_list["balconyWindowOpen"].has_dynamic_description = True
thing_list["balconyWindowOpen"].dynamic_description_text = "There is huge open window to the north."

# Creating lobbyWindow
thing_list["lobbyWindow"] = Thing.Exit("lobbyWindow", "window")
thing_list["lobbyWindow"].description = "A large window. It has slammed shut, and there does not " \
                                        "seem to be a way to open it."
thing_list["lobbyWindow"].can_go = False
thing_list["lobbyWindow"].msg_cannot_go = "The window is closed, and there doens't seem " \
                                          "to be any way to open it."

# Creating ornate doorS
thing_list["ornatedoorS"] = Thing.Exit("ornatedoorS", "door")
thing_list["ornatedoorS"].adjectives.append("ornate")
thing_list["ornatedoorS"].description = "A huge ornate door."
thing_list["ornatedoorS"].can_go = False
thing_list["ornatedoorS"].msg_cannot_go = "This door will not open."

# Creating ornate doorN
thing_list["ornatedoorN"] = Thing.Exit("ornatedoorN", "door")
thing_list["ornatedoorN"].description = "This door"
thing_list["ornatedoorN"].msg_cannot_go = ""

# Creating openingN
thing_list["openingN"] = Thing.Exit("openingN", "opening")
thing_list["openingN"].description = "The opening leads to a dark room."
thing_list["openingN"].msg_go = "You cautiously go through the opening."

# Creating openingS
thing_list["openingS"] = Thing.Exit("openingS", "opening")
thing_list["openingS"].description = "Light pours through the opening to the north."
thing_list["openingS"].msg_go = "You quickly walk back through the opening."

# Creating stairsW
thing_list["stairsW"] = Thing.Exit("stairsW", "stairs")
thing_list["stairsW"].description = "A dark staircase leads up and to the east."
thing_list["stairsW"].msg_go = "You ascend the stairs to the east."

# Creating stairsE
thing_list["stairsE"] = Thing.Exit("stairsE", "stairs")
thing_list["stairsE"].description = "A dark staircase leads down and to the west."
thing_list["stairsE"].msg_go = "You descend the stairs to the west."

# Creating hallwayS
thing_list["hallwayS"] = Thing.Exit("hallwayS", "hallway")
thing_list["hallwayS"].description = "This dark hallway leads off to the north." \
                                     "A strange smell seems to be coming through it."
thing_list["hallwayS"].msg_go = "You slowly creep down the hallway."

# Creating hallwayN
thing_list["hallwayN"] = Thing.Exit("hallwayN", "hallway")
thing_list[
    "hallwayN"].description = "This dark hallway leads off to the north. A strange smell seems to be coming through it."
thing_list["hallwayN"].msg_go = "You slowly creep down the hallway."

# Creating secretDoorE
thing_list["secretWall"] = Thing.Exit("secretWall", "wall")
thing_list["secretWall"].description = "A section of this brick wall looks discolored. " \
                                       "But there is nothing else that appears out of the ordinary."
thing_list["secretWall"].msg_go = ""
thing_list["secretWall"].has_dynamic_description = True
thing_list["secretWall"].dynamic_description_text = "There are discolored bricks on the west wall. (DYNAMIC)"
thing_list["secretWall"].adjectives.append("discolored")
thing_list["secretWall"].alternate_names.append("wall")

thing_list["secretWall"].can_go = False
thing_list["secretWall"].msg_cannot_go = "There does not appear to be any way to go this way."

######################
### CREATING ROOMS ###
######################

room_list = dict()

# Creating roomA
room_list["roomA"] = Room.Room("roomA", "Balcony")

room_list[
    "roomA"].long_description = "You slowly open your eyes. You find yourself on the balcony of a humongous tower. " \
                                "You don't remember how you got here, the last thing you remember is sitting " \
                                "in front of your computer. Looking up at the tower makes you dizzy, it seems to " \
                                "extend infinitely into the sky. Looking down over the railing doesn't help either; " \
                                "the tower descends and disappears the clouds. There is a large window to the north " \
                                "that seems to lead inside. To the left of the window is a keypad." \
                                "To the right of the window on the wall is a plaque." \
                                "At the end of the balcony is a stone pedestal, with an large book on top."
room_list["roomA"].short_description = "You are on a balcony outside of a humongous tower that seems to extend " \
                                       "as far as you can see upwards and downwards."

# Creating roomB
room_list["roomB"] = Room.Room("roomB", "Lobby")

room_list["roomB"].long_description = "In this large room, there is some type of large computer tower in " \
                                      "the corner. A huge ornate door is to the north. Stairs ascend to the east. " \
                                      "A large window is to the south."
room_list["roomB"].short_description = "In this large room, there is some type of large computer tower in" \
                                       "the corner. A huge ornate door is to the north. Stairs ascend to the east. " \
                                       "A large window is to the south. "

# Creating roomC
room_list["roomC"] = Room.Room("roomC", "Cooling Room")

room_list[
    "roomC"].long_description = "This room is cold. Like extremely cold. You see tubes coming in and out of the walls " \
                                "and ceiling that seem to be transporting some blue liquid. On the west side of the room " \
                                "is what looks like a refrigerator. There are stairs to the west, " \
                                "a strange smelling hallway to the north, and a dark corridor leading south."
room_list["roomC"].short_description = "You are in a very cold room. There are stairs to the west, " \
                                       "a strange smelling hallway to the north, and a dark corridor leading south."

# Creating roomD
room_list["roomD"] = Room.Room("roomD", "Mouse Pad")

room_list["roomD"].long_description = "As you enter the room, the first thing you notice is the pungent smell. " \
                                      "You are startled to see in the South East corner... a huge mouse! " \
                                      "Scattered about the floor is bits of hay and... debris. " \
                                      "This appears to be the mouse's... dwelling. " \
                                      "It looks like there may be something on the wall behind the mouse, " \
                                      "but it cannot be reached. The rest of the room is empty with walls " \
                                      "made of large stone bricks. On the west wall, " \
                                      "some of the bricks appear discolored."
room_list["roomD"].short_description = "The floor is covered in hay and debris. In the corner sits a gigantic mouse. " \
                                       "It looks like there may be something on the wall behind the mouse."

# Creating roomI
room_list["roomI"] = Room.Room("roomI", "Dark Webs")
room_list["roomI"].long_description = "A dark room... with webs."
room_list["roomI"].short_description = "A dark room with webs."

# Creating roomP1
room_list["roomP1"] = Room.Room("roomP1", "Monitor Station")
room_list["roomP1"].long_description = "Monitors everywhere."
room_list["roomP1"].short_description = "So many monitors."

# Creating roomMP
room_list["roomMP"] = Room.Room("roomMP", "Motherboard")
room_list["roomMP"].long_description = "The final challenge."
room_list["roomMP"].short_description = "The final challenge."

##############################
### LINKING THINGS & ROOMS ###
##############################

say("Linking things and rooms...")

# linking roomA stuff

# TODO once storage is set up, put book on pedestal
thing_list["pedestal"].add_item(thing_list["book"])
# room_list["roomA"].add_thing(thing_list["book"])

room_list["roomA"].add_thing(thing_list["pedestal"])
room_list["roomA"].add_thing(thing_list["plaque"])
room_list["roomA"].add_thing(thing_list["balconyKeypad"])


# thing_list["balconyWindowClosed"].destination = room_list["roomB"]
room_list["roomA"].exits["north"] = thing_list["balconyWindowClosed"]
thing_list["balconyWindowOpen"].destination = room_list["roomB"]

# linking roomB stuff

room_list["roomB"].add_thing(thing_list["tower"])

thing_list["stairsW"].destination = room_list["roomC"]
thing_list["ornatedoorS"].destination = room_list["roomMP"]

# room_list["roomB"].exits["south"] = thing_list["stonedoorN"]
room_list["roomB"].exits["south"] = thing_list["lobbyWindow"]
room_list["roomB"].exits["east"] = thing_list["stairsW"]
room_list["roomB"].exits["up"] = thing_list["stairsW"]
room_list["roomB"].exits["north"] = thing_list["ornatedoorS"]

# linking roomC stuff

# When storage is implemented, something like this will put the cheese in the fridge
# room_list["roomC"].add_thing(thing_list["cheese"])
room_list["roomC"].add_thing(thing_list["refrigerator"])
thing_list["refrigerator"].add_item(thing_list["cheese"])

# !!!! BEGIN EXTRA STUFF FOR TESTING !!!!
room_list["roomC"].add_thing(thing_list["testTable"])
thing_list["testTable"].add_item(thing_list["key"])
room_list["roomC"].add_thing(thing_list["coin"])
# END TESTING
# !!!! END EXTRA STUFF FOR TESTING !!!!


thing_list["stairsE"].destination = room_list["roomB"]
thing_list["hallwayS"].destination = room_list["roomD"]
thing_list["openingN"].destination = room_list["roomI"]

room_list["roomC"].exits["north"] = thing_list["hallwayS"]
room_list["roomC"].exits["south"] = thing_list["openingN"]
room_list["roomC"].exits["west"] = thing_list["stairsE"]
room_list["roomC"].exits["down"] = thing_list["stairsE"]

# linking roomD stuff

room_list["roomD"].add_thing(thing_list["hungryMouse"])
room_list["roomD"].add_thing(thing_list["lever"])
room_list["roomD"].add_thing(thing_list["secretWall"])

thing_list["hallwayN"].destination = room_list["roomC"]

room_list["roomD"].exits["south"] = thing_list["hallwayN"]
room_list["roomD"].exits["west"] = thing_list["secretWall"]

# linking roomI stuff

room_list["roomI"].add_thing(thing_list["cobwebs"])
room_list["roomI"].add_thing(thing_list["floppy"])

thing_list["openingS"].destination = room_list["roomC"]

room_list["roomI"].exits["north"] = thing_list["openingS"]

# linking roomMP stuff

room_list["roomMP"].exits["south"] = thing_list["ornatedoorN"]


def generate_blank_save(thing_list, room_list):
    print("Generating blank save file...")

    save = dict()

    p = Player.Player()
    p.current_room = room_list[STARTING_ROOM]

    player_data = json.loads(p.get_status())

    print(player_data)

    save["default"] = dict()
    save["default"]["player"] = player_data
    save["saves"] = dict()
    save["save_ctr"] = 0

    f = open(SAVE, "w")
    f.truncate(0)
    json.dump(save, f)
    f.close()


def generate_data_files(thing_list, room_list):
    print("Generating data files...")

    thing_data = dict()

    # Put all Thing data into one file
    for thing in thing_list:
        thing_data[thing] = json.loads(thing_list[thing].get_status())
    f = open(THINGS, "w")
    f.truncate(0)
    json.dump(thing_data, f)
    f.close()

    print(thing_data)

    # Put Room data into separate files
    for room in room_list:
        room_obj = json.loads(room_list[room].get_status())

        file_name = ROOM_PREFIX + room_obj["id"]
        f = open(file_name, "w")
        f.truncate(0)
        json.dump(room_obj, f)
        f.close()

        print(room_obj)


generate_data_files(thing_list, room_list)
generate_blank_save(thing_list, room_list)

# TESTING#

# say("\n")
# say("\n")
# say("TESTING IN CREATE.PY")

# ACCESSIBILITY TEST
# say("ACCESSIBILITY TEST")
# item_a = Thing.Item("item_a", "item_a")

# item_not_a = Thing.Item("item_not_a", "item_not_a")
# item_not_a.is_accessible = False

# stor_a = Thing.Storage("stor_a", "stor_a")

# stor_not_a = Thing.Storage("stor_no_a", "stor_not_a")
# stor_not_a.contents_accessible = False

# sub_item_a = Thing.Item("sub_item_a", "sub_item_a")
# sub_item_not_a = Thing.Item("sub_item_not_a", "sub_item_not_a")
# sub_item_not_a.is_accessible = False

# sub_item_a2 = Thing.Item("sub_item_a2", "sub_item_a2")
# sub_item_not_a2 = Thing.Item("sub_item_not_a2", "sub_item_not_a2")
# sub_item_not_a2.is_accessible = False

# stor_a.contents.extend([sub_item_a, sub_item_not_a])
# stor_not_a.contents.extend([sub_item_a2, sub_item_not_a2])

# test_room = Room.Room("test_room", "test_room")
# test_room.add_thing(item_a)
# test_room.add_thing(item_not_a)
# test_room.add_thing(stor_a)
# test_room.add_thing(stor_not_a)

# say("all things test")
# thing_list = test_room.get_all_contents()
# for thing in thing_list:
#   say(thing.name)

# say("all accessible things test")
# all_a_things = test_room.get_all_accessible_contents()
# for thing in all_a_things:
#   say(thing.name)


# room description test

# say("room description test")
# thing1 = Thing.Item("thing1", "thing1")
# thing2 = Thing.Item("thing2", "thing2")
# thing2.list_name = "another thing"
# thing3 = Thing.Item("thing3", "thing3")
# thing3.list_name = "an item"
# thing4 = Thing.Item("thing4", "thing4")
# thing4.is_listed = False
# thing4.has_dynamic_description = True
# thing4.dynamic_description_text = "A thing is there... dynamically."
#
# thing5 = Thing.Item("thing5", "thing5")
# thing5.is_listed = False
#
# test_room_desc = Room.Room("test_room_desc", "test_room_desc")
# test_room_desc.long_description = "This is a room with lots of stuff!"
# test_room_desc.short_description = "Remember this room?"
#
# test_room_desc.add_thing(thing1)
# test_room_desc.add_thing(thing2)
# test_room_desc.add_thing(thing3)
#
# test_room_desc.add_thing(thing4)
#
# test_room_desc.get_description()
#
# test_room_desc.get_description()
