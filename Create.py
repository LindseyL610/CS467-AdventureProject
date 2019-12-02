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

#####################################
### CREATING ALL THINGS AND ROOMS ###
#####################################

thing_list = dict()

###################################
### CREATING ITEMS AND FEATURES ###
###################################

say("Creating things and rooms...")

#ROOM A (Balcony) FEATURES AND ITEMS--------------------------------------
# Creating book
thing_list["book"] = Thing.Book("book", "book")
thing_list["book"].description = "This ancient book has the title \"Tome of Documentation\" printed on its cover. "
thing_list["book"].alternate_names.extend(["tome","documentation"])

# Creating pedestal
thing_list["pedestal"] = Thing.Surface("pedestal", "pedestal")
thing_list["pedestal"].description = "A pedestal."


# Creating plaque
thing_list["plaque"] = Thing.Sign("plaque", "plaque")
thing_list["plaque"].description = \
    "Welcome to Tower Escape, a game by Jason DiMedio, Lindsey Lopian, and Casey Proulx."

# Creating balcony keyboard
thing_list["balconyKeypad"] = Thing.InputBalconyWindow("balconyKeypad", "keypad")
thing_list["balconyKeypad"].description = "A keypad is on the wall next to the window. " \
                                          "It has buttons to enter letters and spaces."
thing_list["balconyKeypad"].alternate_names.extend(["keyboard"])
thing_list["balconyKeypad"].msg_prompt = "What do you enter on the keypad?"
thing_list["balconyKeypad"].answer = "hello world"
thing_list["balconyKeypad"].msg_correct_answer = "After a brief pause, the window swings open, " \
                                                 "narrowly missing you! You now see more of a " \
                                                 "dimly lit room within the tower."


# ROOM B (Lobby) FEATURES AND ITEMS--------------------------------------
# Creating Computer
thing_list["lobbyComputer"] = Thing.Computer("lobbyComputer", "computer")
thing_list["lobbyComputer"].description = \
    "This massive machine takes up most of the east wall. It is some sort of system of large rectangular devices all " \
    "connected with various wires. There are lights blinking, and you hear whirring and clicking sounds. " \
    "You can only assume it functions as some type of computer. " \
    "There appears to be a handful of unique ports in the machine where something could be inserted."
thing_list["lobbyComputer"].alternate_names.extend(["machine"])

thing_list["floppyDisk"] = Thing.Item("floppyDisk", "disk")
thing_list["floppyDisk"].description = \
    "An ancient data storage device."
thing_list["floppyDisk"].alternate_names.extend(["floppy","floppydisk"])

thing_list["cartridge"] = Thing.Item("cartridge", "cartridge")
thing_list["cartridge"].description = \
    "An ancient data storage device."

thing_list["tape"] = Thing.Item("tape", "tape")
thing_list["tape"].description = \
    "This appears to be a form of magnetic tape, used to store data."

thing_list["cd"] = Thing.Item("cd", "CD")
thing_list["cd"].description = \
    "A c.d., once used to store information."
thing_list["cd"].alternate_names.extend(["C.D."])

thing_list["flashdrive"] = Thing.Item("flashdrive", "flashdrive")
thing_list["flashdrive"].description = \
    "A portable storage device."
thing_list["flashdrive"].alternate_names.extend(["drive","usbdrive", "harddrive"])


# ROOM D (Mouse Pad) FEATURES AND ITEMS--------------------------------------
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

#ROOM E (BALLROOM) FEATURES AND ITEMS--------------------------------------
thing_list["wine"] = Thing.Item("wine", "wine")
thing_list["wine"].description = "A bottle of 'Ivory Keyboard' wine. Seems to be a good vintage."
thing_list["wine"].list_name = "a bottle of wine"

thing_list["water"] = Thing.Item("water", "water")
thing_list["water"].description = "A bottle of water."
thing_list["water"].list_name = "a bottle of water"

thing_list["soda"] = Thing.Item("soda", "soda")
thing_list["soda"].description = "A bottle of Mountain Mist soda. It shines brighter than the light of earendil."
thing_list["soda"].list_name = "a bottle of soda"

