from passwordoptions import *

# Avoid numbers and special characters
def easy_to_say(length):
    uppercase()
    lowercase()


# Avoid ambiguous characters like l, 0, 1, etc
def easy_to_read(length):
    pass


# Any character combination like !, @, #, etc
def all_characters(length):
    uppercase()
    lowercase()
    numbers()
    symbols()
