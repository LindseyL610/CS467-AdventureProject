import Room
import os

ROOM = "RM_"
SAVE = "SV_"

class Game:
	def __init__(self):
		self.rooms = self.load_rooms()

		self.current_room = self.rooms['balcony']

#		for room in self.rooms:
#			print("id= " + self.rooms[room].id)
#			print("long_description= " + self.rooms[room].long_description)
#			print("short_description= " + self.rooms[room].short_description)
#			print("exits= " + str(self.rooms[room].exits))
#			print("actions= " + str(self.rooms[room].actions))
#			print("status= " + str(self.rooms[room].status))

#		print(str(self.rooms))

#		print(str(self.current_room))

	def get_file_names(self, type):
		type_files = list()
	
		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

		for name in files:
			if name.find(type) is 0:
				type_files.append(name)

		return type_files

	def get_object_names(self, type):
		object_names = list()

		files = self.get_file_names(type)

		for name in files:
			object_names.append(name[3:])

		return object_names

	def load_rooms(self):
		rooms = dict()
				
		room_names = self.get_object_names(ROOM)

		for name in room_names:
			rooms[name] = Room.Room(name)

		return rooms


	def prompt(self):
		if not self.current_room.status['visited']:
			print(self.current_room.long_description)
		else:
			print(self.current_room.short_description)

		input_str = input("> ")

		return input_str