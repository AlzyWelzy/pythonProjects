import random

# The game options
options = ['snake', 'water', 'gun']

# The game rules: snake beats water, water beats gun, and gun beats snake
rules = {
    'snake': 'water',
    'water': 'gun',
    'gun': 'snake'
}

# The game loop
while True:
    # Get the player's choice
    player_choice = input("Choose snake, water, or gun: ")

    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid choice, please try again.")
        continue

    # Get the computer's choice
    computer_choice = random.choice(options)
    print(f"The computer chose {computer_choice}.")

    # Compare the choices and determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif rules[player_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? [y/n] ")
    if play_again.lower() != 'y':
        break
