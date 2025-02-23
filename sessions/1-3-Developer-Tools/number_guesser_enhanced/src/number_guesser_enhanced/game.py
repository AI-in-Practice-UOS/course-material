from number_guesser_enhanced.stats import save_score
from number_guesser_enhanced.utils import (
    compare_numbers,
    get_random_number,
    validate_guess,
)


def start_game() -> None:
    print("Starting a new game!")
    number_to_guess = get_random_number(1, 20)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess (1-20): "))
            attempts += 1

            if not validate_guess(user_guess):
                continue

            result = compare_numbers(user_guess, number_to_guess)
            if result == "low":
                print("Too low! Try again.")
            elif result == "high":
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
                name = input("Enter your name: ")
                save_score(name, attempts)
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
