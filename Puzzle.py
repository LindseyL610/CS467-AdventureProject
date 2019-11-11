import os
import json

class Puzzle: # SUBCLASS OF FEATURE
	def __init__(self, data, state):
		# PUZZLE INHERITS FROM THING AND FEATURE
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

		# SPECIAL PUZZLE ATTRIBUTES
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
		# end_text: "Something happened! You get a something!"
		# already_comp_text: "Nothing happens."
		# prize: "item or skill"
		# completed: True/False
		
	# perform_action(verb) - OVERRIDE GENERIC
		# is the puzzle completed already?
			# if puzzle is completed, say aleady_comp_text, return false
			# else if puzzle still ongoing,
				#say "You [verb] the [name]."
				# get current status
				# retrieve responses for current status - responses[current status]
					# is [verb] recognized?
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

	# check_status()
		# if current_status is not solution
			# return false
		# else, if current status IS soluation
			# completed = True
			# say end_text
			# return true

	