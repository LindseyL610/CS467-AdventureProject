from Game import say, Game
from Create import all_things, all_rooms

#Creating Game
my_game = Game()

#creating test args
test_args = {"verb" : "give",
             "dobj" : "cheese",
             "preposition" : "to",
             "iobj" : "mouse"}

# Testing sign
say("\n")
say("TESTING SIGN")
sign = all_things["sign"]
say("Testing sign.look:")
sign.look(my_game, test_args)

say("Testing sign.read:")
sign.read(my_game, test_args)

say("Testing sign.take:")
sign.take(my_game, test_args)

say("Testing sign.drop:")
sign.drop(my_game, test_args)

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


# Testing hallway
say("\n")
say("TESTING HALLWAY")
hallway = all_things["hallway"]
say("Testing hallway.look:")
hallway.look(my_game, test_args)

say("Testing hallway.read:")
hallway.read(my_game, test_args)

say("Testing hallway.take:")
hallway.take(my_game, test_args)

say("Testing hallway.drop:")
hallway.drop(my_game, test_args)

say("Testing hallway.go:")
hallway.go(my_game, test_args)



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

