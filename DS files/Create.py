from Utilities import say
import Thing
import Room

# TODO much of this can be greatly cleaned up, even with the basic names/ids of items/exits/rooms
#  of course we also have to add in the special functionality of many elements as well
#####################################
### CREATING ALL THINGS AND ROOMS ###
#####################################

all_things = {}

# TODO looking at this, I'm not sure of the best format to store all_things and all_rooms
#  a list? a dict? looks like I originally set it up as a dict using object id's as keys
def add_by_id(my_dict, new_thing):
    my_dict[new_thing.id] = new_thing


###################################
### CREATING ITEMS AND FEATURES ###
###################################

# Creating book
say("Creating book")
book = Thing.Item("book", "book")
add_by_id(all_things, book)
book.description = "This ancient book has the word \"Documentation\" printed on its cover. " \
                   "Its contents are as follows: blah blah blah"

book.can_be_read = True
book.can_be_dropped = False
book.msg_cannot_drop = "This book of documentation seems too important to leave behind."

# Creating pedestal
say("Creating pedestal")
pedestal = Thing.Surface("pedestal", "pedestal")
add_by_id(all_things, pedestal)
pedestal.description = "A pedestal"

# Creating Tower
say("Creating tower")
tower = Thing.Feature("tower", "tower")
add_by_id(all_things, tower)
tower.description = "It appears to be a humongous computer tower. " \
                    "Various wires extend from behind it going all directions. " \
                    "Several seem to connect to the large wall of circuitry containing an ornate door. " \
                    "There are five slots on the front of the tower."

# Creating fridge
say("Creating refrigerator")
refrigerator = Thing.Container("refrigerator", "refrigerator")
add_by_id(all_things, refrigerator)
refrigerator.description = "A refrigerator"

# Creating cheese
say("Creating cheese")
cheese = Thing.Item("cheese", "cheese")
add_by_id(all_things, cheese)

cheese.description = "The block of cheese smells quite potent."

# Creating mouse
say("Creating mouse")
mouse = Thing.Feature("mouse", "mouse")
add_by_id(all_things, mouse)

mouse.description = "This mouse is longer than you are tall. It sits calmly in the corner, " \
                    "silently watching you. Whatever the lever is that is behind it is unreachable."

# Creating lever
say("Creating lever")
lever = Thing.Feature("lever", "lever")
add_by_id(all_things, lever)

lever.description = "There is some kind of lever on the wall. You cannot reach it with the mouse in the way."

# Creating Floppy1
say("Creating floppy1")
floppy1 = Thing.Floppy("floppy1", "floppy")
add_by_id(all_things, floppy1)

floppy1.description = "This is some type of ancient storage device. It is a thin rectangle of plastic, " \
                      "with some unkown language written across the top."

# Creating cobwebs
say("Creating cobweb")
cobwebs = Thing.Feature("cobwebs", "cobwebs")
add_by_id(all_things, cobwebs)

cobwebs.description = "Sticky cobwebs cover the walls, celing, " \
                      "and floors, only getting denser further into the darkness."

# Creating plaque
say("Creating plaque")
plaque = Thing.Sign("plaque", "plaque")
add_by_id(all_things, plaque)

plaque.description = "A small ornamental plaque. It says... stuff."

######################
### CREATING EXITS ###
######################

# Creating stone doorS
say("Creating stone door S")
stonedoorS = Thing.Exit("stonedoorS", "door")
add_by_id(all_things, stonedoorS)

stonedoorS.adjectives.append("stone")
stonedoorS.description = "A huge stone door."
stonedoorS.msg_go = "You walk through the open stone door. Just after you pass through, " \
                    "the door crumbles into a huge pile of rubble. "

# Creating stone doorN
say("Creating stone door N")
stonedoorN = Thing.Exit("stonedoorN", "door")
add_by_id(all_things, stonedoorN)

stonedoorN.can_go = False
stonedoorN.adjectives.append("stone")
stonedoorN.description = "What used to be a large stone door is now a pile of rubble. You cannot pass through it."
stonedoorN.msg_cannot_go = "The rubble blocks your way. You cannot return to the balcony."

# Creating ornate doorS
say("Creating ornate door S")
ornatedoorS = Thing.Exit("ornatedoorS", "door")
add_by_id(all_things, ornatedoorS)

ornatedoorS.adjectives.append("ornate")
ornatedoorS.description = "A huge ornate door."
ornatedoorS.can_go = False
ornatedoorS.msg_cannot_go = "This door will not open."

