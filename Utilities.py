import textwrap
import platform

OS = platform.system()
WRAPPER = textwrap.TextWrapper(replace_whitespace=False, width=80)

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

COLORS['<DIGITAL_TEXT>'] = COLORS['<green>']
COLORS['<WRITTEN_TEXT>'] = COLORS['<blue>']
COLORS['<SPOKEN_TEXT>'] = COLORS['<yellow>']
COLORS['<CLUE>'] = COLORS['<red>']


# basic function to display messages to the user. handles text wrapping and formatting
# TODO this may be where we want to handle displaying text of different colors
#  perhaps we come up with a key string (like <colorbegin:red>this text is red<colorend> or something)
#  that this function can find and replace with the necessary output for formatted text
def say(text):
	#if there is no string data, do nothing
	if text is not None and (text == "") is False and isinstance(text, str):
		text = text + "</>"
		text = text.split('\n')

		for line in text:
			#print(line)
			line_cpy = line

			#Color only supported on Linux/Mac
			if OS == "Linux" or OS == "Darwin":
				SPECIAL_CHAR = '`'
				tags = dict()
				indexes = list()

				for color in COLORS:
					index = line_cpy.find(color)
					while index != -1:
						tags[str(index)] = color
						indexes.append(index)
						line_cpy = line_cpy.replace(color,SPECIAL_CHAR,1)
						index = line_cpy.find(color)

				indexes.sort()

				line_wrapped = WRAPPER.fill(line_cpy)

				for i in indexes:
					line_wrapped = line_wrapped.replace(SPECIAL_CHAR,COLORS[tags[str(i)]], 1)

			else:
				for color in COLORS:
					line_cpy = line_cpy.replace(color, "")
				line_wrapped = WRAPPER.fill(line_cpy)
			
			print(line_wrapped)

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
      if thing.name.lower() == name.lower():
        return thing
  # for set or list, just search all elements
  else:
    for thing in group_to_search:
      if thing.name.lower() == name.lower():
        return thing
  return None


# def find_by_name(name, dict_to_search):
#   for thing in dict_to_search.values():
#     if thing.name == name:
#       return thing
#   return None

TEST = \
    "A stack of printed out emails between family members. As you glance through them, " \
    "there are several sentences in different messages that stand out to you. " \
    "There's something not quite right about them, " \
    "like someone has been <CLUE>injecting</> things into them. " \
    "Now it seems as if they're speaking <CLUE>different languages</>, " \
    "and there's something <CLUE>in their words</> that makes you think they're " \
    "going against their <CLUE>programming</>. \n" \
    "Here are the strange sentences: \n" \
    "<WRITTEN_TEXT>\"I'll need a chainsaw if the trees keep growing so </><CLUE>fast</><WRITTEN_TEXT>.\" \n " \
    "\"Better to have wanderlust than to let your dreams </><CLUE>corrode</><WRITTEN_TEXT>.\" \n" \
    "\"To give my mojo a valuable boost, I drink some strong </><CLUE>coffee</><WRITTEN_TEXT>.\" \n" \
    "\"I'm going to run by the jewelers, to buy a </><CLUE>gemstone</><WRITTEN_TEXT>.\" \n" \
    "\"Isn't therapy the one thing that will help your fear of </><CLUE>snakes</><WRITTEN_TEXT>?\""

print(TEST)
say(TEST)