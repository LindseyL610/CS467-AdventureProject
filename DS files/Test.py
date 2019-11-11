from Game import Game
from Utilities import say
from Create import all_things, all_rooms


#Creating Game
my_game = Game()

#creating test args
test_args = {"verb" : "give",
             "dobj" : "cheese",
             "preposition" : "to",
             "iobj" : "mouse"}

# Testing plaque
say("\n")
say("TESTING plaque")
plaque = all_things["plaque"]
say("Testing plaque.look:")
plaque.look(my_game, test_args)



say("Testing plaque.read:")
plaque.read(my_game, test_args)

say("Testing plaque.take:")
plaque.take(my_game, test_args)

say("Testing plaque.drop:")
plaque.drop(my_game, test_args)

# Testing cheese
say("\n")
say("TESTING CHEESE")
cheese = all_things["cheese"]
say("Testing cheese.look:")
cheese.look(my_game, test_args)

say("Testing cheese.read:")
cheese.read(my_game, test_args)

say("Testing cheese.take:")
cheese.take(my_game, test_args)

say("Testing cheese.take again:")
cheese.take(my_game, test_args)

say("Testing cheese.drop:")
cheese.drop(my_game, test_args)

# Testing Book
say("\n")
say("TESTING BOOK")
book = all_things["book"]
say("Testing book.look:")
book.look(my_game, test_args)

say("Testing book.read:")
book.read(my_game, test_args)

say("Testing book.take:")
book.take(my_game, test_args)

say("Testing book.take again:")
book.take(my_game, test_args)

say("Testing book.drop:")
book.drop(my_game, test_args)

say("Testing book.go:")
book.go(my_game, test_args)


# Testing hallwayS
say("\n")
say("TESTING hallwayS")
hallwayS = all_things["hallwayS"]
say("Testing hallwayS.look:")
hallwayS.look(my_game, test_args)

say("Testing hallwayS.read:")
hallwayS.read(my_game, test_args)

say("Testing hallwayS.take:")
hallwayS.take(my_game, test_args)

say("Testing hallwayS.drop:")
hallwayS.drop(my_game, test_args)

say("Testing hallwayS.go:")
hallwayS.go(my_game, test_args)



# Testing going north from RoomC
say("\n")
roomC = all_rooms["roomC"]
roomD = all_rooms["roomD"]
say("TESTING roomC to roomD")

direction_args = {"verb" : "go",
                  "dobj" : "north",
                  "preposition" : None,
                  "iobj" : None}

roomC.go(my_game, direction_args)