# Creating ornate doorN
say("Creating ornate door N")
ornatedoorN = Thing.Exit("ornatedoorN", "door")
add_by_id(all_things, ornatedoorN)

ornatedoorN.description = "This door"
ornatedoorN.msg_cannot_go = ""

# Creating openingN
say("Creating openingN")
openingN = Thing.Exit("openingN", "opening")
add_by_id(all_things, openingN)

openingN.description = "The opening leads to a dark room."
openingN.msg_go = "You cautiously go through the opening."

# Creating openingS
say("Creating openingS")
openingS = Thing.Exit("openingS", "opening")
add_by_id(all_things, openingS)

openingS.description = "Light pours through the opening to the north."
openingS.msg_go = "You quickly walk back through the opening."

# Creating stairsW
say("Creating stairsW")
stairsW = Thing.Exit("stairsW", "stairs")
add_by_id(all_things, stairsW)

stairsW.description = "A dark staircase leads up and to the east."
stairsW.msg_go = "You ascend the stairs to the east."

# Creating stairsE
say("Creating stairsE")
stairsE = Thing.Exit("stairsE", "stairs")
add_by_id(all_things, stairsE)

stairsE.description = "A dark staircase leads down and to the west."
stairsE.msg_go = "You descend the stairs to the west."

# Creating hallwayS
say("Creating hallwayS")
hallwayS = Thing.Exit("hallwayS", "hallway")
add_by_id(all_things, hallwayS)

hallwayS.description = "This dark hallway leads off to the north. A strange smell seems to be coming through it."
hallwayS.msg_go = "You slowly creep down the hallway."

# Creating hallwayN
say("Creating hallwayN")
hallwayN = Thing.Exit("hallwayN", "hallway")
add_by_id(all_things, hallwayN)

hallwayN.description = "This dark hallway leads off to the north. A strange smell seems to be coming through it."
hallwayN.msg_go = "You slowly creep down the hallway."

# Creating secretDoorE
say("Creating secretDoorE")
secretWall = Thing.Exit("secretWall", "wall")
add_by_id(all_things, secretWall)

secretWall.description = "A section of this brick wall looks discolored. " \
                         "But there is nothing else that appears out of the ordinary."
secretWall.msg_go = ""
secretWall.has_dynamic_description = True
secretWall.dynamic_description_text = "There are discolored bricks on the west wall. (DYNAMIC)"
secretWall.adjectives.append("discolored")
secretWall.alternate_names.append("wall")

secretWall.can_go = False
secretWall.msg_cannot_go = "There does not appear to be any way to go this way."

######################
### CREATING ROOMS ###
######################

all_rooms = {}

# Creating roomA
say("Creating roomA")
roomA = Room.Room("roomA", "Balcony")
add_by_id(all_rooms, roomA)

roomA.long_description = "You slowly open your eyes. You find yourself on the balcony of a humongous tower. " \
                         "You don't remember how you got here, the last thing you remember is sitting " \
                         "in front of your computer. Looking up at the tower makes you dizzy, it seems to " \
                         "extend infinitely into the sky. Looking down over the railing doesn't help either; " \
                         "the tower descends and disappears the clouds. There is a large stone door to the north " \
                         "that seems to lead inside. To its right is a pedestal with some type of book " \
                         "sitting on it. On the wall is a plaque."
roomA.short_description = "You are on a balcony outside of a humongous tower that seems to extend " \
                          "as far as you can see upwards and downwards."

# Creating roomB
say("Creating roomB")
roomB = Room.Room("roomB", "Lobby")
add_by_id(all_rooms, roomB)

roomB.long_description = "In this large room, there is some type of large computer tower in the corner. " \
                         "A huge ornate door is to the north. Stairs ascend to the east. "
roomB.short_description = "In this large room, there is some type of large computer tower in the corner. " \
                          "A huge ornate door is to the north. Stairs ascend to the east. "

# Creating roomC
say("Creating roomC")
roomC = Room.Room("roomC", "Cooling Room")
add_by_id(all_rooms, roomC)

roomC.long_description = "This room is cold. Like extremely cold. You see tubes coming in and out of the walls " \
                         "and ceiling that seem to be transporting some blue liquid. On the west side of the room " \
                         "is what looks like a refrigerator. There are stairs to the west, " \
                         "a strange smelling hallway to the north, and a dark corridor leading south."
