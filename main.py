# This is a number guessing game program
import random  # This imports the random module

# Defining variables
number = random.randint(1, 99)  # Generates a random integer number between 1 and 99 inclusive
guess = int(input("Enter an integer number between 1 and 99 inclusive: "))

# Use a loop to keep asking for the guess until user gets it right or opts out
while number != "guess":
    if guess < number:
        print("Your guess is low.")
        guess = int(input("Enter an integer number between 1 and 99 inclusive: "))
    elif guess > number:
        print("Your guess is high.")
        guess = int(input("Enter an integer number between 1 and 99 inclusive: "))
    else:
        print("You guessed it.")
        break
