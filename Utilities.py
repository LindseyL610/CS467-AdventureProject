import textwrap
import platform

OS = platform.system()
WRAPPER = textwrap.TextWrapper(replace_whitespace=False)
COLOR = "\033[1;32;40m"
DEFAULT = "\033[0m"

#NOTE: The following color table was adapted from: https://stackoverflow.com/questions/17771287/python-octal-escape-character-033-from-a-dictionary-value-translates-in-a-prin
COLORS = {
    '<white>': "\033[1;37m",
    '<yellow>': "\033[1;33m",
    '<green>': "\033[1;32m",
    '<blue>': "\033[1;34m",
    '<cyan>': "\033[1;36m",
    '<red>': "\033[1;31m",
    '<magenta>': "\033[1;35m",
    '<black>': "\033[1;30m",
    '<darkwhite>': "\033[0;37m",
    '<darkyellow>': "\033[0;33m",
    '<darkgreen>': "\033[0;32m",
    '<darkblue>': "\033[0;34m",
    '<darkcyan>': "\033[0;36m",
    '<darkred>': "\033[0;31m",
    '<darkmagenta>': "\033[0;35m",
    '<darkblack>': "\033[0;30m",
    '</>': "\033[0;0m"
}

TEST_STR = "<darkcyan>This should be dark cyan</>. This should be back to default. <red>This should be red</>."

# basic function to display messages to the user. handles text wrapping and formatting
# TODO this may be where we want to handle displaying text of different colors
#  perhaps we come up with a key string (like <colorbegin:red>this text is red<colorend> or something)
#  that this function can find and replace with the necessary output for formatted text
def say(text):
	#if there is no string data, do nothing
	if text is not None and (text == "") is False and isinstance(text, str):
		for color in COLORS:
			#Color only supported on Linux/Mac
			if OS == "Linux" or OS == "Darwin":
				text = text.replace(color, COLORS[color])
			else:
				text = text.replace(color, "")

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

def find_by_name(name, group_to_search):
  # for dicts, search all values
  if type(group_to_search) is dict:
    for thing in group_to_search.values():
      if thing.name == name:
        return thing
  # for set or list, just search all elements
  else:
    for thing in group_to_search:
      if thing.name == name:
        return thing
  return None


# def find_by_name(name, dict_to_search):
#   for thing in dict_to_search.values():
#     if thing.name == name:
#       return thing
#   return None

print(TEST_STR)
say(TEST_STR)