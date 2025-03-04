import random

def guess_the_number():
    # This keeps track of the best score across multiple rounds
    global high_score
    print("Welcome to 'Guess the Number'!")
    print("Try to guess the number in the fewest attempts possible.")
    print("If you set a new high score, it will be recorded!")

    # Ask for the player's name and age
    name = input("Please enter your name: ")
    try:
        age = int(input("Please enter your age: "))
        if age < 3:
            print(f"Sorry, {name}, you are too young to play this game. Exiting...")
            return  # Exit the game if age is less than 3
    except ValueError:
        print("Please enter a valid age.")
        return  # Exit if age is invalid

    print(f"Hello {name}, let's play the game!")

    # Get range from the player
    try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        if lower_bound >= upper_bound:
            print("The lower bound must be smaller than the upper bound. Please try again.")
            return
    except ValueError:
        print("Please enter valid integers for bounds.")
        return

    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 10

    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Guess a number: ")

        try:
            guess = int(guess)
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Aim higher.")
        elif guess > number_to_guess:
            print("Too high! Aim lower.")
        else:
            print(f"Congratulations, {name}! You guessed the number {number_to_guess} in {attempts} attempts.")
            
            # Update high score
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"New high score: {high_score} attempts!")
            break
    else:
        print(f"Sorry, {name}, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

# Global variable for high score
high_score = None

# Start the game
guess_the_number()
if __name__ == "__main__":
    guess_the_number()
    print(f"The current high score is: {high_score} attempts.")
