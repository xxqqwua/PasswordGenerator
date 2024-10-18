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
    ask_symbols = input("Do you want symbols in password? (y/n) ")
    ask_numbers = input("Do you want numbers in password? (y/n) ")
    ask_upper = input("Do you want uppercase characters in password? (y/n) ")
    ask_lower = input("Do you want lowercase characters in password? (y/n) ")

    password = ""

    list_w_char = []
    list_w_numbers = []
    list_w_sym = []

    if ask_symbols == "y":
        list_w_sym = symbols(length//4)
    if ask_numbers == "y":
        list_w_numbers = [str(el) for el in numbers(length//4)]
    if ask_upper == "y":
        list_w_char.extend(upper_n_lower_register_characters(length//2, "uppercase"))
    if ask_lower == "y":
        list_w_char.extend(upper_n_lower_register_characters(length//2, "lowercase"))

    list_w_char.extend(list_w_numbers)
    list_w_char.extend(list_w_sym)
    random.shuffle(list_w_char)

    for el in list_w_char:
        password += str(el)

    pyperclip.copy(password)
    print(password)


def ios_style():
    part1 = ''.join(upper_n_lower_register_characters(6, "lowercase"))
    part2 = ''.join(upper_n_lower_register_characters(6, "lowercase"))

    part3 = ''.join(upper_n_lower_register_characters(2, "lowercase"))
    part3 += str(numbers(1)[0])
    part3 += upper_n_lower_register_characters(1, "uppercase")[0]
    part3 += ''.join(upper_n_lower_register_characters(2, "lowercase"))

    password = f"{part1}-{part2}-{part3}"

    pyperclip.copy(password)
    print(password)
