import random

# Uppercase characters in password
def uppercase():
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return letter


# Lowercase characters in password
def lowercase():
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    return letter


# Numbers in password
def numbers():
    pass


# Symbols in password
def symbols():
    pass
