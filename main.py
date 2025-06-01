import random  # For generating random numbers
import os      # For file and path operations

# Constants for the number of tries based on difficulty levels
EASY = 10
MEDIUM = 7
HARD = 5

# After how many tries a hint will be given
HINT_AFTER_TRIES = 3

# File name for storing leaderboard data
LEADERBOARD_FILE = "leaderboard.txt"

def choose_difficulty():
    """
    Ask the user to choose a difficulty level and return
    the corresponding maximum number of attempts.
    """
    print("Choose difficulty level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    choice = input("Enter 1, 2 or 3: ")
    if choice == "1":
        return EASY
    elif choice == "2":
        return MEDIUM
    elif choice == "3":
        return HARD
    else:
        # If invalid input, default to Easy difficulty
        print("Invalid choice, defaulting to Easy.")
        return EASY

def give_hint(number):
    """
    Provide a hint about the target number based on
    simple divisibility rules.
    """
    if number % 2 == 0:
        return "Hint: The number is even."
    elif number % 3 == 0:
        return "Hint: The number is divisible by 3."
    elif number % 5 == 0:
        return "Hint: The number is divisible by 5."
    else:
        # If none of the above, number might be prime or less straightforward
        return "Hint: The number is a prime or tricky one!"

def save_score(username, attempts_used):
    """
    Append the user's name and number of attempts
    used to the leaderboard file.
    """
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{username},{attempts_used}\n")

def display_leaderboard():
    """
    Display the top 5 scores (lowest attempts) from the leaderboard.
    If the leaderboard file doesn't exist, inform the user.
    """
    if not os.path.exists(LEADERBOARD_FILE):
        print("No leaderboard data yet.")
        return

    print("\nLeaderboard:")
    with open(LEADERBOARD_FILE, "r") as file:
        # Read all scores and split into username and attempts
        scores = [line.strip().split(",") for line in file.readlines()]
        # Sort scores based on attempts (convert string to int)
        scores = sorted(scores, key=lambda x: int(x[1]))
        # Print top 5 scores
        for i, (user, score) in enumerate(scores[:5], start=1):
            print(f"{i}. {user} - {score} attempts")

def play_game():
    """
    Main game loop: prompt for username, difficulty, and guesses.
    Provides feedback, hints, and updates leaderboard.
    """
    print("Welcome to the Number Guessing Game!")
    username = input("Enter your username: ")
    max_attempts = choose_difficulty()
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nGuess a number (1-100): "))
        except ValueError:
            # Handle non-integer inputs gracefully
            print("Please enter a valid number.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == number:
            print(f"Correct! You guessed it in {attempts} tries.")
            save_score(username, attempts)
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

        # Give a hint after a certain number of failed attempts
        if attempts >= HINT_AFTER_TRIES:
            print(give_hint(number))

        print(f"Remaining guesses: {remaining}")

    else:
        # This block executes if while loop completes without a break (i.e., no correct guess)
        print(f"Out of attempts. The number was {number}. Better luck next time!")

    # Show leaderboard at the end of the game
    display_leaderboard()

# Run the game if this script is executed directly
if __name__ == "__main__":
    play_game()
