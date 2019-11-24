from Utilities import say
import Utilities
import Thing
import Room
import json
import Player

ROOM_PREFIX = "RM_"
THINGS = "TH"
SAVE = "SV"
STARTING_ROOM = "A"

# TODO much of this can be greatly cleaned up, even with the basic names/ids of items/exits/rooms
#  of course we also have to add in the special functionality of many elements as well
#####################################
### CREATING ALL THINGS AND ROOMS ###
#####################################

thing_list = {}

# TODO looking at this, I'm not sure of the best format to store thing_list and room_list
#  a list? a dict? looks like I originally set it up as a dict using object id's as keys
def add_by_id(my_dict, new_thing):
    my_dict[new_thing.id] = new_thing


###################################
### CREATING ITEMS AND FEATURES ###
###################################

#say("Creating things and rooms...")

#code removed - TODO add Features, etc

######################
### CREATING EXITS ###
######################

# NOTE: These names should be filled in later, this is just for structure.

say("Creating all exits...")

# Creating exits between A and B
thing_list["A-B"] = Thing.Exit("A-B", "exit A to B")
thing_list["A-B"].description = "The exit from room A to room B."
thing_list["A-B"].msg_go = "You walk through the exit from room A to room B."
thing_list["B-A"] = Thing.Exit("B-A", "exit B to A") # This will likely be removed if there is no way to go back to A
thing_list["B-A"].description = "The exit from room B to room A."
thing_list["B-A"].msg_go = "You walk through the exit from room B to room A."

# Creating exits between B and K
thing_list["B-K"] = Thing.Exit("B-K", "exit B to K")
thing_list["B-K"].description = "The exit from room B to room K."
thing_list["B-K"].msg_go = "You walk through the exit from room B to room K."
thing_list["K-B"] = Thing.Exit("K-B", "exit K to B")
thing_list["K-B"].description = "The exit from room K to room B."
thing_list["K-B"].msg_go = "You walk through the exit from room K to room B."

# Creating exits between B and C
thing_list["B-C"] = Thing.Exit("B-C", "exit B to C")
thing_list["B-C"].description = "The exit from room B to room C."
thing_list["B-C"].msg_go = "You walk through the exit from room B to room C."
thing_list["C-B"] = Thing.Exit("C-B", "exit C to B")
thing_list["C-B"].description = "The exit from room C to room B."
thing_list["C-B"].msg_go = "You walk through the exit from room C to room B."

# Creating exits between B and MP
thing_list["B-MP"] = Thing.Exit("B-MP", "exit B to MP")
thing_list["B-MP"].description = "The exit from room B to room MP."
thing_list["B-MP"].msg_go = "You walk through the exit from room B to room MP."
thing_list["MP-B"] = Thing.Exit("MP-B", "exit MP to B")
thing_list["MP-B"].description = "The exit from room MP to room B."
thing_list["MP-B"].msg_go = "You walk through the exit from room MP to room B."

# Creating exits between C and D
thing_list["C-D"] = Thing.Exit("C-D", "exit C to D")
thing_list["C-D"].description = "The exit from room C to room D."
thing_list["C-D"].msg_go = "You walk through the exit from room C to room D."
thing_list["D-C"] = Thing.Exit("D-C", "exit D to C")
thing_list["D-C"].description = "The exit from room D to room C."
thing_list["D-C"].msg_go = "You walk through the exit from room D to room C."

# Creating exits between D and E
thing_list["D-E"] = Thing.Exit("D-E", "exit D to E")
thing_list["D-E"].description = "The exit from room D to room E."
thing_list["D-E"].msg_go = "You walk through the exit from room D to room E."
thing_list["E-D"] = Thing.Exit("E-D", "exit E to D")
thing_list["E-D"].description = "The exit from room E to room D."
thing_list["E-D"].msg_go = "You walk through the exit from room E to room D."

# Creating exits between D and P1
thing_list["D-P1"] = Thing.Exit("D-P1", "exit D to P1")
thing_list["D-P1"].description = "The exit from room D to room P1."
thing_list["D-P1"].msg_go = "You walk through the exit from room D to room P1."
thing_list["P1-D"] = Thing.Exit("P1-D", "exit P1 to D")
thing_list["P1-D"].description = "The exit from room P1 to room D."
thing_list["P1-D"].msg_go = "You walk through the exit from room P1 to room D."

