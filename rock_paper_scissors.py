# This program lets a user play Rock, Paper, Scissors against the computer.
import random

def choice_random():
    # Generate a random number.
    keep_going = 'y'

    print()
    while keep_going == 'y':
        choice = {1: 'rock', 2: 'paper', 3: 'scissors'}
        num = user_input()
        print()
        print('You picked ', choice[num])

        # Get a random number and compare it to the number entered.
        comp = random.randint(1, 3)

        print('The computer pick', choice[comp])

        decider(num, comp)

        keep_going = (input("Do you want to play again: enter, 'y', for " + \
        "yes anything else for no "))

def decider (num, comp):
    if num == comp:
        print("It's a draw ")

    # If the two numbers are different, then figure out who wins.
    elif num == 1 and comp == 2:
        print('The computer wins, rock loses to paper')
    elif num == 1 and comp == 3:
         print('The computer loses, scissors loses to rock')
    elif num == 2 and comp == 3:
         print('The computer wins, paper loses to scissors')
    elif num == 2 and comp ==1:
        print('The computer loses, rock loses to paper')
    elif num == 3 and comp ==1:
        print('The computer wins, scissors loses to rock')
    elif num == 3 and comp == 2:
        print('The computer loses, paper loses to scissors')
    else:
        print('Good game')

# Get player's input.
def user_input():
    # Enter a number.
    number = int(input('Enter a number, 1 = rock, 2 = paper and 3 = scissors : '))
    while number < 1 or number > 3:
        print('Please enter a valid number')
        number = int(input('Enter a number, 1 = rock, 2 = paper and 3 = scissors : '))
    print()
    return number
def main():

    choice_random()


# Call the main function.
if __name__ == '__main__':
    main()
