import action

class InputClass:
	@staticmethod	
	def getInput(game):
		print('Enter a new phrase ("quit" to quit).')
		phrase = raw_input(': ')
		
		if phrase == 'quit':
			return 1

		action.Action.actionFunc(game, phrase)
		return 0
