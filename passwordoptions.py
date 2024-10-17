import random


# Uppercase 'n' lowercase characters in password
def upper_n_lower_register_characters(length, register):
    def create_characters(length, roster, characters):
        while len(characters) < length:
            letter = random.choice(roster)
            characters.append(letter)
        return characters

    if register == "uppercase":
        uppercases_characters = []
        create_characters(length, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", uppercases_characters)
        return uppercases_characters

    elif register == "lowercase":
        lower_characters = []
        create_characters(length, "abcdefghijklmnopqrstuvwxyz", lower_characters)
        return lower_characters


# Numbers in password
def numbers(length):
    pass


# Symbols in password
def symbols(length):
    pass
