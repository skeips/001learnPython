print("Welcome to simple condition code game")

user_input = input("If you want to play this game type 'y': ").lower()


if user_input == 'y':
    print("Nice Let's play game")
    letters = input("Choose from a-d: ").lower()
    if letters == 'a':
        print("Hello World")
    elif letters == 'b':
        print("Hello You")
    elif letters == 'c':
        print("Hello me")
    elif letters == 'd':
        print("Hello everyone")
else:
    print("Quitting game ....")

