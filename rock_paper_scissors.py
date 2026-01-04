# This program is to PLAY Rock-Paper_scissors game. Enjoy!!
# `random` module, nested `if/else` statements
import random


def get_choices():
    # try:
    player_choice = input("Enter your choice (rock/paper/scissors) :").lower().strip()
    # except:
    #     print(f"Invalid entry. Try again!")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player choice' : player_choice, 'computer choice' : computer_choice}
    return choices

def check_win(player, computer):
    result = 0
    try:
        if computer == player:
            output = 'It is a Tie!'
            print(f"You chose {player}, computer chose {computer}. {output}")
            result = 0
        elif computer == 'rock':
            if player == 'paper':
                output = 'You won!'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = 1
            elif player == 'scissors':
                output = 'You lose.'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = -1
        elif computer == 'paper':
            if player == 'scissors':
                output = 'You won!'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = 1
            elif player == 'rock':
                output = 'You lose.'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = -1
        elif computer == 'scissors':
            if player == 'rock':
                output = 'You won!'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = 1
            elif player == 'paper':
                output = 'You lose.'
                print(f"You chose {player}, computer chose {computer}. {output}")
                result = -1
        return result
    except (UnboundLocalError, TypeError):
        print("Please enter a valid input. (rock/paper/scissors)")
        return 0
    

print(f"Welcome to Rock-Paper-Scissors game, it contains negative marking".center(100, '_'))
try:
    query = int(input("How many matches you wanna play ? :"))
    score = 0
    print(type(score))
    for i in range(query):
        choices = get_choices()
        score += check_win(choices['player choice'], choices['computer choice'])
    print(f"You scored {score} out of {query}. ( {score}/{query} )")
except ValueError:
    print("Please enter a valid non-negative integer.")