# Creating exits between E and F
thing_list["E-F"] = Thing.Exit("E-F", "exit E to F")
thing_list["E-F"].description = "The exit from room E to room F."
thing_list["E-F"].msg_go = "You walk through the exit from room E to room F."
thing_list["F-E"] = Thing.Exit("F-E", "exit F to E")
thing_list["F-E"].description = "The exit from room F to room E."
thing_list["F-E"].msg_go = "You walk through the exit from room F to room E."

# Creating exits between E and P2
thing_list["E-P2"] = Thing.Exit("E-P2", "exit E to P2")
thing_list["E-P2"].description = "The exit from room E to room P2."
thing_list["E-P2"].msg_go = "You walk through the exit from room E to room P2."
thing_list["P2-E"] = Thing.Exit("P2-E", "exit P2 to E")
thing_list["P2-E"].description = "The exit from room P2 to room E."
thing_list["P2-E"].msg_go = "You walk through the exit from room P2 to room E."

# Creating exits between F and G
thing_list["F-G"] = Thing.Exit("F-G", "exit F to G")
thing_list["F-G"].description = "The exit from room F to room G."
thing_list["F-G"].msg_go = "You walk through the exit from room F to room G."
thing_list["G-F"] = Thing.Exit("G-F", "exit G to F")
thing_list["G-F"].description = "The exit from room G to room F."
thing_list["G-F"].msg_go = "You walk through the exit from room G to room F."

# Creating exits between F and P3
thing_list["F-P3"] = Thing.Exit("F-P3", "exit F to P3")
thing_list["F-P3"].description = "The exit from room F to room P3."
thing_list["F-P3"].msg_go = "You walk through the exit from room F to room P3."
thing_list["P3-F"] = Thing.Exit("P3-F", "exit P3 to F")
thing_list["P3-F"].description = "The exit from room P3 to room F."
thing_list["P3-F"].msg_go = "You walk through the exit from room P3 to room F."

# Creating exits between G and H
thing_list["G-H"] = Thing.Exit("G-H", "exit G to H")
thing_list["G-H"].description = "The exit from room G to room H."
thing_list["G-H"].msg_go = "You walk through the exit from room G to room H."
thing_list["H-G"] = Thing.Exit("H-G", "exit H to G")
thing_list["H-G"].description = "The exit from room H to room G."
thing_list["H-G"].msg_go = "You walk through the exit from room H to room G."

# Creating exits between H and I
thing_list["H-I"] = Thing.Exit("H-I", "exit H to I")
thing_list["H-I"].description = "The exit from room H to room I."
thing_list["H-I"].msg_go = "You walk through the exit from room H to room I."
thing_list["I-H"] = Thing.Exit("I-H", "exit I to H")
thing_list["I-H"].description = "The exit from room I to room H."
thing_list["I-H"].msg_go = "You walk through the exit from room I to room H."

# Creating exits between H and J
thing_list["H-J"] = Thing.Exit("H-J", "exit H to J")
thing_list["H-J"].description = "The exit from room H to room J."
thing_list["H-J"].msg_go = "You walk through the exit from room H to room J."
thing_list["J-H"] = Thing.Exit("J-H", "exit J to H")
thing_list["J-H"].description = "The exit from room J to room H."
thing_list["J-H"].msg_go = "You walk through the exit from room J to room H."

# Creating exits between H and P4
thing_list["H-P4"] = Thing.Exit("H-P4", "exit H to P4")
thing_list["H-P4"].description = "The exit from room H to room P4."
thing_list["H-P4"].msg_go = "You walk through the exit from room H to room P4."
thing_list["P4-H"] = Thing.Exit("P4-H", "exit P4 to H")
thing_list["P4-H"].description = "The exit from room P4 to room H."
thing_list["P4-H"].msg_go = "You walk through the exit from room P4 to room H."

# Creating exits between J and K
thing_list["J-K"] = Thing.Exit("J-K", "exit J to K")
thing_list["J-K"].description = "The exit from room J to room K."
thing_list["J-K"].msg_go = "You walk through the exit from room J to room K."
thing_list["K-J"] = Thing.Exit("K-J", "exit K to J")
thing_list["K-J"].description = "The exit from room K to room J."
thing_list["K-J"].msg_go = "You walk through the exit from room K to room J."

