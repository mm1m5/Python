#Game: Rock, Paper, Scissors
import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK:'🪨', PAPER:'📄',SCISSORS:'✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Type 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower() #converts input to lowercase
        if user_choice not in choices:  #not in checks if value is not presesent in a sequence
            print('Invalid choice!')
            continue  #goes back to loop
        else:
            return user_choice

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]} ')
    print(f'Computer chose {emojis[computer_choice]} ')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
            (user_choice == ROCK and computer_choice == SCISSORS) or
            (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSORS and computer_choice == PAPER)):
        print('You win!')
    else:
        print('You lose!')

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices) #comp picks random choice between r,p,s

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower() #continue game?
        if should_continue == 'n':
            break #exit

play_game() #start game