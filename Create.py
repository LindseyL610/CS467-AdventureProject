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

# RUBBER DUCK--------------------------
# Creating rubber duck
thing_list["rubberDuck"] = Thing.RubberDuck("rubber duck", "rubber duck")
thing_list["rubberDuck"].description = "A rubber duck."
thing_list["rubberDuck"].alternate_names.extend(["duck"])
thing_list["rubberDuck"].adjectives.extend(["rubber"])

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


# ROOM C (Utility Room) FEATURES AND ITEMS------------------------------------------
# Creating desk
thing_list["utilityRoomDesk"] = Thing.Surface("utilityRoomDesk", "desk")
thing_list["utilityRoomDesk"].description = "A desk."

# Creating newspaper
thing_list["newspaper"] = Thing.Newspaper("newspaper", "newspaper")
thing_list["newspaper"].description = "A newspaper with an article about bugs."
thing_list["newspaper"].alternate_names.extend(["paper"])

# Creating toolbox
thing_list["toolbox"] = Thing.Feature("toolbox", "toolbox")
thing_list["toolbox"].description = "A toolbox."
thing_list["toolbox"].msg_cannot_take = "The toolbox is too heavy for you to pick up."
thing_list["toolbox"].msg_cannot_be_opened = "The toolbox is rusted shut."

# Creating locker
thing_list["utilityRoomLocker"] = Thing.Container("utilityRoomLocker", "locker")
thing_list["utilityRoomLocker"].description = "A locker."

# Creating cleaning supplies
thing_list["cleaning supplies"] = Thing.Feature("cleaning supplies", "cleaning supplies")
thing_list["cleaning supplies"].description = "Some bottles of cleaning supplies."
thing_list["cleaning supplies"].list_name = "some bottles of cleaning supplies"
thing_list["cleaning supplies"].alternate_names.extend(["supplies", "bottles"])
thing_list["cleaning supplies"].adjectives.extend(["cleaning"])
thing_list["cleaning supplies"].msg_cannot_take = "There are too many bottles for you to take."

# Creating debugger
thing_list["debugger"] = Thing.Debugger("debugger", "debugger")
thing_list["debugger"].description = "A can of debugger."
thing_list["debugger"].list_name = "a can of debugger"


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
thing_list["wine"] = Thing.Wine("wine", "wine")
thing_list["wine"].description = "A bottle of 'Ivory Keyboard' wine. Seems to be a good vintage."
thing_list["wine"].list_name = "a bottle of wine"

thing_list["water"] = Thing.Drink("water", "water")
thing_list["water"].description = "A bottle of water."
thing_list["water"].list_name = "a bottle of water"

thing_list["soda"] = Thing.Drink("soda", "soda")
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

thing_list["coin"] = Thing.Key("coin", "coin")
thing_list["coin"].list_name = "a gold coin"
thing_list["coin"].adjectives.extend(["gold"])
thing_list["coin"].description = "A gold coin."

thing_list["piano"] = Thing.Piano("piano", "piano")
thing_list["piano"].description = "A grand piano with a long keyboard of shiny white and black ivory keys. " \
                                  "The piano has the words 'Qwerty Classics Series' painted in gold cursive " \
                                  "beneath the cover."
thing_list["piano"].adjectives.extend(["grand"])

thing_list["ballroomCoinSlot"] = Thing.Lock("ballroomCoinSlot", "slot")
thing_list["ballroomCoinSlot"].description = "A coin slot next to the door."
thing_list["ballroomCoinSlot"].list_name = "a slot"
thing_list["ballroomCoinSlot"].receive_preps.append("in")
thing_list["ballroomCoinSlot"].key_consumed = True
thing_list["ballroomCoinSlot"].door_lock = True
thing_list["ballroomCoinSlot"].item_dispenser = False
thing_list["ballroomCoinSlot"].msg_toggled = "The coin disappears into the slot. You hear a click near the door--it is now unlocked."


thing_list["DancingDaemon"] = Thing.DancingDaemon("DancingDaemon", "DAEMON")
thing_list["DancingDaemon"].adjectives.extend(["dancing"])
thing_list["DancingDaemon"].description = "The DAEMON dances all across the dance floor and beckons you to join..."
thing_list["DancingDaemon"].list_name = "a dancing DAEMON"


#--------------------------------------------------------------------------
#ROOM F (I/O ROOM) FEATURES AND ITEMS--------------------------------------
thing_list["key"] = Thing.Key("key", "key")
thing_list["key"].list_name = "a key"
thing_list["key"].adjectives.extend(["metal"])
thing_list["key"].description = "A standard metal key for opening a lock."

thing_list["card"] = Thing.Key("card", "card")
thing_list["card"].list_name = "a punch card"
thing_list["card"].adjectives.extend(["punch"])
thing_list["card"].description = "An old computer punch card. At the top of the card is the word 'key'."

thing_list["IOroomDocuments"] = Thing.Item("IOroomDocuments", "documents")
thing_list["IOroomDocuments"].description = "A disorderly stack of documents. Coffee rings abound."
thing_list["IOroomDocuments"].list_name = "some useless documents"
thing_list["IOroomDocuments"].adjectives.extend(["disorderly"])

thing_list["IOroomCardScraps"] = Thing.Item("IOroomCardScraps", "scraps")
thing_list["IOroomCardScraps"].description = "A pile of paper scraps. Looks like old punch cards. These things have been used, and not gently. They are useless."
thing_list["IOroomCardScraps"].list_name = "some paper scraps"
thing_list["IOroomCardScraps"].adjectives.extend(["paper"])

thing_list["IOroomMetalChunks"] = Thing.Item("IOroomMetalChunks", "chunks")
thing_list["IOroomMetalChunks"].description = "A pile of useless metal chunks. Not even a fully formed paper clip can be found in the heap."
thing_list["IOroomMetalChunks"].list_name = "some metal chunks"
thing_list["IOroomMetalChunks"].adjectives.extend(["metal"])

thing_list["IOroomShreddings"] = Thing.Item("IOroomShreddings", "shreddings")
thing_list["IOroomShreddings"].description = "Shredded paper. You begin to piece the shreddings together to see what they say but decide not to, because you don't want to die alone in this tower, literally trying to read what is written on trash."
thing_list["IOroomShreddings"].list_name = "some paper shreddings"
thing_list["IOroomShreddings"].adjectives.extend(["paper"])

thing_list["IOroomFiles"] = Thing.Item("IOroomFiles", "files")
thing_list["IOroomFiles"].description = "Files. They appear to contain technical schematics."
thing_list["IOroomFiles"].list_name = "a bunch of files"

thing_list["IOroomDesk"] = Thing.Surface("IOroomDesk", "desk")
thing_list["IOroomDesk"].description = "A cluttered desk. There is a drawer."

