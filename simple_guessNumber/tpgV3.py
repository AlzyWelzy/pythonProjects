import random


class Game:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.random_int = random.randint(min_value, max_value)
        self.guesses = 0
        self.user_int = None

    def prompt_guess(self):
        try:
            self.user_int = int(input("Enter a random integer between {} and {}: ".format(
                self.min_value, self.max_value)))
        except:
            print("That's not an int!")
        return self.user_int

    def check_guess(self):
        if self.user_int < self.min_value or self.user_int > self.max_value:
            print("Invalid guess. Please enter a number between {} and {}.".format(
                self.min_value, self.max_value))
            return False
        if self.random_int == self.user_int:
            print(
                f"CORRECT! The Random Number was {self.random_int} and you guessed it in {self.guesses}.")
            return True
        else:
            if self.user_int < self.random_int:
                self.guesses += 1
                print("Too Low!")
            else:
                self.guesses += 1
                print("Too High!")
            return False

    def get_score(self):
        return self.guesses


class NumberGuessingGame(Game):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)


class Scoreboard:
    def __init__(self, filename):
        self.filename = filename
        self.high_score = self.read_high_score()

    def read_high_score(self):
        with open(self.filename, "r") as f:
            high_score = int(f.read())
        return high_score

    def update_high_score(self, new_score):
        with open(self.filename, "w") as f:
            f.write(str(new_score))
        self.high_score = new_score


# Create a new game and a scoreboard
game = NumberGuessingGame(1, 100)
scoreboard = Scoreboard("Project 2/hiscore.txt")

# Play the game until the user guesses the correct number
while not game.check_guess():
    game.prompt_guess()

# Get the user's score for the current game
score = game.get_score()

# Print the current high score
print(f"Your current high score is {scoreboard.high_score}.")

# If the user's score for the current game is higher than their high score, update the high score
if score > scoreboard.high_score:
    print(
        f"You broke your high score that was {scoreboard.high_score}. Your new high score is {score}.")
    scoreboard.update_high_score(score)
