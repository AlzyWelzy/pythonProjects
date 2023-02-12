import random

choices = {
    1: "snake",
    2: "water",
    3: "gun"
}

rounds = 1

player = 0
comp = 0


def game():
    global player, comp
    playerChoice = int(
        input("Enter a choice \n 1 Snake \n 2 Water \n 3 Gun \n"))
    compChoice = random.randint(1, 3)

    if (playerChoice > 3 or playerChoice < 0):
        print("Enter valid value")

    if (choices[playerChoice] == choices[compChoice]):
        print("TIE")

    elif (choices[playerChoice] == choices[1] and choices[compChoice] == choices[2]):
        print(
            f"You WON! {choices[compChoice]} lost to {choices[playerChoice]}")

        player += 1

    elif (choices[playerChoice] == choices[2] and choices[compChoice] == choices[3]):
        print(
            f"You LOST! {choices[playerChoice]} lost to {choices[compChoice]}")

        comp += 1

    elif (choices[playerChoice] == choices[3] and choices[compChoice] == choices[1]):
        print(
            f"You WON! {choices[compChoice]} lost to {choices[playerChoice]}")

        player += 1

    elif (choices[playerChoice] == choices[2] and choices[compChoice] == choices[1]):
        print(
            f"You LOST! {choices[compChoice]} lost to {choices[playerChoice]}")

        comp += 1

    elif (choices[playerChoice] == choices[2] and choices[compChoice] == choices[3]):
        print(
            f"You WON! {choices[playerChoice]} lost to {choices[compChoice]}")

        player += 1

    elif (choices[playerChoice] == choices[1] and choices[compChoice] == choices[3]):
        print(
            f"You LOST! {choices[playerChoice]} lost to {choices[compChoice]}")

        comp += 1

    else:
        return "error"


print("Snake - Water - Gun")


while rounds <= 10:
    game()
    rounds += 1

if player > comp:
    print(f"You have won by {player} wins and {comp} losses")
else:
    print(f"You have lost by {comp} losses and {player} wins")
