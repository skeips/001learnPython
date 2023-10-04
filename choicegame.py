
# This program is a simple guessing game. The computer generates a random word from a list of words,
# and the player tries to guess the word. If the player guesses the word correctly, they win a point.
# The game continues until the player chooses to stop playing.

import random

# Initialize the score list
score = []

# Create a list of words to choose from
choices = ['apple', 'ball', 'cat', 'dog', 'elephant']

# Start the game loop
while True:

    # Print the list of choices
    print("Welcome to Choose and win Game!!")
    print(choices)

    # Get the player's choice
    your_choice = input('Please type your choice from given list: ')

    # Generate a random word from the list of choices
    my_choice = random.choice(choices)

    # Check if the player guessed the word correctly
    if your_choice == my_choice:

        # The player guessed correctly, so they win a point
        print('You win!')
        score.append(1)

        # Print the current score
        print('The score is:', score)

        # Ask the player if they want to play again
        play_again = input('Please type yes to play again (y/n):')

        # If the player says yes, start the next round of the game
        if play_again == 'y':
            True
        else:
            # If the player says no, break out of the game loop
            break

    # If the player did not guess the word correctly, check if they entered an empty string
    elif your_choice == "":

        # If the player entered an empty string, break out of the game loop
        break

    # Otherwise, the player guessed the word incorrectly
    else:

        # Print a message to the player telling them they guessed incorrectly
        print('You lost!!')

        # Print the computer's choice
        print("Here is my choice: ",my_choice)

        # Ask the player if they want to play again
        play_again = input('Please type yes to play again (y/n):')

        # If the player says yes, start the next round of the game
        if play_again == 'y':
            True
        else:
            # If the player says no, break out of the game loop
            break

# The game loop has ended, so print the final score
print('The score is:', len(score))

#Winning Gifts
if len(score) == 0:
    print("You receive nothing")
elif len(score) == 1:
    print("you received one apple.")
elif len(score) == 2:
    print("you received two balls.")
elif len(score) == 3:
    print("you received three cats.")
elif len(score) == 4:
    print("you received four dogs.")
elif len(score) == 4:
    print("you received five Elephants.")
    print("That's great!!")
