#Game: Guess the Secret Number!

import random

def check_if_valid_guess():
    while True:
        try:
            guess = int(input("Take a guess "))
            if guess >= 1 and guess <= 100:
                return guess
            else:
                print("Enter a valid number.")
        except ValueError:
            print("Invalid input! Enter a valid integer.")

def result(guesses_taken, secret_num):
    if guesses_taken:
        print("Good job! You guessed the secret number in " + str(guesses_taken) + " guesses!")
    else:
        print("Wrong! The secret number is: " + str(secret_num))

def game():
    secret_num = random.randint(1, 100) #random num between 1 and 100
    print("You have 5 tries to guess a number between 1 and 100.")

    for guesses_taken in range(1, 6): #loops 5 times
        guess = check_if_valid_guess()

        if guess < secret_num:
            print("Your guess is too low.")
        elif guess > secret_num:
            print("Your guess is too high.")
        else:
            return guesses_taken, secret_num

    return None, secret_num #None if user runs out of guesses

guesses_taken, secret_num = game() #call start game
result(guesses_taken, secret_num) #show result
