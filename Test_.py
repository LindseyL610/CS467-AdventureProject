import json
import Thing
import Room

room_list = dict()
thing_list = dict()

room_list["test room name"] = Room.Room("test room id", "test room name")
room_list["test room2 name"] = Room.Room("test room2 id", "test room2 name")

thing_list["test thing name"] = Thing.Item("test thing id", "test thing name")
thing_list["test thing 2 name"] = Thing.Item("test thing 2 id", "test thing 2 name")

thing_list["test thing name"].starting_location = room_list["test room2 name"]
thing_list["test thing name"].current_location = room_list["test room name"]

thing1_status = thing_list["test thing name"].get_status()

#print("thing1= " + thing1_status)

thing_list["test thing 2 name"].set_status(thing1_status, thing_list, room_list)

thing2_status = thing_list["test thing 2 name"].get_status()

#print("thing2= " + thing2_status)
print(room_list["test room name"])
print(room_list["test room2 name"])