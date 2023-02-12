import random


def game(randomInt):
    guesses = 0
    userInt = 0

    while (randomInt != userInt):
        try:
            userInt = int(input("Enter a random integer between 1 to 100: "))
        except Exception as e:
            print("That's not an int!")
        if userInt < 1 or userInt > 100:
            print("Invalid guess. Please enter a number between 1 and 100.")
            continue
        if (randomInt == userInt):
            print(
                f"CORRECT! The Random Number was {randomInt} and you guessed it in {guesses}.")
        else:
            if (userInt < randomInt):
                guesses += 1
                print("Too Low!")
            else:
                guesses += 1
                print("Too High!")
    return guesses


randomInt = random.randint(1, 100)
score = game(randomInt)


with open("Project 2/hiscore.txt", "r") as f:
    hiScore = int(f.read())
    print(f"Your current high score is {hiScore}.")

if (score > hiScore):
    print(
        f"You broke your high score that was {hiScore}. Your new high score is {score}.")
    with open("Project 2/hiscore.txt", "w") as f:
        f.write(str(score))
