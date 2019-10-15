import inputclass

class Game:
	def __init__(game, phrase):
		game.phrase = phrase

	def playGame(game):
		while True:
			print("\ngame.phrase is: " + game.phrase)
			exit = inputclass.InputClass.getInput(game)
			if(exit == 1):
				break
