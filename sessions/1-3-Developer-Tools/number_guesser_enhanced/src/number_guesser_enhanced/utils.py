import random


def get_random_number(start: int, end: int) -> int:
    """Generate a random number between start and end."""
    return random.randint(start, end)


def validate_guess(guess: int) -> bool:
    """Validate the user's guess."""
    if guess < 1 or guess > 20:
        print("Please guess a number between 1 and 20.")
        return False
    return True


def compare_numbers(user_guess: int, number_to_guess: int) -> str:
    """Compare the user's guess with the number to guess."""
    if user_guess < number_to_guess:
        return "low"
    elif user_guess > number_to_guess:
        return "high"
    else:
        return "correct"
