from passwordprofiles import *

def main():
    password = False
    while not password:
        try:
            length = int(input("Enter the length of the password: "))
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

        user_choose = input("Choose a profile (1. Easy to remember 2. Strong (0 - Exit)): ")

        if 'easy' in user_choose or '1' in user_choose:
            easy_to_remember(length)
            password = True
        elif 'strong' in user_choose or '2' in user_choose:
            all_characters(length)
            password = True
        elif user_choose == '0':
            break
        else:
            print('Invalid input')
            continue


if __name__ == '__main__':
    main()