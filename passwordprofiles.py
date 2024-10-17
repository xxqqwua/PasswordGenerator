from passwordoptions import *
import random
import pyperclip


def mixed_register_characters(length):
    lower = upper_n_lower_register_characters(length/2, "lowercase")
    upper = upper_n_lower_register_characters(length/2, "uppercase")
    lower.extend(upper)
    random.shuffle(lower)
    return lower


# Avoid numbers and special characters
def easy_to_remember(length):
    password = ""

    for el in mixed_register_characters(length):
        password += el

    pyperclip.copy(password)
    print(password)


# Any character combination like !, @, #, etc
def all_characters(length):
    mixed_register_characters(length)
    numbers()
    symbols()