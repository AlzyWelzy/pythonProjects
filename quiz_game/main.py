print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no)")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")
score = 0

qa_dict = {
    "cpu": "central processing unit",
    "gpu": "graphics processing unit",
    "ram": "Random Access Memory",
    "psu": "power supply unit",
}

for key, value in qa_dict.items():
    answer = input(f"What does {key.upper()} stands for? ")
    if answer.lower() == value:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score/4)*100}%")