# Creating exits between J and P5
thing_list["J-P5"] = Thing.Exit("J-P5", "exit J to P5")
thing_list["J-P5"].description = "The exit from room J to room P5."
thing_list["J-P5"].msg_go = "You walk through the exit from room J to room P5."
thing_list["P5-J"] = Thing.Exit("P5-J", "exit P5 to J")
thing_list["P5-J"].description = "The exit from room P5 to room J."
thing_list["P5-J"].msg_go = "You walk through the exit from room P5 to room J."

######################
### CREATING ROOMS ###
######################

room_list = {}

say("Creating all rooms...")

# Creating room A
room_list["A"] = Room.Room("A", "room A")
room_list["A"].long_description = "You are in room A (long description)."
room_list["A"].short_description = "You are in room A (short description)."

# Creating room B
room_list["B"] = Room.Room("B", "room B")
room_list["B"].long_description = "You are in room B (long description)."
room_list["B"].short_description = "You are in room B (short description)."

# Creating room C
room_list["C"] = Room.Room("C", "room C")
room_list["C"].long_description = "You are in the room C (long description)."
room_list["C"].short_description = "You are in the room C (short desciprtion)."

# Creating room D
room_list["D"] = Room.Room("D", "room D")
room_list["D"].long_description = "You are in room D (long description)."
room_list["D"].short_description = "You are in room D (short description)."

# Creating room E
room_list["E"] = Room.Room("E", "room E")
room_list["E"].long_description = "You are in room E (long description)."
room_list["E"].short_description = "You are in room E (short description)."

# Creating room F
room_list["F"] = Room.Room("F", "room F")
room_list["F"].long_description = "You are in room F (long description)."
room_list["F"].short_description = "You are in room F (short description)."

# Creating room G
room_list["G"] = Room.Room("G", "room G")
room_list["G"].long_description = "You are in room G (long description)."
room_list["G"].short_description = "You are in room G (short description)."

# Creating room H
room_list["H"] = Room.Room("H", "room H")
room_list["H"].long_description = "You are in room H (long description)."
room_list["H"].short_description = "You are in room H (short description)."

# Creating room I
room_list["I"] = Room.Room("I", "room I")
room_list["I"].long_description = "You are in room I (long description)."
room_list["I"].short_description = "You are in room I (short description)."

# Creating room J
room_list["J"] = Room.Room("J", "room J")
room_list["J"].long_description = "You are in room J (long description)."
room_list["J"].short_description = "You are in room J (short description)."

# Creating room K
room_list["K"] = Room.Room("K", "room K")
room_list["K"].long_description = "You are in room K (long description)."
room_list["K"].short_description = "You are in room K (short description)."

# Creating room P1
room_list["P1"] = Room.Room("P1", "puzzle 1")
room_list["P1"].long_description = "You are in puzzle 1 (long description)."
room_list["P1"].short_description = "You are in puzzle 1 (short description)."

# Creating room P2
room_list["P2"] = Room.Room("P2", "puzzle 2")
room_list["P2"].long_description = "You are in puzzle 2 (long description)."
room_list["P2"].short_description = "You are in puzzle 2 (short description)."

# Creating room P3
room_list["P3"] = Room.Room("P3", "puzzle 3")
room_list["P3"].long_description = "You are in puzzle 3 (long description)."
room_list["P3"].short_description = "You are in puzzle 3 (short description)."

# Creating room P4
room_list["P4"] = Room.Room("P4", "puzzle 4")
room_list["P4"].long_description = "You are in puzzle 4 (long description)."
room_list["P4"].short_description = "You are in puzzle 4 (short description)."

# Creating room P5
room_list["P5"] = Room.Room("P5", "puzzle 5")
room_list["P5"].long_description = "You are in puzzle 5 (long description)."
room_list["P5"].short_description = "You are in puzzle 5 (short description)."

# Creating room MP
room_list["MP"] = Room.Room("MP", "meta puzzle")
room_list["MP"].long_description = "You are in the meta puzzle (long description)."
room_list["MP"].short_description = "You are in the meta puzzle (short description)."

##############################
### LINKING THINGS & ROOMS ###
##############################

say("Linking exits and rooms...")

thing_list["A-B"].destination = room_list["B"]
room_list["A"].exits["north"] = thing_list["A-B"]
thing_list["B-A"].destination = room_list["A"]
room_list["B"].exits["south"] = thing_list["B-A"]

