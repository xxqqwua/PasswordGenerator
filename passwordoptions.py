import random


def create_characters(length, roster):
    characters = []
    while len(characters) < length:
        letter = random.choice(roster)
        characters.append(letter)
    return characters


# Uppercase 'n' lowercase characters in password
def upper_n_lower_register_characters(length, register):
    if register == "uppercase":
        return create_characters(length, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elif register == "lowercase":
        return create_characters(length, "abcdefghijklmnopqrstuvwxyz")


# Numbers in password
def numbers(length):
    return create_characters(length, "0123456789")


# Symbols in password
def symbols(length):
    return create_characters(length, "!@#$%^&*()_+-=[]{}|;:,.<>/?")
