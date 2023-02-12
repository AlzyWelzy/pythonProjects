import random


class NumberGuessingGame:
    def __init__(self, range_min=1, range_max=100):
        self.range_min = range_min
        self.range_max = range_max
        self.high_scores = {}

    def generate_random_int(self):
        return random.randint(self.range_min, self.range_max)

    def get_high_score(self, player):
        return self.high_scores.get(player, 0)

    def set_high_score(self, player, score):
        self.high_scores[player] = score

    def play(self, player):
        random_int = self.generate_random_int()
        high_score = self.get_high_score(player)
        print(
            f"Try to guess the random number between {self.range_min} and {self.range_max}.")
        print(f"{player}'s current high score is {high_score}.")

        for i in range(1, self.range_max + 1):
            try:
                user_int = int(
                    input(f"Enter your guess ({i}/{self.range_max}): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if user_int == random_int:
                print(
                    f"CORRECT! You guessed the random number in {i} guesses.")
                break
            elif user_int < random_int:
                print("Too low!")
            else:
                print("Too high!")
        else:
            print(
                f"You failed to guess the random number ({random_int}) within {self.range_max} guesses.")

        if i < high_score:
            print(
                f"You broke your high score of {high_score} with a score of {i}!")
            self.set_high_score(player, i)


def main():
    game = NumberGuessingGame()

    while True:
        player = input("Enter your name: ")
        game.play(player)

        play_again = input("Do you want to play again (y/n)? ").lower()
        if play_again != "y":
            break


if __name__ == "__main__":
    main()
