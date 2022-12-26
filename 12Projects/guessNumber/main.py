import random


class Guess_Number:
    def __init__(self):
        self.guessNum = 0
        self.guesses = 0

    @staticmethod
    def hiScore(guesses):
        with open("./12Projects/guessNumber/hiScore.txt") as f:
            curHiScore = int(f.read())

        if curHiScore > guesses:
            with open('./12Projects/guessNumber/hiScore.txt', "w") as f:
                f.write(str(guesses))
                print(
                    f"YOU HAVE SURPASSED YOUR PREVIOUS HIGH SCORE THAT WAS {curHiScore}, YOUR NEW HIGH SCORE IS {guesses}.")

    def guess(self):
        self.randNum = random.randint(1, 1000000000)

        while self.randNum != self.guessNum:

            try:
                self.guessNum = int(
                    input("Enter a positive integer between 1 to 1000: "))
                if self.randNum == self.guessNum:
                    print(
                        f"You managed to complete the game in {self.guesses}.")
                    self.hiScore(self.guesses)
                else:
                    if self.guessNum > self.randNum:
                        print("Too High")
                        self.guesses += 1
                    elif self.guessNum < self.randNum:
                        print("Too Low")
                        self.guesses += 1

            except Exception as e:
                print(e)


newU = Guess_Number()

newU.guess()