thing_list["IOroomDeskDrawer"] = Thing.Container("IOroomDeskDrawer", "drawer")
thing_list["IOroomDeskDrawer"].description = "A desk drawer."
thing_list["IOroomDeskDrawer"].can_be_opened = True
thing_list["IOroomDeskDrawer"].is_open = False
thing_list["IOroomDeskDrawer"].contents_accessible = False
thing_list["IOroomDeskDrawer"].contents_accessible_iff_open = True
thing_list["IOroomDeskDrawer"].is_listed = False
thing_list["IOroomDeskDrawer"].list_name = "a desk drawer"

thing_list["IOroomBox"] = Thing.Container("IOroomBox", "box")
thing_list["IOroomBox"].description = "A cardboard box with 'junk' scrawled on it with marker."
thing_list["IOroomBox"].can_be_opened = True
thing_list["IOroomBox"].is_open = False
thing_list["IOroomBox"].contents_accessible = False
thing_list["IOroomBox"].contents_accessible_iff_open = True
thing_list["IOroomBox"].is_listed = True
thing_list["IOroomBox"].list_name = "a cardboard box"
thing_list["IOroomBox"].adjectives.extend(["cardboard"])

thing_list["IOroomInbox"] = Thing.Container("IOroomInbox", "inbox")
thing_list["IOroomInbox"].description = "An inbox. That is, a literal inbox. A bin labeled 'in' for putting papers into, to be pushed, for instance, to an outbox."
thing_list["IOroomInbox"].can_be_opened = False
thing_list["IOroomInbox"].is_open = True
thing_list["IOroomInbox"].contents_accessible = True
thing_list["IOroomInbox"].list_name = "an inbox"

thing_list["IOroomOutbox"] = Thing.Container("IOroomOutbox", "outbox")
thing_list["IOroomOutbox"].description = "An outbox. For stuff going out, such as useless metal chunks."
thing_list["IOroomOutbox"].can_be_opened = False
thing_list["IOroomOutbox"].is_open = True
thing_list["IOroomOutbox"].contents_accessible = True
thing_list["IOroomOutbox"].list_name = "an outbox"

thing_list["IOroomCabinet"] = Thing.Container("IOroomCabinet", "cabinet")
thing_list["IOroomCabinet"].description = "A metal filing cabinet."
thing_list["IOroomCabinet"].can_be_opened = True
thing_list["IOroomCabinet"].is_open = False
thing_list["IOroomCabinet"].contents_accessible = False
thing_list["IOroomCabinet"].contents_accessible_iff_open = True
thing_list["IOroomCabinet"].is_listed = False
thing_list["IOroomCabinet"].list_name = "a filing cabinet"
thing_list["IOroomCabinet"].adjectives.extend(["filing"])

thing_list["IOroomPunchCardReader"] = Thing.Lock("IOroomPunchCardReader", "reader")
thing_list["IOroomPunchCardReader"].description = "A punch card reader. There is a cavity below the reader. It looks like objects are dispensed into the cavity."
thing_list["IOroomPunchCardReader"].list_name = "a punch card reader"
thing_list["IOroomPunchCardReader"].receive_preps.append("in")
thing_list["IOroomPunchCardReader"].key_consumed = True
thing_list["IOroomPunchCardReader"].door_lock = False
thing_list["IOroomPunchCardReader"].item_dispenser = True
thing_list["IOroomPunchCardReader"].msg_toggled = "The reader accepts the punch card. You hear deafening mechanical noises coming from all around you. After awhile, the reader spits out a key. You add the key to your inventory."

thing_list["IOroomLock"] = Thing.Lock("IOroomLock", "lock")
thing_list["IOroomLock"].description = "A locking mechanism next to the door. There is a hole where a key should go."
thing_list["IOroomLock"].list_name = "a door lock"
thing_list["IOroomLock"].receive_preps.append("in")
thing_list["IOroomLock"].key_consumed = False
thing_list["IOroomLock"].door_lock = True
thing_list["IOroomLock"].item_dispenser = False
thing_list["IOroomLock"].msg_toggled = "The key turns in the lock, and the door unlocks."
#--------------------------------------------------------------------------
#ROOM G (BUS STATION) FEATURES AND ITEMS--------------------------------------
thing_list["busLocked"] = Thing.Feature("busLocked", "bus")
thing_list["busLocked"].description = "A bus. On the side of the bus it says 'Serial Bus Lines'. You can see through the windows that it is lit inside, but the Driver DAEMON stands at the door, blocking access to the bus."
thing_list["busLocked"].is_listed = True
thing_list["busLocked"].list_name = "a bus waiting at the platform"

thing_list["bus"] = Thing.Container("bus", "bus")
thing_list["bus"].description = "A bus. On the side of the bus it says 'Serial Bus Lines'. The driver DAEMON has stepped aside, allowing you access to the bus."
thing_list["bus"].can_be_opened = False
thing_list["bus"].is_open = True
thing_list["bus"].contents_accessible = True
thing_list["bus"].contents_accessible_iff_open = True
thing_list["bus"].is_listed = True
thing_list["bus"].list_name = "a bus waiting at the platform"

thing_list["driverDaemon"] = Thing.Feature("driverDaemon", "DAEMON")
thing_list["driverDaemon"].description = "A DAEMON, the bus driver, standing at the door of the bus."
thing_list["driverDaemon"].is_listed = True
thing_list["driverDaemon"].list_name = "a driver DAEMON"
thing_list["driverDaemon"].adjectives.extend(["driver"])

thing_list["ticket"] = Thing.Ticket("ticket", "ticket")
thing_list["ticket"].list_name = "a ticket"
thing_list["ticket"].description = "Maybe a bus ticket, but you can't see it, because it's stuck in the vending terminal."
thing_list["ticket"].alt_description = "A ticket for a bus. On the ticket it reads 'Serial Bus Lines, trip 600', origin GPU, destination CPU."
thing_list["ticket"].msg_blocked = "The ticket seems to be stuck far back in the dispensing slot, and you hear a mechanical whining sound. Maybe you can do something to dislodge it..."

thing_list["busTicketTerminal"] = Thing.VendingTerminal("busTicketTerminal", "terminal")
thing_list["busTicketTerminal"].description = "A vending terminal for bus tickets. The screen reads 'Dispensing ticket...'. Below the screen is a dispensing slot. You can hear a whining noise coming from inside the terminal. Inside the dispensing slot you can see that a bus ticket is right at the edge but seems to be blocked."
thing_list["busTicketTerminal"].alt_description = "A vending terminal for bus tickets."
thing_list["busTicketTerminal"].list_name = "a bus ticket vending terminal"
thing_list["busTicketTerminal"].msg_rammed = "The whining sound coming from the terminal is replaced with the satisfying sound of a gear locking into place, followed by silence. The ticket has been dispensed!"
thing_list["busTicketTerminal"].adjectives.extend(["vending"])