thing_list["bar"] = Thing.Surface("ballroomBar", "bar")
thing_list["bar"].description = "A fully stocked bar."

thing_list["tipJar"] = Thing.Container("tipJar", "jar")
thing_list["tipJar"].description = "A tip jar next to the piano. There's only one way to fill it..."
thing_list["tipJar"].can_be_opened = False
thing_list["tipJar"].is_open = True
thing_list["tipJar"].contents_accessible = True
thing_list["tipJar"].list_name = "a tip jar"
thing_list["tipJar"].adjectives.extend(["tip"])
#--------------------------------------------------------------------------


# ROOM I (Dark Webs) FEATURES AND ITEMS--------------------------------------
# Creating Floppy
thing_list["floppy"] = Thing.Item("floppy", "floppy")
thing_list["floppy"].description = "This is some type of ancient storage device. It is a thin rectangle of plastic, " \
                                    "with some unkown language written across the top."

# Creating cobwebs
thing_list["cobwebs"] = Thing.Feature("cobwebs", "cobwebs")
thing_list["cobwebs"].description = "Sticky cobwebs cover the walls, celing, " \
                                    "and floors, only getting denser further into the darkness."
thing_list["cobwebs"].list_name = "some cobwebs"

# ROOM K (Cooling Room) FEATURES AND ITEMS--------------------------------------

# Creating fridge
thing_list["refrigerator"] = Thing.Container("refrigerator", "refrigerator")
thing_list["refrigerator"].description = "A refrigerator"
thing_list["refrigerator"].alternate_names.extend(["fridge"])


# Creating cheese
thing_list["cheese"] = Thing.Cheese("cheese", "cheese")
thing_list["cheese"].description = "The block of cheese smells quite potent."
thing_list["cheese"].list_name = "some cheese"



