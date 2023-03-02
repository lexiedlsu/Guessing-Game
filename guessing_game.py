# Python has a number of built-in functions. One of which is the random module. Use the module to generate a random number - import random
import random

# The code will generate a random integer
hidden_number = random.randint(0,100)

print("Guess the Number!\n")
# Use a looping function for the 10 chances/trials
for n in range(0,10):
    guess = int(input("Enter a number between 1 and 100: "))

    # Use the print function to display if the guess is too low, too high, or correct
    if guess > hidden_number:
        print("Too High\n")

    elif guess < hidden_number:
        print("Too Low\n")

    else:
        print("Correct\n")
        break   # Use the break function if the guess is correct

print()

# If the guess is correct, print the number of guesses, and the correct number
if guess == hidden_number:
    print("Number of Guesses: ", n)
    print("Hidden Number was: ", hidden_number)

# Else, print the random number
else:
    print("Out of guesses, the hidden number was: ", hidden_number)