thing_list["B-K"].destination = room_list["K"]
room_list["B"].exits["west"] = thing_list["B-K"]
thing_list["K-B"].destination = room_list["B"]
room_list["K"].exits["east"] = thing_list["K-B"]

thing_list["B-C"].destination = room_list["C"]
room_list["B"].exits["east"] = thing_list["B-C"]
thing_list["C-B"].destination = room_list["B"]
room_list["C"].exits["west"] = thing_list["C-B"]

thing_list["B-MP"].destination = room_list["MP"]
room_list["B"].exits["north"] = thing_list["B-MP"]
thing_list["MP-B"].destination = room_list["B"]
room_list["MP"].exits["south"] = thing_list["MP-B"]

thing_list["C-D"].destination = room_list["D"]
room_list["C"].exits["north"] = thing_list["C-D"]
thing_list["D-C"].destination = room_list["C"]
room_list["D"].exits["south"] = thing_list["D-C"]

thing_list["D-E"].destination = room_list["E"]
room_list["D"].exits["north"] = thing_list["D-E"]
thing_list["E-D"].destination = room_list["D"]
room_list["E"].exits["south"] = thing_list["E-D"]

thing_list["D-P1"].destination = room_list["P1"]
room_list["D"].exits["west"] = thing_list["D-P1"]
thing_list["P1-D"].destination = room_list["D"]
room_list["P1"].exits["east"] = thing_list["P1-D"]

thing_list["E-F"].destination = room_list["F"]
room_list["E"].exits["north"] = thing_list["E-F"]
thing_list["F-E"].destination = room_list["E"]
room_list["F"].exits["south"] = thing_list["F-E"]

thing_list["E-P2"].destination = room_list["P2"]
room_list["E"].exits["west"] = thing_list["E-P2"]
thing_list["P2-E"].destination = room_list["E"]
room_list["P2"].exits["east"] = thing_list["P2-E"]

thing_list["F-G"].destination = room_list["G"]
room_list["F"].exits["west"] = thing_list["F-G"]
thing_list["G-F"].destination = room_list["F"]
room_list["G"].exits["east"] = thing_list["G-F"]

thing_list["F-P3"].destination = room_list["P3"]
room_list["F"].exits["south"] = thing_list["F-P3"]
thing_list["P3-F"].destination = room_list["F"]
room_list["P3"].exits["north"] = thing_list["P3-F"]

thing_list["G-H"].destination = room_list["H"]
room_list["G"].exits["south"] = thing_list["G-H"]
thing_list["H-G"].destination = room_list["G"]
room_list["H"].exits["north"] = thing_list["H-G"]

thing_list["H-I"].destination = room_list["I"]
room_list["H"].exits["south"] = thing_list["H-I"]
thing_list["I-H"].destination = room_list["H"]
room_list["I"].exits["north"] = thing_list["I-H"]

thing_list["H-J"].destination = room_list["J"]
room_list["H"].exits["west"] = thing_list["H-J"]
thing_list["J-H"].destination = room_list["H"]
room_list["J"].exits["east"] = thing_list["J-H"]

thing_list["H-P4"].destination = room_list["P4"]
room_list["H"].exits["east"] = thing_list["H-P4"]
thing_list["P4-H"].destination = room_list["H"]
room_list["P4"].exits["west"] = thing_list["P4-H"]

thing_list["J-K"].destination = room_list["K"]
room_list["J"].exits["south"] = thing_list["J-K"]
thing_list["K-J"].destination = room_list["J"]
room_list["K"].exits["north"] = thing_list["K-J"]

thing_list["J-P5"].destination = room_list["P5"]
room_list["J"].exits["north"] = thing_list["J-P5"]
thing_list["P5-J"].destination = room_list["J"]
room_list["P5"].exits["south"] = thing_list["P5-J"]

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
	f = open (THINGS, "w")
	f.truncate(0)
	json.dump(thing_data, f)
	f.close()

	print(thing_data)

	# Put Room data into separate files
	for room in room_list:
		room_obj = json.loads(room_list[room].get_status())

		file_name = ROOM_PREFIX + room_obj["id"]
		f = open (file_name, "w")
		f.truncate(0)
		json.dump(room_obj, f)
		f.close()
		
		print(room_obj)


generate_data_files(thing_list, room_list)
generate_blank_save(thing_list, room_list)

#TESTING#

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
