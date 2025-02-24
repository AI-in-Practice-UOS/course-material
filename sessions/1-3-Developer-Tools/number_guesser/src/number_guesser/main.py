import random


def main() -> None:
    print("Starting a new game!")
    number_to_guess = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess (1-20): "))
            attempts += 1

            if user_guess < 1 or user_guess > 20:
                continue

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
