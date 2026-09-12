import random

def generate_secret_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(user_guess, secret_number):
    """Compares the guess with the secret number and returns a hint."""
    if user_guess < secret_number:
        return "Too low"
    elif user_guess > secret_number:
        return "Too high"
    else:
        return "Correct"
