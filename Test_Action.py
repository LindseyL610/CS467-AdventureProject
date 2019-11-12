from Test_Game import GameData
from Utilities import say
from Verbs_and_Actions import verb_list, action_list

#Creating Game
my_game = GameData()

def run_test(test_args):
    # this line is similar to what can be run in the parser
    verb_list[test_args["verb"]].execute(my_game, test_args)

say("\n\n")
say("testing 'look'")
run_test(
    {"verb" : "look"})

say("\n\n")
say("testing 'look' (again)")
run_test(
    {"verb" : "look"})

say("\n\n")
say("testing 'look at'")
run_test(
    {"verb" : "look",
     "prep" : "at"})

say("\n\n")
say("testing 'look at book'")
run_test(
    {"verb" : "look",
     "dobj" : "book",
     "prep" : "at"})

say("\n\n")
say("testing take book")
run_test(
    {"verb" : "take",
     "dobj" : "book"})


say("\n\n")
say("testing take book again")
run_test(
    {"verb" : "take",
     "dobj" : "book"})

say("\n\n")
say("testing take cheese")
run_test(
    {"verb" : "take",
     "dobj" : "cheese"})

say("\n\n")
say("testing take")
run_test(
    {"verb" : "take"})

say("\n\n")
say("testing read book")
run_test(
    {"verb" : "read",
     "dobj" : "book"})

say("\n\n")
say("testing read book in door")
run_test(
    {"verb" : "read",
     "dobj" : "book",
     "prep" : "in",
     "iobj" : "door"})

say("\n\n")
say("testing 'read plaque'")
run_test(
    {"verb": "read",
     "dobj": "plaque"})

say("\n\n")
say("testing 'drop book'")
run_test(
    {"verb": "drop",
     "dobj": "book"})

say("\n\n")
say("testing 'put book on cheese'")
run_test(
    {"verb": "put",
     "dobj": "book",
     "prep": "on",
     "iobj": "cheese"})


say("\n\n")
say("testing 'pull lever'")
run_test(
    {"verb": "pull",
     "dobj": "lever"})