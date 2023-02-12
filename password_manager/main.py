from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("./password_manager/key.key", "wb") as key_file:
        key_file.write(key)


write_key()
"""


def load_key():
    file = open("./password_manager/key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pwd = input("What is the master password? ")
# key = load_key() + master_pwd.encode()
key = load_key()
fer = Fernet(key)


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
            print(f"User: {user}\nPassword: {fer.decrypt(passw.encode()).decode()}\n")

        # print("")
        # print(f.read())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("./password_manager/passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


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
