from Game import say, Game
import Thing
from Room import Room


### CREATING THINGS ###

all_things = {}
def add_by_id(my_dict, new_thing):
    my_dict[new_thing.id] = new_thing




#Creating sign
say("Creating sign")
sign = Thing.Sign("sign", "sign")
add_by_id(all_things, sign)

sign.description = "The sign says: Watch for Falling Rocks."

#Creating cheese
say("Creating cheese")
cheese = Thing.Item("cheese", "cheese")
add_by_id(all_things, cheese)

cheese.description = "The block of cheese smells quite potent."

#Creating book
say("Creating book")
book = Thing.Item("book", "book")
add_by_id(all_things, book)
book.description = "This ancient book has the word \"Documentation\" printed on its cover. Its contents are as follows:"

book.can_be_read = True
book.can_be_dropped = False
book.msg_cannot_drop = "This book of documentation seems too important to leave behind."


#Creating hallway
say("Creating hallway")
hallway = Thing.Exit("hallway", "hallway")
add_by_id(all_things, hallway)

hallway.description = "This dark hallway leads off to the north. A strange smell seems to be coming through it."
hallway.msg_go = "You slowly creep down the hallway."

all_rooms = {}

#Creating roomD
say("Creating roomD")
roomD = Room.Room("roomD", "Mouse Pad")
add_by_id(all_rooms, roomD)

roomD.long_description = "As you enter the room, the first thing you notice is the pungent smell." \
                         "You are startled to see in the South East corner... a huge mouse!" \
                         "Scattered about the floor is bits of hay and... debris. " \
                         "This appears to be the mouse's... dwelling." \
                         "It looks like there may be something on the wall behind the mouse," \
                         "but it cannot be reached. The rest of the room is empty with walls" \
                         "made of large stone bricks. On the west wall," \
                         "some of the bricks appear discolored."
roomD.short_description ="The floor is covered in hay and debris. In the corner sits a gigantic mouse." \
                         "It looks like there may be something on the wall behind the mouse." \
                         "There are discolored bricks on the west wall."


#Creating roomC
say("Creating roomC")
roomC = Room.Room("roomC", "Cooling Room")
add_by_id(all_rooms, roomC)

roomC.long_description = "This room is cold. Like extremely cold. You see tubes coming in and out of the walls" \
                         "and ceiling that seem to be transporting some blue liquid. On the west side of the room" \
                         "is what looks like a refrigerator. There are stairs to the west," \
                         "a strange smelling hallway to the north, and a dark corridor leading south."
roomC.short_description ="You are in a very cold room. There are stairs to the west," \
                         "a strange smelling hallway to the north, and a dark corridor leading south."


### LINKING THINGS ###

#linking roomD & hallway
say("\n")
say("Linking Things")
hallway.destination = roomD
roomC.exits["north"] = hallway

print(all_things)
print(all_rooms)