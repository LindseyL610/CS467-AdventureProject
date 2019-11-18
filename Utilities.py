import textwrap
import platform

OS = platform.system()
WRAPPER = textwrap.TextWrapper()
COLOR = "\033[1;32;40m"
DEFAULT = "\033[0m"

# basic function to display messages to the user. handles text wrapping and formatting
# TODO this may be where we want to handle displaying text of different colors
#  perhaps we come up with a key string (like <colorbegin:red>this text is red<colorend> or something)
#  that this function can find and replace with the necessary output for formatted text
def say(text, game = None):
	#if there is no string data, do nothing
	if text is not None and (text == "") is False:
		#see if game object was passed (for color)
		if game is not None:
			#Color only supported on Linux/Mac
			if OS == "Linux" or OS == "Darwin":
				#find each instance of each key word
				for word in game.keywords:
					start_idx = 0
					start = 0

					while start is not -1:
						start = text.find(word, start_idx)
						end = start + len(word) - 1

						#insert color cords before and after each instance
						if start is not -1:
							text = text[0:start] + COLOR + word + DEFAULT + text[end+1:]

						start_idx = text.find(word,start_idx) + len(word)

		print(WRAPPER.fill(text))

def list_to_words(object_list):
  list_length = len(object_list)
  list_string = ""
  if list_length > 0:
    for i in range(list_length):
      # if there are at least 2 words, add "and" to final word
      if i == (list_length - 1) and list_length >= 2:
        list_string += " and"

      # display word
      list_string += " " + object_list[i]

      # if there are at least 3 words, add comma to all but final word
      if i != (list_length - 1) and list_length >= 3:
        list_string += ","

  return list_string

# list_to_words tests
# test_list1 = ["this", "that", "the other"]
# test_list2 = ["salt", "pepper"]
# test_list3 = ["highlander"]
# print("testing list_to_words")
# print(list_to_words(test_list1))
# print(list_to_words(test_list2))
# print(list_to_words(test_list3))