thing_list["busSchedule"] = Thing.Sign("busSchedule", "schedule")
thing_list["busSchedule"].description = "Bus to GPU: t=4; Bus to CPU: t=11."
thing_list["busSchedule"].list_name = "a bus schedule"

#--------------------------------------------------------------------------

# ROOM H (WEB) FEATURES AND ITEMS-------------------------------------------

# Creating moth
thing_list["moth"] = Thing.Moth("moth", "moth")
thing_list["moth"].description = "A moth."
thing_list["moth"].list_name = "a moth"


# ROOM I (Dark Webs) FEATURES AND ITEMS--------------------------------------
# Creating Floppy
# thing_list["floppy"] = Thing.Item("floppy", "floppy")
# thing_list["floppy"].description = "This is some type of ancient storage device. It is a thin rectangle of plastic, " \
#                                     "with some unkown language written across the top."

# Creating cobwebs
thing_list["cobwebs"] = Thing.Feature("cobwebs", "cobwebs")
thing_list["cobwebs"].description = "You can see that there are sticky cobwebs everywhere, "\
				    "but can't see much more detail without any light."
thing_list["cobwebs"].list_name = "some cobwebs"

# Creating spider
thing_list["spider"] = Thing.Spider("spider", "spider")
thing_list["spider"].description = "A spider."
thing_list["spider"].list_name = "a spider"


# ROOM J (Clock Room) FEATURES AND ITEMS---------------------------------------
thing_list["shiftyMan"] = Thing.ShiftyMan("shiftyMan", "shiftyMan")
thing_list["shiftyMan"].description = "A shifty man."
thing_list["shiftyMan"].list_name = "a shifty man"
thing_list["shiftyMan"].alternate_names.extend(["man"])
thing_list["shiftyMan"].adjectives.extend(["shifty"])

# ROOM K (Cooling Room) FEATURES AND ITEMS--------------------------------------

# Creating fridge
thing_list["refrigerator"] = Thing.Container("refrigerator", "refrigerator")
thing_list["refrigerator"].description = "A refrigerator."
thing_list["refrigerator"].alternate_names.extend(["fridge"])

# Creating cheese
thing_list["cheese"] = Thing.Cheese("cheese", "cheese")
thing_list["cheese"].description = "The block of cheese smells quite potent."
thing_list["cheese"].list_name = "some cheese"

thing_list["freezer"] = Thing.Freezer("freezer", "freezer")
thing_list["freezer"].description = "This strange device has is labeled as a \"freezer\". " \
                                    "Is is making a grumbling sound, and cold air is pouring from it. " \
                                    "It is connected to a small platform on which is a chunk of ice. " \
                                    "It seems to be keeping it frozen."

thing_list["frozenLaptop"] = Thing.Feature("frozenLaptop", "ice")
thing_list["frozenLaptop"].description = \
    "A strangely shaped chunk of ice sitting on a platform. " \
    "Looking closer at it, it appears as though something is inside. " \
    "You're not sure, but it resembles a laptop."

thing_list["brokenLaptop"] = Thing.Item("brokenLaptop", "laptop")
thing_list["brokenLaptop"].description = "A laptop, broken, though no longer frozen."

# ROOM P1 (Cooling Room) FEATURES AND ITEMS--------------------------------------

thing_list["puzzle1Sign"] = Thing.Sign("puzzle1Sign", "sign")
thing_list["puzzle1Sign"].description = \
    "The sign reads: \n" \
    "Crystal Installation Notes: \n" \
    "1. Eggplant, Hot Pink, and Ivory must form a diagonal line. \n" \
    "2. Make sure Azure, Canary, and Gunmetal do not share a row or column. \n" \
    "3. Forest needs to be higher than Desert, but lower than Burgundy. \n" \
    "4. Hot Pink should be somewhere below and to the left of Gunmetal. \n" \
    "5. Canary and Desert each belong in a corner. \n" \
    "6. It is important that Ivory is not adjacent to Forest."

thing_list["puzzle1Machine"] = Thing.Feature("puzzle1Machine", "machine")
thing_list["puzzle1Machine"].description = \
    "Written on the machine are the words: 'Crystal Display System' " \
    "In the center of the machine are nine square cells, arranged in a 3x3 grid. " \
    "In each cell of the grid is a hole, " \
    "where it looks like something used to be. But nothing is there now. "

# Creating puzzle 1 input
thing_list["puzzle1Panel"] = Thing.InputPuzzle1("puzzle1Panel", "panel")
thing_list["puzzle1Panel"].adjectives.extend(["control"])

# Creating puzzle 2 input

thing_list["puzzle2Desk"] = Thing.Surface("puzzle2Desk", "desk")
thing_list["puzzle2Desk"].description = "A small desk."

thing_list["puzzle2Letters"] = Thing.Feature("puzzle2Letters", "letters")
thing_list["puzzle2Letters"].description = \
    "A stack of printed out emails between family members. As you glance through them, " \
    "there are several sentences in different messages that stand out to you. " \
    "There's something not quite right about them, " \
    "like someone has been <darkgreen>injecting</> things into them that shouldn't be there. " \
    "Now it seems as if they're speaking <darkgreen>different languages</>, " \
    "and there's something <darkgreen>in their words</> that makes you think they're " \
    "going against their <darkgreen>programming</>. \n" \
    "Here are the strange sentences: \n" \
    "<darkblue>\"I'll need a chainsaw if the trees keep growing so </><darkgreen>fast</><darkblue>.\" \n " \
    "\"Better to have wanderlust than to let your dreams </><darkgreen>corrode</><darkblue>.\" \n" \
    "\"To give my mojo a valuable boost, I drink some strong </><darkgreen>coffee</><darkblue>.\" \n" \
    "\"I'm going to run by the jewelers, to buy a </><darkgreen>gemstone</><darkblue>.\" \n" \
    "\"Isn't therapy the one thing that will help your fear of </><darkgreen>snakes</><darkblue>?\""

thing_list["puzzle2Letters"].can_be_taken = False
thing_list["puzzle2Letters"].msg_cannot_take = "There are too many letters to take all of them."
thing_list["puzzle2Letters"].list_name = "a pile of letters."
thing_list["puzzle2Letters"].can_be_read = True


thing_list["puzzle2Computer"] = Thing.InputPuzzle2("puzzle2Computer", "computer")
thing_list["puzzle2Computer"].description = "A computer."


