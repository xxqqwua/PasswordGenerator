from passwordoptions import *
import random
import pyperclip


def mixed_register_characters(length):
    lower = upper_n_lower_register_characters(length//2, "lowercase")
    upper = upper_n_lower_register_characters(length//2, "uppercase")
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
    password = ""

    list_w_char = mixed_register_characters(length//2)
    list_w_numbers = [str(el) for el in numbers(length//4)]
    list_w_sym = symbols(length//4)

    list_w_char.extend(list_w_numbers)
    list_w_char.extend(list_w_sym)
    random.shuffle(list_w_char)

    for el in list_w_char:
        password += str(el)

    pyperclip.copy(password)
    print(password)


def custom(length):
    pass