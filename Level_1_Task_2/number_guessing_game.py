import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("🎮 Welcome to the Number Guessing Game!")
    print(f"I've picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1

        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            attempts -= 1  # Don't count invalid input
            continue

        if guess < 1 or guess > 100:
            print("⚠️  Please guess between 1 and 100!\n")
            attempts -= 1
            continue

        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}!")
            print(f"You guessed it in {attempts} attempt(s)!")
            break
        elif guess < secret_number:
            print(f"📈 Too Low! ", end="")
        else:
            print(f"📉 Too High! ", end="")

        if attempts < max_attempts:
            print(f"({remaining - 1} attempts remaining)\n")
        else:
            print(f"\n😢 Game Over! The number was {secret_number}.")

number_guessing_game()