# Creating puzzle 3 input
thing_list["puzzle3Keyboard"] = Thing.InputPuzzle3("puzzle3Keyboard", "keyboard")
thing_list["puzzle3Keyboard"].description = "A keyboard."
thing_list["puzzle3Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle3Keyboard"].answer = "answer"
thing_list["puzzle3Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"


# Creating puzzle 4 input
thing_list["puzzle4Keyboard"] = Thing.InputPuzzle4("puzzle4Keyboard", "keyboard")
thing_list["puzzle4Keyboard"].description = "A keyboard."
thing_list["puzzle4Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle4Keyboard"].answer = "answer"
thing_list["puzzle4Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"


# Creating puzzle 5 input
thing_list["puzzle5Keyboard"] = Thing.InputPuzzle5("puzzle5Keyboard", "keyboard")
thing_list["puzzle5Keyboard"].description = "A keyboard."
thing_list["puzzle5Keyboard"].msg_prompt = "What do you enter on the keyboard?"
thing_list["puzzle5Keyboard"].answer = "answer"
thing_list["puzzle5Keyboard"].msg_correct_answer = "You enter the correct answer and learn a function!"
#--------------------------------------------------------------------------
#CLOCK STUFF---------------------------------------------------------------
thing_list["universalClock"] = Thing.Clock("universalClock", "clock")
thing_list["universalClock"].list_name = "a clock on the wall"




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
thing_list["utilityStairs"].has_dynamic_description = True
thing_list["utilityStairs"].dynamic_description_text = "There is a staircase leading down and to the west."

# Creating exits between C (Utilities) and D (Mousepad) [[HALLWAY]]
# Creating utilityHallway
thing_list["utilityHallway"] = Thing.Exit("utilityHallway", "hallway")
thing_list["utilityHallway"].description = "This dark hallway leads off to the north." \
                                     "A strange smell seems to be coming through it."
thing_list["utilityHallway"].msg_go = "You slowly creep down the hallway."
thing_list["utilityHallway"].has_dynamic_description = True
thing_list["utilityHallway"].dynamic_description_text = "There is a hallway leading to the north."

# Creating mousepadHallway
thing_list["mousepadHallway"] = Thing.Exit("mousepadHallway", "hallway")
thing_list[
    "mousepadHallway"].description = "This dark hallway leads off to the north." \
                                     "A strange smell seems to be coming through it."
thing_list["mousepadHallway"].msg_go = "You slowly creep down the hallway."



# Creating exits between B and K [[RAMP (OR ESCALATOR?)]]
thing_list["lobbyRamp"] = Thing.Exit("lobbyRamp", "ramp")
thing_list["lobbyRamp"].description = "This ramp descends to the west."
thing_list["lobbyRamp"].msg_go = "You walk down the ramp to the west."
thing_list["coolingRamp"] = Thing.Exit("coolingRamp", "ramp")
thing_list["coolingRamp"].description = "This ramp goes up to the east."
thing_list["coolingRamp"].msg_go = "You walk up the ramp to the east."



# Creating exits between D and E [[STAIRS]]
thing_list["mousepadStairs"] = Thing.Exit("mousepadStairs", "stairs")
thing_list["mousepadStairs"].description = "A staircase leading up and to the north."
thing_list["mousepadStairs"].msg_go = "You ascend the stairs to the north."

thing_list["ballroomStairs"] = Thing.Exit("ballroomStairs", "stairs")
thing_list["ballroomStairs"].description = "A staircase leading down and to the south."
thing_list["ballroomStairs"].msg_go = "You descend the stairs to the south."
thing_list["ballroomStairs"].has_dynamic_description = True
thing_list["ballroomStairs"].dynamic_description_text = "There are stairs to the south."


# Creating exits between D (Mousepad) and P1 (Monitors) [[BRICKS/ TUNNEL]]

thing_list["secretWall"] = Thing.Exit("secretWall", "wall")
thing_list["secretWall"].description = "A section of this brick wall looks discolored. " \
                                       "But there is nothing else that appears out of the ordinary."
thing_list["secretWall"].has_dynamic_description = True
thing_list["secretWall"].dynamic_description_text = "There are discolored bricks on the west wall."
thing_list["secretWall"].adjectives.extend(["discolored"])
thing_list["secretWall"].alternate_names.extend(["bricks"])

thing_list["secretWall"].can_go = False
thing_list["secretWall"].msg_cannot_go = "There does not appear to be any way to go this way."

thing_list["mousepadTunnel"] = Thing.Exit("mousepadTunnel","tunnel")
thing_list["mousepadTunnel"].alternate_names.extend(["passage"])
thing_list["mousepadTunnel"].description = "A revealed tunnel leads to the west."
thing_list["mousepadTunnel"].has_dynamic_description = True
thing_list["mousepadTunnel"].dynamic_description_text = "A tunnel leads to the west."
thing_list["mousepadTunnel"].msg_go = "You creep down the tunnel."

thing_list["monitorTunnel"] = Thing.Exit("monitorTunnel", "tunnel")
thing_list["monitorTunnel"].description = "This tunnel leads back to the east."
thing_list["monitorTunnel"].msg_go = "You walk through the tunnel."

# Creating exits between E and F [[Elevator]]
thing_list["ballroomElevator"] = Thing.Exit("ballroomElevator", "elevator")
thing_list["ballroomElevator"].description = "An elevator stands ready to take you... somewhere. The light inside flickers."
thing_list["ballroomElevator"].msg_go = "You walk into the elevator, and the door closes behind you. You feel heavier. The elevator must be going up."
thing_list["ballroomElevator"].has_dynamic_description = True
thing_list["ballroomElevator"].dynamic_description_text = "There is an elevator that goes up."
thing_list["IOroomElevator"] = Thing.Exit("IOroomElevator", "elevator")
thing_list["IOroomElevator"].description = "An elevator stands ready to take you... somewhere. The light inside flickers."
thing_list["IOroomElevator"].msg_go = "You walk into the elevator, and the door closes behind you. You feel lighter. The elevator must be going down."
thing_list["IOroomElevator"].has_dynamic_description = True
thing_list["IOroomElevator"].dynamic_description_text = "There is an elevator that goes down."

# Creating exits between E and P2 [[Door]]
thing_list["ballroomDoorLocked"] = Thing.Exit("ballroomDoorLocked", "door")
thing_list["ballroomDoorLocked"].description = "An ordinary door, but it's locked."
thing_list["ballroomDoorLocked"].can_go = False
thing_list["ballroomDoorLocked"].msg_cannot_go = "The door is locked!"
thing_list["ballroomDoorLocked"].has_dynamic_description = True
thing_list["ballroomDoorLocked"].dynamic_description_text = "There is a door to the west."
thing_list["ballroomDoor"] = Thing.Exit("ballroomDoor", "door")
thing_list["ballroomDoor"].description = "An ordinary door."
thing_list["ballroomDoor"].msg_go = "You proceed through the door to the west."
thing_list["ballroomDoor"].has_dynamic_description = True
thing_list["ballroomDoor"].dynamic_description_text = "There is a door to the west."
thing_list["P2Door"] = Thing.Exit("P2Door", "door")
thing_list["P2Door"].description = "An ordinary door."
thing_list["P2Door"].msg_go = "You proceed through the door to the east."


# Creating exits between F and G [[Hallway]]
thing_list["IOroomHallway"] = Thing.Exit("IOroomHallway", "hallway")
thing_list["IOroomHallway"].description = "A long, well-lit hallway leading off to the west."
thing_list["IOroomHallway"].msg_go = "You walk through the hallway to the west."
thing_list["IOroomHallway"].has_dynamic_description = True
thing_list["IOroomHallway"].dynamic_description_text = "There is a hallway to the west."
thing_list["busHallway"] = Thing.Exit("busHallway", "hallway")
thing_list["busHallway"].description = "A long, well-lit hallway leading off to the east."
thing_list["busHallway"].msg_go = "You walk through the hallway to the east."
thing_list["busHallway"].has_dynamic_description = True
thing_list["busHallway"].dynamic_description_text = "There is a hallway to the east."


# Creating exits between F and P3 [[Door]]
thing_list["IOroomDoorLocked"] = Thing.Exit("IOroomDoorLocked", "door")
thing_list["IOroomDoorLocked"].can_go = False
thing_list["IOroomDoorLocked"].msg_cannot_go = "The door is locked!"
thing_list["IOroomDoorLocked"].has_dynamic_description = True
thing_list["IOroomDoorLocked"].dynamic_description_text = "There is a door to the south."
thing_list["IOroomDoor"] = Thing.Exit("IOroomDoor", "door")
thing_list["IOroomDoor"].description = "An ordinary door."
thing_list["IOroomDoor"].msg_go = "You proceed through the door to the south."
thing_list["IOroomDoor"].has_dynamic_description = True
thing_list["IOroomDoor"].dynamic_description_text = "There is a door to the south."
thing_list["P3Door"] = Thing.Exit("P3Door", "door")
thing_list["P3Door"].description = "An ordinary door."
thing_list["P3Door"].msg_go = "You proceed through the door to the north."

# Creating exits between G and H [[RAMP]]
thing_list["busRamp"] = Thing.Exit("busRamp", "ramp")
thing_list["busRamp"].description = "A ramp leading up and to the south."
thing_list["busRamp"].msg_go = "You walk up the ramp to the south."
thing_list["busRamp"].has_dynamic_description = True
thing_list["busRamp"].dynamic_description_text = "There is a ramp going up to the south."
thing_list["websRamp"] = Thing.Exit("websRamp", "ramp")
thing_list["websRamp"].description = "A ramp leading down and to the north."
thing_list["websRamp"].msg_go = "You walk up the ramp to the north."
thing_list["websRamp"].has_dynamic_description = True
thing_list["websRamp"].dynamic_description_text = "There is a ramp going down to the north."


# Creating exits between H (Webs) and I (Dark Webs)  [[OPENING]]

# Creating websOpening
thing_list["websOpening"] = Thing.Exit("websOpening", "opening")
thing_list["websOpening"].description = "The opening leads to a dark room."
thing_list["websOpening"].msg_go = "You cautiously go through the opening."
thing_list["websOpening"].has_dynamic_description = True
thing_list["websOpening"].dynamic_description_text = "There is an opening to the south."

# Creating darkWebsOpening
thing_list["darkWebsOpening"] = Thing.Exit("darkWebsOpening", "opening")
thing_list["darkWebsOpening"].description = "Light pours through the opening to the north."
thing_list["darkWebsOpening"].msg_go = "You quickly walk back through the opening."
thing_list["darkWebsOpening"].has_dynamic_description = True
thing_list["darkWebsOpening"].dynamic_description_text = "There is an opening to the north."

# thing_list["H-I"] = Thing.Exit("H-I", "exit H to I")
# thing_list["H-I"].description = "The exit from room H to room I."
# thing_list["H-I"].msg_go = "You walk through the exit from room H to room I."
# thing_list["I-H"] = Thing.Exit("I-H", "exit I to H")
# thing_list["I-H"].description = "The exit from room I to room H."
# thing_list["I-H"].msg_go = "You walk through the exit from room I to room H."

# Creating exits between H and J  [[STAIRS]]
thing_list["websStairs"] = Thing.Exit("websStairs", "stairs")
thing_list["websStairs"].description = "A staircase leading up and to the west."
thing_list["websStairs"].msg_go = "You walk up the stairs to the west."
thing_list["websStairs"].has_dynamic_description = True
thing_list["websStairs"].dynamic_description_text = "There is a staircase to the west."
thing_list["clockRoomStairs"] = Thing.Exit("clockRoomStairs", "stairs")
thing_list["clockRoomStairs"].description = "A staircase leading down and to the east ."
thing_list["clockRoomStairs"].msg_go = "You walk down the stairs to the east."
thing_list["clockRoomStairs"].has_dynamic_description = True
thing_list["clockRoomStairs"].dynamic_description_text = "There is a staircase to the east."

# Creating exits between H and P4 [[DOOR]]
thing_list["webDoor"] = Thing.BlockedDoor("webDoor", "door")
thing_list["webDoor"].description = "There is a door leading to the east."
thing_list["webDoor"].msg_go = "You walk east through the door."
thing_list["webDoor"].msg_cannot_go = "The moth blocks you from approaching the door."
thing_list["p4Door"] = Thing.BlockedDoor("p4Door", "door")
thing_list["p4Door"].description = "There is a door leading to the west."
thing_list["p4Door"].msg_go = "You walk west through the door."
thing_list["p4Door"].can_go = True

# Creating exits between J and K  [[HALLWAY]]
thing_list["clockRoomHallway"] = Thing.Exit("clockRoomHallway", "hallway")
thing_list["clockRoomHallway"].description = "This hallway leads south."\
					     "You can feel cold air coming from that direction."
thing_list["clockRoomHallway"].msg_go = "You follow the hallway south."
thing_list["coolingHallway"] = Thing.Exit("coolingHallway", "hallway")
thing_list["coolingHallway"].description = "This hallway leads north." \
                                           "You can feel warmer air coming from that direction."
thing_list["coolingHallway"].msg_go = "You follow the hallway north."

# Creating exits between J and P5 [[DOOR]]
thing_list["clockRoomDoor"] = Thing.BlockedDoor("clockRoomDoor", "door")
thing_list["clockRoomDoor"].description = "There is a door leading to the north."
thing_list["clockRoomDoor"].msg_go = "You walk north through the door."
thing_list["clockRoomDoor"].locked = True
thing_list["clockRoomDoor"].msg_unlock = "The shifty man opens the door for you."
thing_list["clockRoomDoor"].msg_cannot_go = "You tug on the door, but it is locked."
thing_list["clockRoomDoor"].alt_msg_cannot_go = "The shifty man blocks you from approaching the door."
thing_list["p5Door"] = Thing.BlockedDoor("p5Door", "door")
thing_list["p5Door"].description = "There is a door leading to the south."
thing_list["p5Door"].msg_go = "You walk south through the door."
thing_list["p5Door"].can_go = True


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


# Creating roomC
room_list["roomC"] = Room.Room("roomC", "Utility Room")
room_list["roomC"].long_description = "You step into a small room from its western side. "\
				      "It's just your luck that you immediately trip over a toolbox that you hadn't noticed lying on the floor. "\
				      "Irritated, you shove the toolbox to the right, where it stops with a thud next to a desk. "\
				      "You glance at the desk and notice a newspaper lying on top of it. "\
				      "Straight ahead of you, a large locker stands against the wall. "\
				      "To your left, on the north side of the room, you see a dark hallway. "
room_list["roomC"].short_description = "You are in the utility room. "


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

# Creating room E
room_list["roomE"] = Room.Ballroom("roomE", "Ballroom")
room_list["roomE"].long_description = "You enter an enormous ballroom, which is wide open, with a stocked bar on one side of the room, " \
										"a grand piano on the other side of the room, and a huge dancefloor made of ornate wood. " \
										"An elevator with shiny doors and a gold finish is on one end of the room. On the western wall is a door. " \
										"On the southern wall is a staircase leading down."
room_list["roomE"].short_description = "You are in the ballroom."
room_list["roomE"].documentation = "The art of programming starts at the keyboard. " \
									"Typing involves inputting text by pressing keys on a keyboard, which " \
									"might be a computer keyboard, a graphical user interface, or anything with keys to be pressed. " \
									"Typing is measured in words per minute (wpm). On average, programmers can type 50-70 wpm. " \
									"However, a real PRO can type 90+ wpm!"

# Creating room F
room_list["roomF"] = Room.Room("roomF", "I/O Room")
room_list["roomF"].long_description = "You are in a cluttered office. There is a desk, with high stacks of papers along with an inbox and an outbox. " \
										"A file cabinet sits next to the desk. A cardboard box sits on the floor next to the cabinet. " \
										"Near the desk is a reader for reading punch cards."
room_list["roomF"].short_description = "You are in the cluttered office."
room_list["roomF"].documentation = "The relevant page is ripped out except for a small triangular portion on the bottom containing the phrase 'Garbage in, garbage out!'"

# Creating room G
room_list["roomG"] = Room.BusStation("roomG", "Bus Station")
room_list["roomG"].long_description = "You are in... a bus station? Isn't this a tower? Nonetheless, there is a bus platform with sixteen parallel bus lanes that start on one end of the station and run together to the other end. At both ends, the lanes disappear into darkness. There is a ticket vending terminal on the platform and a bus schedule hanging on a post near the terminal. A ramp leading up is to the south, and there is a door leading east."
room_list["roomG"].short_description = "You are in the bus station."


# Creating room H
room_list["roomH"] = Room.Room("roomH", "Web")
room_list["roomH"].long_description = "You step into the west side of an extravagent marble hall, warmly lit by the glow from a fireplace in the north-east corner of the hall. "\
				      "A comfortable-looking velvet couch sits in front of the fireplace, but what really draws your attention is "\
				      "the giant moth hovering directly across from you, on the east side of the room. You take a good look at the moth "\
				      "and notice that it is holding some sort of a cartride in its mouth. Behind the moth lies a door, which the moth "\
				      "appears to be guarding. On the north side of the hall, you see a ramp going downward. On the south side "\
				      "of the hall, you see a pitch black opening." 
room_list["roomH"].short_description = "You are in the marble hall."



# Creating roomI
room_list["roomI"] = Room.DarkWeb("roomI", "Dark Web")
room_list["roomI"].long_description = "You enter a room so dark you can't see much of anything. As you you try to make out more of the room, using the small amount of light "\
				      "shining in from the hall to the north, you notice spider webs stretching across the room. You'll need to find a source of light before "\
				      "you can determine anything else about this room..."
room_list["roomI"].short_description = "You are in the dark room. The only thing you can see is some spider webs stretching across the room."



# Creating room J
room_list["roomJ"] = Room.ClockRoom("roomJ", "Clock Room")
room_list["roomJ"].long_description = "You enter a room containing a large, hand-carved clock on its west side. "\
				      "On the east side of the room, a staircase leads downward. "\
				      "Across from you, on the north side of the room, there is a door. "
room_list["roomJ"].short_description = "You are in the clock room."
room_list["roomJ"].special_time.append(2)

# Creating roomK
room_list["roomK"] = Room.Room("roomK", "Cooling Room")

room_list[
    "roomK"].long_description = \
    "This room is cold. Like extremely cold. You see tubes coming in and out of the walls " \
    "and ceiling that seem to be transporting some blue liquid. " \
    "On the south side of the room is what looks like a refrigerator. " \
    "Against the west wall is a contraption labeled \"freezer\", next to which is a chunk of ice. " \
    "There is a ramp ascending to the east, and a hallway leading north."
room_list["roomK"].short_description = \
    "You are in a very cold room. " \
    "There is a ramp ascending to the east, and a hallway leading north."





# Creating roomP1
room_list["roomP1"] = Room.Room("roomP1", "Monitor Station")
room_list["roomP1"].long_description = \
    "The walls are covered with several screens, of various sizes. Most of them seem to be horribly malfunctioning," \
    "like someone cast a *HEX* on them! They are all displaying nonsense, with the exception of a large control panel" \
    "on the north wall. All of the monitors have cords running into a large machine." \
    "There is a sign hanging next to the machine. " \
    "There is a tunnel to the east."
room_list["roomP1"].short_description = "So many monitors. " \
                                       "There is a tunnel to the east."
room_list["roomP1"].documentation = "This room uses a Crystal Display System to power the monitors used " \
                                    "for surveillance of the tower"

# Creating room P2
room_list["roomP2"] = Room.Room("roomP2", "Mailroom")
room_list["roomP2"].long_description = "In this small room, there is a desk, with a computer, and pile of letters. " \
                                       "There is a door to the east."
room_list["roomP2"].short_description = "A small, dusty room." \
                                        "There is a door to the east."
room_list["roomP2"].documentation = "The answer is 'answer'."

# Creating room P3
room_list["roomP3"] = Room.Room("roomP3", "puzzle 3 (search/ memory)")
room_list["roomP3"].long_description = "You are in puzzle 3 (long description). " \
                                       "There is a door to the north."
room_list["roomP3"].short_description = "You are in puzzle 3 (short description). " \
                                        "There is a door to the north."
room_list["roomP3"].documentation = "The answer is 'answer'."

# Creating room P4
room_list["roomP4"] = Room.Room("roomP4", "puzzle 4 (cpu)")
room_list["roomP4"].long_description = "You are in puzzle 4 (long description). " \
                                       "There is a door to the west."
room_list["roomP4"].short_description = "You are in puzzle 4 (short description). " \
                                        "There is a door to the west."
room_list["roomP4"].documentation = "The answer is 'answer'."

# Creating room P5
room_list["roomP5"] = Room.Room("roomP5", "puzzle 5 (keyboard)")
room_list["roomP5"].long_description = "You are in puzzle 5 (long description). " \
                                       "There is a door to the south."
room_list["roomP5"].short_description = "You are in puzzle 5 (short description). " \
                                        "There is a door to the south."
room_list["roomP5"].documentation = "The answer is 'answer'."




# Creating roomMP
room_list["roomMP"] = Room.Room("roomMP", "Motherboard")
room_list["roomMP"].long_description = "The final challenge."
room_list["roomMP"].short_description = "The final challenge."

##############################
### LINKING THINGS & ROOMS ###
##############################

say("Linking things and rooms...")

# Clock stuff -- applies to all Rooms!
room_list["roomB"].add_thing(thing_list["universalClock"])
room_list["roomC"].add_thing(thing_list["universalClock"])
room_list["roomD"].add_thing(thing_list["universalClock"])
room_list["roomE"].add_thing(thing_list["universalClock"])
room_list["roomF"].add_thing(thing_list["universalClock"])
room_list["roomG"].add_thing(thing_list["universalClock"])
room_list["roomH"].add_thing(thing_list["universalClock"])
room_list["roomI"].add_thing(thing_list["universalClock"])
room_list["roomJ"].add_thing(thing_list["universalClock"])
room_list["roomK"].add_thing(thing_list["universalClock"])
room_list["roomP1"].add_thing(thing_list["universalClock"])
room_list["roomP2"].add_thing(thing_list["universalClock"])
room_list["roomP3"].add_thing(thing_list["universalClock"])
room_list["roomP4"].add_thing(thing_list["universalClock"])
room_list["roomP5"].add_thing(thing_list["universalClock"])





# linking roomA (Balcony) stuff

thing_list["pedestal"].add_item(thing_list["book"])

room_list["roomA"].add_thing(thing_list["pedestal"])
room_list["roomA"].add_thing(thing_list["plaque"])
room_list["roomA"].add_thing(thing_list["balconyKeypad"])

room_list["roomA"].exits["north"] = thing_list["balconyWindowClosed"]
thing_list["balconyWindowOpen"].destination = room_list["roomB"]

# linking roomB (Lobby) stuff

# adding "rubberDuck" to lobby for now
room_list["roomB"].add_thing(thing_list["rubberDuck"])

room_list["roomB"].add_thing(thing_list["lobbyComputer"])

# adding "floppies" to lobby for now

#room_list["roomB"].add_thing(thing_list["floppyDisk"])
#room_list["roomB"].add_thing(thing_list["cd"])
#room_list["roomB"].add_thing(thing_list["cartridge"])
#room_list["roomB"].add_thing(thing_list["tape"])
room_list["roomB"].add_thing(thing_list["flashdrive"])


thing_list["lobbyStairs"].destination = room_list["roomC"]
thing_list["lobbyOrnateDoor"].destination = room_list["roomMP"]
thing_list["lobbyRamp"].destination = room_list["roomK"]

room_list["roomB"].exits["south"] = thing_list["lobbyWindow"]
room_list["roomB"].exits["east"] = thing_list["lobbyStairs"]
room_list["roomB"].exits["up"] = thing_list["lobbyStairs"]
room_list["roomB"].exits["north"] = thing_list["lobbyOrnateDoor"]
# TODO
room_list["roomB"].exits["west"] = thing_list["lobbyRamp"]
room_list["roomB"].exits["down"] = thing_list["lobbyRamp"]


# linking roomC (Utilities) stuff

room_list["roomC"].add_thing(thing_list["utilityRoomDesk"])
thing_list["utilityRoomDesk"].add_item(thing_list["newspaper"])
room_list["roomC"].add_thing(thing_list["toolbox"])
room_list["roomC"].add_thing(thing_list["utilityRoomLocker"])
thing_list["utilityRoomLocker"].add_item(thing_list["cleaning supplies"])
thing_list["utilityRoomLocker"].add_item(thing_list["debugger"])

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
thing_list["mousepadTunnel"].destination = room_list["roomP1"]

room_list["roomD"].exits["south"] = thing_list["mousepadHallway"]
room_list["roomD"].exits["west"] = thing_list["secretWall"]
# TODO
room_list["roomD"].exits["north"] = thing_list["mousepadStairs"]
room_list["roomD"].exits["up"] = thing_list["mousepadStairs"]
room_list["roomD"].exits["west"] = thing_list["secretWall"]



# linking roomE (Ballroom) stuff
thing_list["ballroomStairs"].destination = room_list["roomD"]
thing_list["ballroomElevator"].destination = room_list["roomF"]
thing_list["ballroomDoor"].destination = room_list["roomP2"]

room_list["roomE"].exits["south"] = thing_list["ballroomStairs"]
room_list["roomE"].exits["down"] = thing_list["ballroomStairs"]
room_list["roomE"].exits["up"] = thing_list["ballroomElevator"]
room_list["roomE"].exits["west"] = thing_list["ballroomDoorLocked"]

thing_list["ballroomCoinSlot"].controlled_exit = thing_list["ballroomDoorLocked"]
thing_list["ballroomCoinSlot"].open_exit = thing_list["ballroomDoor"]
thing_list["ballroomCoinSlot"].key = thing_list["coin"]

thing_list["coin"].lock = thing_list["ballroomCoinSlot"]

thing_list["bar"].add_item(thing_list["wine"])
thing_list["bar"].add_item(thing_list["water"])
thing_list["bar"].add_item(thing_list["soda"])

room_list["roomE"].add_thing(thing_list["bar"])
room_list["roomE"].add_thing(thing_list["tipJar"])
room_list["roomE"].add_thing(thing_list["piano"])
room_list["roomE"].add_thing(thing_list["ballroomCoinSlot"])

thing_list["DancingDaemon"].floppy = thing_list["cd"]

# linking roomF (I/O Room) stuff
# TODO
thing_list["IOroomElevator"].destination = room_list["roomE"]
thing_list["IOroomHallway"].destination = room_list["roomG"]
thing_list["IOroomDoor"].destination = room_list["roomP3"]

room_list["roomF"].exits["down"] = thing_list["IOroomElevator"]
room_list["roomF"].exits["west"] = thing_list["IOroomHallway"]
room_list["roomF"].exits["south"] = thing_list["IOroomDoorLocked"]

thing_list["IOroomPunchCardReader"].item = thing_list["key"]
thing_list["IOroomPunchCardReader"].key = thing_list["card"]

thing_list["IOroomLock"].controlled_exit = thing_list["IOroomDoorLocked"]
thing_list["IOroomLock"].open_exit = thing_list["IOroomDoor"]
thing_list["IOroomLock"].key = thing_list["key"]

thing_list["card"].lock = thing_list["IOroomPunchCardReader"]
thing_list["key"].lock = thing_list["IOroomLock"]

thing_list["IOroomDeskDrawer"].add_item(thing_list["card"])
thing_list["IOroomDesk"].add_item(thing_list["IOroomDocuments"])
thing_list["IOroomBox"].add_item(thing_list["IOroomShreddings"])
thing_list["IOroomInbox"].add_item(thing_list["IOroomCardScraps"])
thing_list["IOroomOutbox"].add_item(thing_list["IOroomMetalChunks"])
thing_list["IOroomCabinet"].add_item(thing_list["IOroomFiles"])

room_list["roomF"].add_thing(thing_list["IOroomPunchCardReader"])
room_list["roomF"].add_thing(thing_list["IOroomLock"])
room_list["roomF"].add_thing(thing_list["IOroomDesk"])
room_list["roomF"].add_thing(thing_list["IOroomDeskDrawer"])
room_list["roomF"].add_thing(thing_list["IOroomBox"])
room_list["roomF"].add_thing(thing_list["IOroomInbox"])
room_list["roomF"].add_thing(thing_list["IOroomOutbox"])
room_list["roomF"].add_thing(thing_list["IOroomCabinet"])

# linking roomG (Bus Station) stuff
# TODO
thing_list["busHallway"].destination = room_list["roomF"]
thing_list["busRamp"].destination = room_list["roomH"]

room_list["roomG"].exits["east"] = thing_list["busHallway"]
room_list["roomG"].exits["south"] = thing_list["busRamp"]
room_list["roomG"].exits["up"] = thing_list["busRamp"]

thing_list["bus"].add_item(thing_list["floppyDisk"])
thing_list["busTicketTerminal"].add_item(thing_list["ticket"])
thing_list["busTicketTerminal"].ticket = thing_list["ticket"]

room_list["roomG"].bus = thing_list["busLocked"]
room_list["roomG"].daemon = thing_list["driverDaemon"]
room_list["roomG"].special_time.append(4)
room_list["roomG"].special_time.append(7)

room_list["roomG"].add_thing(thing_list["busTicketTerminal"])
room_list["roomG"].add_thing(thing_list["busSchedule"])

# linking roomH (Webs) stuff

room_list["roomH"].add_thing(thing_list["moth"])

thing_list["moth"].floppy = thing_list["cartridge"]

thing_list["websOpening"].destination = room_list["roomI"]
thing_list["websRamp"].destination = room_list["roomG"]
thing_list["websStairs"].destination = room_list["roomJ"]
thing_list["webDoor"].destination = room_list["roomP4"]

room_list["roomH"].exits["south"] = thing_list["websOpening"]
room_list["roomH"].exits["north"] = thing_list["websRamp"]
room_list["roomH"].exits["down"] = thing_list["websRamp"]
room_list["roomH"].exits["west"] = thing_list["websStairs"]
room_list["roomH"].exits["up"] = thing_list["websStairs"]
room_list["roomH"].exits["east"] = thing_list["webDoor"]


# linking roomI (Dark Webs) stuff

room_list["roomI"].add_thing(thing_list["cobwebs"])
room_list["roomI"].add_thing(thing_list["spider"])
room_list["roomI"].add_thing(thing_list["tape"])
# room_list["roomI"].add_thing(thing_list["floppy"])

thing_list["darkWebsOpening"].destination = room_list["roomH"]

room_list["roomI"].exits["north"] = thing_list["darkWebsOpening"]


# linking roomJ (Clock Room) stuff
room_list["roomJ"].shifty_man = thing_list["shiftyMan"]
thing_list["clockRoomStairs"].destination = room_list["roomH"]
thing_list["clockRoomHallway"].destination = room_list["roomK"]
thing_list["clockRoomDoor"].destination = room_list["roomP5"]

room_list["roomJ"].exits["east"] = thing_list["clockRoomStairs"]
room_list["roomJ"].exits["down"] = thing_list["clockRoomStairs"]
room_list["roomJ"].exits["south"] = thing_list["clockRoomHallway"]
room_list["roomJ"].exits["north"] = thing_list["clockRoomDoor"]


# linking roomK (Cooling Room) stuff

thing_list["refrigerator"].add_item(thing_list["cheese"])

room_list["roomK"].add_thing(thing_list["refrigerator"])
room_list["roomK"].add_thing(thing_list["freezer"])
room_list["roomK"].add_thing(thing_list["frozenLaptop"])

thing_list["coolingRamp"].destination = room_list["roomB"]
thing_list["coolingHallway"].destination = room_list["roomJ"]

room_list["roomK"].exits["east"] = thing_list["coolingRamp"]
room_list["roomK"].exits["up"] = thing_list["coolingRamp"]
room_list["roomK"].exits["north"] = thing_list["coolingHallway"]

# linking roomP1 (Puzzle 1) stuff

room_list["roomP1"].add_thing(thing_list["puzzle1Panel"])
room_list["roomP1"].add_thing(thing_list["puzzle1Machine"])
room_list["roomP1"].add_thing(thing_list["puzzle1Sign"])

# TODO
thing_list["monitorTunnel"].destination = room_list["roomD"]
room_list["roomP1"].exits["east"] = thing_list["monitorTunnel"]

# linking roomP2 (Puzzle 2) stuff
room_list["roomP2"].add_thing(thing_list["puzzle2Computer"])
room_list["roomP2"].add_thing(thing_list["puzzle2Desk"])
thing_list["puzzle2Desk"].add_item(thing_list["puzzle2Computer"])
thing_list["puzzle2Desk"].add_item(thing_list["puzzle2Letters"])

# TODO
thing_list["P2Door"].destination = room_list["roomE"]
room_list["roomP2"].exits["east"] = thing_list["P2Door"]

# linking roomP3 (Puzzle 3) stuff
room_list["roomP3"].add_thing(thing_list["puzzle3Keyboard"])

thing_list["P3Door"].destination = room_list["roomF"]
room_list["roomP3"].exits["north"] = thing_list["P3Door"]

# linking roomP4 (Puzzle 4) stuff
room_list["roomP4"].add_thing(thing_list["puzzle4Keyboard"])

thing_list["p4Door"].destination = room_list["roomH"]
room_list["roomP4"].exits["west"] = thing_list["p4Door"]

# linking roomP5 (Puzzle 5) stuff
room_list["roomP5"].add_thing(thing_list["puzzle5Keyboard"])

thing_list["p5Door"].destination = room_list["roomJ"]
room_list["roomP5"].exits["south"] = thing_list["p5Door"]

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
