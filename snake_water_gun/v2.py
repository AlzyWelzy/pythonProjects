# The three possible choices in the game
choices = ["snake", "water", "gun"]

# A dictionary mapping the player's choice to the result
results = {
    "snake": {
        "snake": "Draw!",
        "water": "You win!",
        "gun": "You lose!"
    },
    "water": {
        "snake": "You lose!",
        "water": "Draw!",
        "gun": "You win!"
    },
    "gun": {
        "snake": "You win!",
        "water": "You lose!",
        "gun": "Draw!"
    }
}

# The main game loop
while True:
    # Get the player's choice
    player_choice = input("Choose snake, water, or gun: ")

    # Check if the player's choice is valid
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Get the computer's choice
    import random
    computer_choice = random.choice(choices)

    # Print the result
    print(f"You chose {player_choice}, the computer chose {computer_choice}")
    print(results[player_choice][computer_choice])