roomC.short_description = "You are in a very cold room. There are stairs to the west, " \
                          "a strange smelling hallway to the north, and a dark corridor leading south."

# Creating roomD
say("Creating roomD")
roomD = Room.Room("roomD", "Mouse Pad")
add_by_id(all_rooms, roomD)

roomD.long_description = "As you enter the room, the first thing you notice is the pungent smell. " \
                         "You are startled to see in the South East corner... a huge mouse! " \
                         "Scattered about the floor is bits of hay and... debris. " \
                         "This appears to be the mouse's... dwelling. " \
                         "It looks like there may be something on the wall behind the mouse, " \
                         "but it cannot be reached. The rest of the room is empty with walls " \
                         "made of large stone bricks. On the west wall, " \
                         "some of the bricks appear discolored."
roomD.short_description = "The floor is covered in hay and debris. In the corner sits a gigantic mouse. " \
                          "It looks like there may be something on the wall behind the mouse."

# Creating roomI
say("Creating roomI")
roomI = Room.Room("roomI", "Dark Webs")
add_by_id(all_rooms, roomI)

roomI.long_description = "A dark room... with webs."
roomI.short_description = "A dark room with webs."

# Creating roomP1
say("Creating roomP1")
roomP1 = Room.Room("roomP1", "Monitor Station")
add_by_id(all_rooms, roomP1)

roomP1.long_description = "Monitors everywhere."
roomP1.short_description = "So many monitors."

# Creating roomMP
say("Creating roomMP")
roomMP = Room.Room("roomMP", "Motherboard")
add_by_id(all_rooms, roomMP)

roomMP.long_description = "The final challenge."
roomMP.short_description = "The final challenge."

##############################
### LINKING THINGS & ROOMS ###
##############################

say("\n")
say("Linking Things")

# linking roomA stuff

pedestal._add_item(book)

roomA.add_thing(pedestal)
roomA.add_thing(plaque)

stonedoorS.destination = roomB
roomA.exits["north"] = stonedoorS

# linking roomB stuff

roomB.add_thing(tower)

stairsW.destination = roomC
ornatedoorS.destination = roomMP

roomB.exits["south"] = stonedoorN
roomB.exits["east"] = stairsW
roomB.exits["up"] = stairsW
roomB.exits["north"] = ornatedoorS

# linking roomC stuff

refrigerator._add_item(cheese)

roomC.add_thing(refrigerator)

stairsE.destination = roomB
hallwayS.destination = roomD
openingN.destination = roomI

roomC.exits["north"] = hallwayS
roomC.exits["south"] = openingN
roomC.exits["west"] = stairsE
roomC.exits["down"] = stairsE

# linking roomD stuff

roomD.add_thing(mouse)
roomD.add_thing(lever)
roomD.add_thing(secretWall)

hallwayN.destination = roomC

roomD.exits["south"] = hallwayN
roomD.exits["west"] = secretWall

# linking roomI stuff

roomI.add_thing(cobwebs)
roomI.add_thing(floppy1)

openingS.destination = roomC

roomI.exits["north"] = openingS

# linking roomMP stuff

roomMP.exits["south"] = ornatedoorN


#TESTING#

say("\n")
say("\n")
say("TESTING IN CREATE.PY")
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
# all_things = test_room.get_all_contents()
# for thing in all_things:
#   say(thing.name)

# say("all accessible things test")
# all_a_things = test_room.get_all_accessible_contents()
# for thing in all_a_things:
#   say(thing.name)


# room description test

say("room description test")
thing1 = Thing.Item("thing1", "thing1")
thing2 = Thing.Item("thing2", "thing2")
thing2.list_name = "another thing"
thing3 = Thing.Item("thing3", "thing3")
thing3.list_name = "an item"
thing4 = Thing.Item("thing4", "thing4")
thing4.is_listed = False
thing4.has_dynamic_description = True
thing4.dynamic_description_text = "A thing is there... dynamically."

thing5 = Thing.Item("thing5", "thing5")
thing5.is_listed = False

test_room_desc = Room.Room("test_room_desc", "test_room_desc")
test_room_desc.long_description = "This is a room with lots of stuff!"
test_room_desc.short_description = "Remember this room?"

test_room_desc.add_thing(thing1)
test_room_desc.add_thing(thing2)
test_room_desc.add_thing(thing3)

test_room_desc.add_thing(thing4)

test_room_desc.get_description()

test_room_desc.get_description()
