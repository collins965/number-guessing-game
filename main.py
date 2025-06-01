import random
import os

# Constants
EASY = 10
MEDIUM = 7
HARD = 5
HINT_AFTER_TRIES = 3
LEADERBOARD_FILE = "leaderboard.txt"

def choose_difficulty():
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
        print("Invalid choice, defaulting to Easy.")
        return EASY

def give_hint(number):
    if number % 2 == 0:
        return "Hint: The number is even."
    elif number % 3 == 0:
        return "Hint: The number is divisible by 3."
    elif number % 5 == 0:
        return "Hint: The number is divisible by 5."
    else:
        return "Hint: The number is a prime or tricky one!"

def save_score(username, attempts_used):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{username},{attempts_used}\n")

def display_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("No leaderboard data yet.")
        return

    print("\n Leaderboard:")
    with open(LEADERBOARD_FILE, "r") as file:
        scores = [line.strip().split(",") for line in file.readlines()]
        scores = sorted(scores, key=lambda x: int(x[1]))
        for i, (user, score) in enumerate(scores[:5], start=1):  # Show top 5
            print(f"{i}. {user} - {score} attempts")

def play_game():
    print(" Welcome to the Number Guessing Game!")
    username = input("Enter your username: ")
    max_attempts = choose_difficulty()
    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nGuess a number (1-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == number:
            print(f" Correct! You guessed it in {attempts} tries.")
            save_score(username, attempts)
            break
        elif guess < number:
            print(" Too low.")
        else:
            print(" Too high.")

        if attempts >= HINT_AFTER_TRIES:
            print(give_hint(number))

        print(f" Remaining guesses: {remaining}")

    else:
        print(f" Out of attempts. The number was {number}. Better luck next time!")

    display_leaderboard()

# Run the game
if __name__ == "__main__":
    play_game()