# Creating puzzle 1 input
thing_list["puzzle1Keyboard"] = Thing.InputPuzzle1("puzzle1Keyboard", "keyboard")
thing_list["puzzle1Keyboard"].description = "A keyboard."
thing_list["puzzle1Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle1Keyboard"].answer = "answer"
thing_list["puzzle1Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"

# Creating puzzle 2 input
thing_list["puzzle2Keyboard"] = Thing.InputPuzzle2("puzzle2Keyboard", "keyboard")
thing_list["puzzle2Keyboard"].description = "A keyboard."
thing_list["puzzle2Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle2Keyboard"].answer = "answer"
thing_list["puzzle2Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"


# Creating puzzle 3 input
thing_list["puzzle3Keyboard"] = Thing.InputPuzzle3("puzzle3Keyboard", "keyboard")
thing_list["puzzle3Keyboard"].description = "A keyboard."
thing_list["puzzle3Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle3Keyboard"].answer = "answer"
thing_list["puzzle3Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"


# Creating puzzle 1 input
thing_list["puzzle4Keyboard"] = Thing.InputPuzzle4("puzzle4Keyboard", "keyboard")
thing_list["puzzle4Keyboard"].description = "A keyboard."
thing_list["puzzle4Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle4Keyboard"].answer = "answer"
thing_list["puzzle4Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"


# Creating puzzle 1 input
thing_list["puzzle5Keyboard"] = Thing.InputPuzzle5("puzzle5Keyboard", "keyboard")
thing_list["puzzle5Keyboard"].description = "A keyboard."
thing_list["puzzle5Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle5Keyboard"].answer = "answer"
thing_list["puzzle5Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"



######################
### CREATING EXITS ###
######################

# Creating exits between A (Balcony) and B (Lobby) [[WINDOW]]
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

# Creating exits between B (Lobby) and MP (Motherboard) [[ORNATE DOOR]]
# Creating lobbyOrnateDoor
thing_list["lobbyOrnateDoor"] = Thing.MetaDoor("lobbyOrnateDoor", "door")
thing_list["lobbyOrnateDoor"].adjectives.extend(["ornate"])

# Creating motherboardOrnateDoor
thing_list["motherboardOrnateDoor"] = Thing.Exit("motherboardOrnateDoor", "door")
thing_list["motherboardOrnateDoor"].description = "This door"
thing_list["motherboardOrnateDoor"].msg_cannot_go = ""


# Creating exits between B (Lobby) and C (Utilities) [[ORNATE DOOR]]
# Creating lobbyStairs
thing_list["lobbyStairs"] = Thing.Exit("lobbyStairs", "stairs")
thing_list["lobbyStairs"].description = "A dark staircase leads up and to the east."
thing_list["lobbyStairs"].msg_go = "You ascend the stairs to the east."

# Creating utilityStairs
thing_list["utilityStairs"] = Thing.Exit("utilityStairs", "stairs")
thing_list["utilityStairs"].description = "A dark staircase leads down and to the west."
thing_list["utilityStairs"].msg_go = "You descend the stairs to the west."


# Creating exits between C (Utilities) and D (Mousepad) [[HALLWAY]]
# Creating utilityHallway
thing_list["utilityHallway"] = Thing.Exit("utilityHallway", "hallway")
thing_list["utilityHallway"].description = "This dark hallway leads off to the north." \
                                     "A strange smell seems to be coming through it."
thing_list["utilityHallway"].msg_go = "You slowly creep down the hallway."

# Creating mousepadHallway
thing_list["mousepadHallway"] = Thing.Exit("mousepadHallway", "hallway")
thing_list[
    "mousepadHallway"].description = "This dark hallway leads off to the north." \
                                     "A strange smell seems to be coming through it."
thing_list["mousepadHallway"].msg_go = "You slowly creep down the hallway."

# Creating exits between D (Mousepad) and P1 (Monitors) [[BRICKS/ TUNNEL]]


# Creating exits between B and K [[RAMP (OR ESCALATOR?)]]
thing_list["B-K"] = Thing.Exit("B-K", "exit B to K")
thing_list["B-K"].description = "The exit from room B to room K."
thing_list["B-K"].msg_go = "You walk through the exit from room B to room K."
thing_list["K-B"] = Thing.Exit("K-B", "exit K to B")
thing_list["K-B"].description = "The exit from room K to room B."
thing_list["K-B"].msg_go = "You walk through the exit from room K to room B."



# Creating exits between D and E [[STAIRS]]
thing_list["mousepadStairs"] = Thing.Exit("mousepadStairs", "stairs")
thing_list["mousepadStairs"].description = "A staircase leading up and to the north."
thing_list["mousepadStairs"].msg_go = "You ascend the stairs to the north."
thing_list["ballroomStairs"] = Thing.Exit("ballroomStairs", "stairs")
thing_list["ballroomStairs"].description = "A staircase leading down and to the south."
thing_list["ballroomStairs"].msg_go = "You descend the stairs to the south."

# Creating exits between D (Mousepad) and P1 (Monitors) [[BRICKS/ TUNNEL]]

# ToDo This needs to be changed, to disclored bricks/ wall that changes into a new exit: secret passage (tunnel?)
thing_list["secretWall"] = Thing.Exit("secretWall", "wall")
thing_list["secretWall"].description = "A section of this brick wall looks discolored. " \
                                       "But there is nothing else that appears out of the ordinary."
thing_list["secretWall"].msg_go = ""
thing_list["secretWall"].has_dynamic_description = True
thing_list["secretWall"].dynamic_description_text = "There are discolored bricks on the west wall. (DYNAMIC)"
thing_list["secretWall"].adjectives.extend(["discolored"])
thing_list["secretWall"].alternate_names.extend(["wall"])

thing_list["secretWall"].can_go = False
thing_list["secretWall"].msg_cannot_go = "There does not appear to be any way to go this way."

# thing_list["D-P1"] = Thing.Exit("D-P1", "exit D to P1")
# thing_list["D-P1"].description = "The exit from room D to room P1."
# thing_list["D-P1"].msg_go = "You walk through the exit from room D to room P1."
thing_list["P1-D"] = Thing.Exit("P1-D", "exit P1 to D")
thing_list["P1-D"].description = "The exit from room P1 to room D."
thing_list["P1-D"].msg_go = "You walk through the exit from room P1 to room D."

# Creating exits between E and F [[Elevator]]
thing_list["ballroomElevator"] = Thing.Exit("ballroomElevator", "elevator")
thing_list["ballroomElevator"].description = "An elevator stands ready to take you... somewhere. The light inside flickers."
thing_list["ballroomElevator"].msg_go = "You walk into the elevator, and the door closes behind you. You feel heavier. The elevator must be going up."
thing_list["IOroomElevator"] = Thing.Exit("IOroomElevator", "elevator")
thing_list["IOroomElevator"].description = "An elevator stands ready to take you... somewhere. The light inside flickers."
thing_list["IOroomElevator"].msg_go = "You walk into the elevator, and the door closes behind you. You feel lighter. The elevator must be going down."

# Creating exits between E and P2 [[Door]]
thing_list["ballroomDoor"] = Thing.Exit("ballroomDoor", "door")
thing_list["ballroomDoor"].description = "An ordinary door."
thing_list["ballroomDoor"].msg_go = "You proceed through the door to the west."
thing_list["P2Door"] = Thing.Exit("P2Door", "door")
thing_list["P2Door"].description = "An ordinary door."
thing_list["P2Door"].msg_go = "You proceed through the door to the east."

# Creating exits between F and G [[Hallway]]
thing_list["IOroomHallway"] = Thing.Exit("IOroomHallway", "hallway")
thing_list["IOroomHallway"].description = "A long, well-lit hallway leading off to the west."
thing_list["IOroomHallway"].msg_go = "You walk through the hallway to the west."
thing_list["busHallway"] = Thing.Exit("busHallway", "hallway")
thing_list["busHallway"].description = "A long, well-lit hallway leading off to the east."
thing_list["busHallway"].msg_go = "You walk through the hallway to the east."

# Creating exits between F and P3 [[Door]]
thing_list["IOroomDoor"] = Thing.Exit("IOroomDoor", "door")
thing_list["IOroomDoor"].description = "An ordinary door."
thing_list["IOroomDoor"].msg_go = "You proceed through the door to the south."
thing_list["P3Door"] = Thing.Exit("P3Door", "door")
thing_list["P3Door"].description = "An ordinary door."
thing_list["P3Door"].msg_go = "You proceed through the door to the north."

# Creating exits between G and H [[RAMP]]
thing_list["busRamp"] = Thing.Exit("busRamp", "ramp")
thing_list["busRamp"].description = "A ramp leading up and to the south."
thing_list["busRamp"].msg_go = "You walk up the ramp to the south."
thing_list["websRamp"] = Thing.Exit("websRamp", "ramp")
thing_list["websRamp"].description = "A ramp leading down and to the north."
thing_list["websRamp"].msg_go = "You walk up the ramp to the north."

# Creating exits between H (Webs) and I (Dark Webs)  [[OPENING]]

# Creating websOpening
thing_list["websOpening"] = Thing.Exit("websOpening", "opening")
thing_list["websOpening"].description = "The opening leads to a dark room."
thing_list["websOpening"].msg_go = "You cautiously go through the opening."

# Creating darkWebsOpening
thing_list["darkWebsOpening"] = Thing.Exit("darkWebsOpening", "opening")
thing_list["darkWebsOpening"].description = "Light pours through the opening to the north."
thing_list["darkWebsOpening"].msg_go = "You quickly walk back through the opening."

# thing_list["H-I"] = Thing.Exit("H-I", "exit H to I")
# thing_list["H-I"].description = "The exit from room H to room I."
# thing_list["H-I"].msg_go = "You walk through the exit from room H to room I."
# thing_list["I-H"] = Thing.Exit("I-H", "exit I to H")
# thing_list["I-H"].description = "The exit from room I to room H."
# thing_list["I-H"].msg_go = "You walk through the exit from room I to room H."

# Creating exits between H and J  [[STAIRS]]
thing_list["H-J"] = Thing.Exit("H-J", "exit H to J")
thing_list["H-J"].description = "The exit from room H to room J."
thing_list["H-J"].msg_go = "You walk through the exit from room H to room J."
thing_list["J-H"] = Thing.Exit("J-H", "exit J to H")
thing_list["J-H"].description = "The exit from room J to room H."
thing_list["J-H"].msg_go = "You walk through the exit from room J to room H."

# Creating exits between H and P4 [[DOOR]]
thing_list["H-P4"] = Thing.Exit("H-P4", "exit H to P4")
thing_list["H-P4"].description = "The exit from room H to room P4."
thing_list["H-P4"].msg_go = "You walk through the exit from room H to room P4."
thing_list["P4-H"] = Thing.Exit("P4-H", "exit P4 to H")
thing_list["P4-H"].description = "The exit from room P4 to room H."
thing_list["P4-H"].msg_go = "You walk through the exit from room P4 to room H."

# Creating exits between J and K  [[HALLWAY]]
thing_list["J-K"] = Thing.Exit("J-K", "exit J to K")
thing_list["J-K"].description = "The exit from room J to room K."
thing_list["J-K"].msg_go = "You walk through the exit from room J to room K."
thing_list["K-J"] = Thing.Exit("K-J", "exit K to J")
thing_list["K-J"].description = "The exit from room K to room J."
thing_list["K-J"].msg_go = "You walk through the exit from room K to room J."

# Creating exits between J and P5 [[DOOR]]
thing_list["J-P5"] = Thing.Exit("J-P5", "exit J to P5")
thing_list["J-P5"].description = "The exit from room J to room P5."
thing_list["J-P5"].msg_go = "You walk through the exit from room J to room P5."
thing_list["P5-J"] = Thing.Exit("P5-J", "exit P5 to J")
thing_list["P5-J"].description = "The exit from room P5 to room J."
thing_list["P5-J"].msg_go = "You walk through the exit from room P5 to room J."



######################
### CREATING ROOMS ###
######################

room_list = dict()

# Creating roomA
room_list["roomA"] = Room.Room("roomA", "Balcony")

room_list[
    "roomA"].long_description = \
    "You slowly open your eyes. You find yourself on the balcony of a humongous tower. You don't remember " \
    "how you got here, the last thing you remember is sitting in front of your computer. Looking up at the " \
    "tower makes you dizzy, it seems to extend infinitely into the sky. Looking down over the railing " \
    "doesn't help either; the tower descends and disappears the clouds. There is a large window to the north " \
    "that seems to lead inside. To the left of the window is a keypad. To the right of the window on the " \
    "wall is a plaque. At the end of the balcony is a stone pedestal, with an large book on top."
room_list["roomA"].short_description = "You are on a balcony outside of a humongous tower that seems to extend " \
                                       "as far as you can see upwards and downwards."
room_list["roomA"].documentation = "Enter the tower at your own risk, you may find yourself caught " \
                                   "in an infinite loop. " \
                                   "To remedy this, you must discover who you are. " \
                                   "As with most journeys, you may want to start with a simple phrase: " \
                                   "\"Hello World.\""


# Creating roomB
room_list["roomB"] = Room.Room("roomB", "Lobby")

room_list["roomB"].long_description = \
    "As you enter this massive room, the first thing you notice is a huge ornate door across from you on " \
    "the north wall. There are various wires and tubes connecting it to a large machine along the east " \
    "wall. Stairs ascend to the east, and a ramp descends to the west. The window you came in is to the south."
room_list["roomB"].short_description = \
    "In this massive room, there is some type of large computer taking up most of the east wall. " \
    "A huge ornate door is to the north. Stairs ascend to the east. A ramp goes down to the west. " \
    "A large window is to the south. "


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

# Creating roomC
room_list["roomC"] = Room.Room("roomC", "Utility Room")
room_list["roomC"].long_description = "You are in roomC (long description)."
room_list["roomC"].short_description = "You are in roomC (short description)."

# Creating room E
room_list["roomE"] = Room.Room("roomE", "Ballroom")
room_list["roomE"].long_description = "You are in room E (long description)."
room_list["roomE"].short_description = "You are in room E (short description)."

# Creating room F
room_list["roomF"] = Room.Room("roomF", "I/O Room")
room_list["roomF"].long_description = "You are in room F (long description)."
room_list["roomF"].short_description = "You are in room F (short description)."

# Creating room G
room_list["roomG"] = Room.Room("roomG", "Bus Station")
room_list["roomG"].long_description = "You are in room G (long description)."
room_list["roomG"].short_description = "You are in room G (short description)."


# Creating room H
room_list["roomH"] = Room.Room("roomH", "Web")
room_list["roomH"].long_description = "You are in room H (long description)."
room_list["roomH"].short_description = "You are in room H (short description)."



# Creating roomI
room_list["roomI"] = Room.Room("roomI", "Dark Webs")
room_list["roomI"].long_description = "A dark room... with webs."
room_list["roomI"].short_description = "A dark room with webs."



# Creating room J
room_list["roomJ"] = Room.Room("roomJ", "Clock Room")
room_list["roomJ"].long_description = "You are in room J (long description)."
room_list["roomJ"].short_description = "You are in room J (short description)."

# Creating roomK
room_list["roomK"] = Room.Room("roomK", "Cooling Room")

room_list[
    "roomK"].long_description = "This room is cold. Like extremely cold." \
                                "You see tubes coming in and out of the walls " \
                                "and ceiling that seem to be transporting some blue liquid." \
                                "On the west side of the room " \
                                "is what looks like a refrigerator. There are stairs to the west, " \
                                "a strange smelling hallway to the north, and a dark corridor leading south."
room_list["roomK"].short_description = "You are in a very cold room. There are stairs to the west, " \
                                       "a strange smelling hallway to the north, and a dark corridor leading south."





# Creating roomP1
room_list["roomP1"] = Room.Room("roomP1", "Monitor Station")
room_list["roomP1"].long_description = "Monitors everywhere. Also a keyboard."
room_list["roomP1"].short_description = "So many monitors."
room_list["roomP1"].documentation = "The answer is 'answer'."

# Creating room P2
room_list["roomP2"] = Room.Room("roomP2", "puzzle 2 (database)")
room_list["roomP2"].long_description = "You are in puzzle 2 (long description). There is a keyboard."
room_list["roomP2"].short_description = "You are in puzzle 2 (short description)."
room_list["roomP2"].documentation = "The answer is 'answer'."

# Creating room P3
room_list["roomP3"] = Room.Room("roomP3", "puzzle 3 (search/ memory)")
room_list["roomP3"].long_description = "You are in puzzle 3 (long description)."
room_list["roomP3"].short_description = "You are in puzzle 3 (short description)."
room_list["roomP3"].documentation = "The answer is 'answer'."

# Creating room P4
room_list["roomP4"] = Room.Room("roomP4", "puzzle 4 (cpu)")
room_list["roomP4"].long_description = "You are in puzzle 4 (long description)."
room_list["roomP4"].short_description = "You are in puzzle 4 (short description)."
room_list["roomP4"].documentation = "The answer is 'answer'."

# Creating room P5
room_list["roomP5"] = Room.Room("roomP5", "puzzle 5 (keyboard)")
room_list["roomP5"].long_description = "You are in puzzle 5 (long description)."
room_list["roomP5"].short_description = "You are in puzzle 5 (short description)."
room_list["roomP5"].documentation = "The answer is 'answer'."




# Creating roomMP
room_list["roomMP"] = Room.Room("roomMP", "Motherboard")
room_list["roomMP"].long_description = "The final challenge."
room_list["roomMP"].short_description = "The final challenge."

##############################
### LINKING THINGS & ROOMS ###
##############################

say("Linking things and rooms...")

# linking roomA (Balcony) stuff

thing_list["pedestal"].add_item(thing_list["book"])

room_list["roomA"].add_thing(thing_list["pedestal"])
room_list["roomA"].add_thing(thing_list["plaque"])
room_list["roomA"].add_thing(thing_list["balconyKeypad"])

room_list["roomA"].exits["north"] = thing_list["balconyWindowClosed"]
thing_list["balconyWindowOpen"].destination = room_list["roomB"]

# linking roomB (Lobby) stuff

room_list["roomB"].add_thing(thing_list["lobbyComputer"])

# adding "floppies" to lobby for now

room_list["roomB"].add_thing(thing_list["floppyDisk"])
room_list["roomB"].add_thing(thing_list["cd"])
room_list["roomB"].add_thing(thing_list["cartridge"])
room_list["roomB"].add_thing(thing_list["tape"])
room_list["roomB"].add_thing(thing_list["flashdrive"])


thing_list["lobbyStairs"].destination = room_list["roomC"]
thing_list["lobbyOrnateDoor"].destination = room_list["roomMP"]
thing_list["B-K"].destination = room_list["roomK"]

room_list["roomB"].exits["south"] = thing_list["lobbyWindow"]
room_list["roomB"].exits["east"] = thing_list["lobbyStairs"]
room_list["roomB"].exits["up"] = thing_list["lobbyStairs"]
room_list["roomB"].exits["north"] = thing_list["lobbyOrnateDoor"]
# TODO
room_list["roomB"].exits["west"] = thing_list["B-K"]
room_list["roomB"].exits["down"] = thing_list["B-K"]



# linking roomC (Utilities) stuff

thing_list["utilityStairs"].destination = room_list["roomB"]
thing_list["utilityHallway"].destination = room_list["roomD"]

room_list["roomC"].exits["north"] = thing_list["utilityHallway"]
room_list["roomC"].exits["west"] = thing_list["utilityStairs"]
room_list["roomC"].exits["down"] = thing_list["utilityStairs"]

# linking roomD (MousePad) stuff

room_list["roomD"].add_thing(thing_list["hungryMouse"])
room_list["roomD"].add_thing(thing_list["lever"])
room_list["roomD"].add_thing(thing_list["secretWall"])

thing_list["mousepadHallway"].destination = room_list["roomC"]
# TODO
thing_list["mousepadStairs"].destination = room_list["roomE"]
# thing_list["D-P1"].destination = room_list["roomP1"]

room_list["roomD"].exits["south"] = thing_list["mousepadHallway"]
room_list["roomD"].exits["west"] = thing_list["secretWall"]
# TODO
room_list["roomD"].exits["north"] = thing_list["mousepadStairs"]
room_list["roomD"].exits["up"] = thing_list["mousepadStairs"]
# room_list["roomD"].exits["west"] = thing_list["D-P1"]



# linking roomE (Ballroom) stuff
thing_list["ballroomStairs"].destination = room_list["roomD"]
thing_list["ballroomElevator"].destination = room_list["roomF"]
thing_list["ballroomDoor"].destination = room_list["roomP2"]

room_list["roomE"].exits["south"] = thing_list["ballroomStairs"]
room_list["roomE"].exits["down"] = thing_list["ballroomStairs"]
room_list["roomE"].exits["up"] = thing_list["ballroomElevator"]
room_list["roomE"].exits["west"] = thing_list["ballroomDoor"]

thing_list["bar"].add_item(thing_list["wine"])
thing_list["bar"].add_item(thing_list["water"])
thing_list["bar"].add_item(thing_list["soda"])

room_list["roomE"].add_thing(thing_list["bar"])
room_list["roomE"].add_thing(thing_list["tipJar"])

# linking roomF (I/O Room) stuff

# TODO
thing_list["IOroomElevator"].destination = room_list["roomE"]
thing_list["IOroomHallway"].destination = room_list["roomG"]
thing_list["IOroomDoor"].destination = room_list["roomP3"]

room_list["roomF"].exits["down"] = thing_list["IOroomElevator"]
room_list["roomF"].exits["west"] = thing_list["IOroomHallway"]
room_list["roomF"].exits["south"] = thing_list["IOroomDoor"]

# linking roomG (Bus Station) stuff
# TODO
thing_list["busHallway"].destination = room_list["roomF"]
thing_list["busRamp"].destination = room_list["roomH"]

room_list["roomG"].exits["east"] = thing_list["busHallway"]
room_list["roomG"].exits["south"] = thing_list["busRamp"]
room_list["roomG"].exits["up"] = thing_list["busRamp"]


# linking roomH (Webs) stuff

thing_list["websOpening"].destination = room_list["roomI"]
# TODO
thing_list["websRamp"].destination = room_list["roomG"]
thing_list["H-J"].destination = room_list["roomJ"]
thing_list["H-P4"].destination = room_list["roomP4"]

room_list["roomH"].exits["south"] = thing_list["websOpening"]
# TODO
room_list["roomH"].exits["north"] = thing_list["websRamp"]
room_list["roomH"].exits["down"] = thing_list["websRamp"]
room_list["roomH"].exits["west"] = thing_list["H-J"]
room_list["roomH"].exits["up"] = thing_list["H-J"]
room_list["roomH"].exits["east"] = thing_list["H-P4"]


# linking roomI (Dark Webs) stuff

room_list["roomI"].add_thing(thing_list["cobwebs"])
# room_list["roomI"].add_thing(thing_list["floppy"])

thing_list["darkWebsOpening"].destination = room_list["roomH"]

room_list["roomI"].exits["north"] = thing_list["darkWebsOpening"]


# linking roomJ (Clock Room) stuff

# TODO
thing_list["J-H"].destination = room_list["roomH"]
thing_list["J-K"].destination = room_list["roomK"]
thing_list["J-P5"].destination = room_list["roomP5"]

room_list["roomJ"].exits["east"] = thing_list["J-H"]
room_list["roomJ"].exits["down"] = thing_list["J-H"]
room_list["roomJ"].exits["south"] = thing_list["J-K"]
room_list["roomJ"].exits["north"] = thing_list["J-P5"]


# linking roomK (Cooling Room) stuff

thing_list["refrigerator"].add_item(thing_list["cheese"])

room_list["roomK"].add_thing(thing_list["refrigerator"])

thing_list["K-B"].destination = room_list["roomB"]
thing_list["K-J"].destination = room_list["roomJ"]

room_list["roomK"].exits["east"] = thing_list["K-B"]
room_list["roomK"].exits["up"] = thing_list["K-B"]
room_list["roomK"].exits["north"] = thing_list["K-J"]

# linking roomP1 (Puzzle 1) stuff

room_list["roomP1"].add_thing(thing_list["puzzle1Keyboard"])

# TODO
thing_list["P1-D"].destination = room_list["roomD"]
room_list["roomP1"].exits["east"] = thing_list["P1-D"]

# linking roomP2 (Puzzle 2) stuff
room_list["roomP2"].add_thing(thing_list["puzzle2Keyboard"])

# TODO
thing_list["P2Door"].destination = room_list["roomE"]
room_list["roomP2"].exits["east"] = thing_list["P2Door"]

# linking roomP3 (Puzzle 3) stuff
room_list["roomP3"].add_thing(thing_list["puzzle3Keyboard"])

thing_list["P3Door"].destination = room_list["roomF"]
room_list["roomP3"].exits["north"] = thing_list["P3Door"]

# linking roomP4 (Puzzle 4) stuff
room_list["roomP4"].add_thing(thing_list["puzzle4Keyboard"])

thing_list["P4-H"].destination = room_list["roomH"]
room_list["roomP4"].exits["west"] = thing_list["P4-H"]

# linking roomP5 (Puzzle 5) stuff
room_list["roomP5"].add_thing(thing_list["puzzle5Keyboard"])

thing_list["P5-J"].destination = room_list["roomJ"]
room_list["roomP5"].exits["south"] = thing_list["P5-J"]

# linking roomMP stuff

thing_list["motherboardOrnateDoor"].destination = room_list["roomB"]
room_list["roomMP"].exits["south"] = thing_list["motherboardOrnateDoor"]



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

        file_name = ROOM_PREFIX + room_obj["data"]["id"]
        f = open(file_name, "w")
        f.truncate(0)
        json.dump(room_obj, f)
        f.close()

        print(room_obj)


generate_data_files(thing_list, room_list)
generate_blank_save(thing_list, room_list)
