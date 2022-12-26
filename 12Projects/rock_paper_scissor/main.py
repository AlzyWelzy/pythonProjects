import random


class RockPaperScissor:
    def __init__(self):
        self.options = ["rock", "paper", "scissor"]
        self.rules = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "rock"
        }

    def game(self):

        while True:
            player_choice = input("Choose rock, paper, or scissor: ")

            if player_choice not in self.options:
                print("Invalid choice, please try again.")
                continue

            computer_choice = random.choice(self.options)
            print(f"The computer chose {computer_choice}.")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif self.rules[player_choice] == self.rules[computer_choice]:
                print("You win!")
            else:
                print("You lose!")

            player_again = input("Do you want to play again? [y/n].")
            if player_again.lower() != "y":
                break


user = RockPaperScissor()
user.game()
