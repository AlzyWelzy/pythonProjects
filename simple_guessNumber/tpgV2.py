import random
import time


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

        start_time = time.time()
        for i in range(1, self.range_max + 1):
            try:
                user_int = int(
                    input(f"Enter your guess ({i}/{self.range_max}): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if user_int == random_int:
                end_time = time.time()
                elapsed_time = end_time - start_time
                score = (self.range_max - i) * 100 - elapsed_time
                print(
                    f"CORRECT! You guessed the random number in {i} guesses and {elapsed_time:.2f} seconds.")
                print(f"Your score is {score:.2f}.")
                break
            elif user_int < random_int:
                print("Too low!")
            else:
                print("Too high!")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"You failed to guess the random number ({random_int}) within {self.range_max} guesses.")
            print(f"Your time was {elapsed_time:.2f} seconds.")
            score = 0

        if score > high_score:
            print(
                f"You broke your high score of {high_score} with a score of {score:.2f}!")
            self.set_high_score(player, score)


def main():
    game = NumberGuessingGame()

    while True:
        print("Number Guessing Game")
        print("1. Play game")
        print("2. View high scores")
        print("3. Set custom range")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player = input("Enter your name: ")
            game.play(player)
        elif choice == "2":
            for player, score in game.high_scores.items():
                print(f"{player}: {score:.2f}")
