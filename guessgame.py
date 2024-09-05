import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")

    # Get range from the player
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 10
    high_score = None
    
    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Guess a number: ")

        try:
            guess = int(guess)
            attempts += 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            
            # Update high score
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"New high score: {high_score} attempts!")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

# Start the game
guess_the_number()
