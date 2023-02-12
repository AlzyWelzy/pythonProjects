import random
from pathlib import Path


class GuessNumber:
    def __init__(self):
        self.randNum = None
        self.guessNum = 0
        self.guesses = 0

    @staticmethod
    def hiscore(guesses):
        hi_score_file = Path("hiscore.txt")
        if hi_score_file.exists():
            with open(hi_score_file, "r") as f:
                cur_hi_score = int(f.read())
            if cur_hi_score > guesses:
                with open(hi_score_file, "w") as f:
                    f.write(str(guesses + 1))
                    print(
                        f"YOU HAVE SURPASSED YOUR PREVIOUS HIGH SCORE {cur_hi_score}, YOUR NEW HIGH SCORE IS {guesses + 1}."
                    )
        else:
            with open(hi_score_file, "w") as f:
                f.write(str(guesses + 1))
                print(
                    f"High score file not found. Creating new high score with value {guesses + 1}."
                )

    def guess(self, max_value):
        self.randNum = random.randint(1, max_value)
        while self.randNum != self.guessNum:
            try:
                self.guessNum = int(
                    input(f"Enter a positive integer between 1 to {max_value}: ")
                )
                if self.guessNum < 1 or self.guessNum > max_value:
                    print(
                        "Invalid input. Please enter a positive integer between 1 to {max_value}."
                    )
                    continue
                if self.randNum == self.guessNum:
                    print(
                        f"You managed to complete the game in {self.guesses + 1} guesses."
                    )
                    self.hiscore(self.guesses)
                else:
                    if self.guessNum > self.randNum:
                        print("Too High")
                        self.guesses += 1
                    elif self.guessNum < self.randNum:
                        print("Too Low")
                        self.guesses += 1
            except ValueError:
                print(
                    "Invalid input. Please enter a positive integer between 1 to {max_value}."
                )

    @staticmethod
    def comp_guess(max_value):
        guesses = 0
        try:
            user = int(input("Enter a positive integer between 1 to max_value: "))
            if user < 1 or user > max_value:
                print(
                    "Invalid input. Please enter a positive integer between 1 to {max_value}."
                )
                return
            comp = 0
            while user != comp:
                comp = random.randint(1, max_value)
                if user == comp:
                    print(f"Computer guesses it in {guesses + 1} guesses.")
                else:
                    if comp > user:
                        guesses += 1
                        print("Too High")
                    else:
                        guesses += 1
                        print("Too Low")
        except ValueError:
            print(
                "Invalid input. Please enter a positive integer between 1 to {max_value}."
            )


print("Welcome to the Number guessing game.")

try:
    max_value = int(input("Enter a positive integer: "))
except Exception as e:
    print(e)
else:
    newU = GuessNumber()
    # newU.comp_guess(max_value)
    newU.guess(max_value)
