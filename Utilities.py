import textwrap

# basic function to display messages to the user. handles text wrapping and formatting
# TODO this may be where we want to handle displaying text of different colors
#  perhaps we come up with a key string (like <colorbegin:red>this text is red<colorend> or something)
#  that this function can find and replace with the necessary output for formatted text
def say(string):
    print(textwrap.fill(string))
    # print string


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