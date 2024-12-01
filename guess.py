import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            # Ask the player to input a guess
            guess = int(input(f"Enter your guess ({attempts} attempts left): "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You guessed it right. The number was {number_to_guess}.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            
            attempts -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

guess_the_number()
