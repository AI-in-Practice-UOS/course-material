from number_guesser_enhanced.game import start_game
from number_guesser_enhanced.stats import display_leaderboard


def main() -> None:
    print("Welcome to the Enhanced 'Guess the Number' Game!")
    print("1. Play Game")
    print("2. View Leaderboard")
    choice = input("Choose an option: ")

    if choice == "1":
        start_game()
    elif choice == "2":
        display_leaderboard()
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
