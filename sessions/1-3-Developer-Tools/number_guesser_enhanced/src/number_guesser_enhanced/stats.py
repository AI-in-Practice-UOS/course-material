import json

LEADERBOARD_FILE = "leaderboard.json"


def save_score(name: str, attempts: int) -> None:
    """Save the player's score to the leaderboard."""
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    leaderboard.append({"name": name, "attempts": attempts})
    leaderboard = sorted(leaderboard, key=lambda x: x["attempts"])[
        :10
    ]  # Keep top 10 scores

    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)


def display_leaderboard() -> None:
    """Display the top 10 players from the leaderboard."""
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = json.load(file)

        print("\n--- Leaderboard ---")
        for idx, entry in enumerate(leaderboard, start=1):
            print(f"{idx}. {entry['name']} - {entry['attempts']} attempts")
        print("-------------------\n")
    except FileNotFoundError:
        print("No leaderboard data found. Play a game first!")
