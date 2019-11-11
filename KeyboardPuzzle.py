import os
import json

class KeyboardPuzzle: # SUBCLASS OF FEATURE
	def __init__(self, data, state):
		# KEYBOARD PUZZLE INHERITS FROM THING AND FEATURE
		# ATTRIBUTES FROM THING-- need to figure out how to make this inherit
		# id
		# long description - used for look() and first time room visited
		# short description - used for second time room visited
			# also used by Room for Things in Room when look() is called for Room
			# can be based on different statuses, or just default
		# responses : {
		#				[verb] : RESPONSE_TEXT,
		#				[verb] : RESPONSE_TEXT
		#					etc
		#			}
		
		# INHERITED FEATURE ATTRIBUTES
		# takeable: True/False
		# surface: [item1, item2, etc] OR None
		# container: [item1, item2, etc] OR None
		# surface_capacity: (int)
		# container_capacity (int)
		# container_locked : True/False
		# key_needed : some_item
		# container_open : True/False
		# container_closeable: True/False
		# keyboard : True/False

		# INHERITED PUZZLE ATTRIBUTES
		# name: "something"
		# current_status : "whatever"
		# responses: {
		#				status1 : {
		#							[verb]: {
		#									response : RESPONSE_TEXT,
		#									status: new_status
		#							},
		#							[verb]: {
		#									response : RESPONSE_TEXT,
		#									status: None
		#							},
		#										etc
		#						}
		#					etc
		#			}
		# solution: "some final status",
		# end_text: "You solved the puzzle! Take this floppy disk, etc"
		# already_comp_text: "You already got the floppy out of this machine."
		# prize: "some floppy"
		# completed: True/False

		# SPECIAL KeyboardPuzzle ATTRIBUTES
		# keyboard_responses: {					
		#				status1 : {
		#							TEXT: {
		#									response : RESPONSE_TEXT,
		#									status: new_status
		#							},
		#							TEXT: {
		#									response : RESPONSE_TEXT,
		#									status: None
		#							},
		#										etc
		#						}
		#					etc
		# }


	# FUNCTIONS INHERITED FROM PUZZLE:
	# perform_action(verb)
	# check_status()

	# SPECIAL KEYBOARD_PUZZLE FUNCTIONS:
	# type(TEXT) - OVERRIDES GENERIC FUNCTION
		# is the puzzle completed already?
			# if puzzle is completed, say already_comp_text, return false
			# else if puzzle still ongoing,
				#say "You enter TEXT on the keyboard."
				# get current status
				# retrieve responses for current status - responses[current status]
					# is TEXT recognized?
						#if not
							# say "Nothing happened!"
							# return false
						# if TEXT is found in responses[current status]
							# say RESPONSE_TEXT
							# does status change?
								# if response status is not None
									# current_status = response status
									# return True
								# if status does not change, return False

	