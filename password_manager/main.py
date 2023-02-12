master_pwd = input("What is the master password? ")


def view():
    with open("./password_manager/passwords.txt", "r") as f:
        for line in f.readlines():
            # print(line.strip())
            data = line.strip()
            # print(data)
            # print(data.split("|"))
            user, passw = data.split("|")
            # print(user)
            # print(passw)
            print(f"User: {user}\nPassword: {passw}\n")

        # print("")
        # print(f.read())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("./password_manager/passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), enter 'q' to quit? ".lower()
    )

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
