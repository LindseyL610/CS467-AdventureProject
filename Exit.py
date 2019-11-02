import os
import json

class Exit:
	def __init__(self, data, state):
		self.data = data.copy()
		self.state = state.copy()

	def get_state_data(self):
		return self.state