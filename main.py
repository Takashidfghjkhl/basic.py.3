import os
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    return key


def add(fernet):
    login = input("введите логин: ")
    password = input("введите пароль: ")
    with open("passwords.txt", "w") as f:
        f.write(f"{login}|{fernet.encrypt(password.encode()).decode()}")


def view(fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            auth_info = line.rstrip()
            login, password = auth_info.split("|")
            print(f"Логин: {login} | Пароль: {fernet.decrypt(password.encode()).decode()}\n")


def main():
    if not os.path.exists("key.key"):
        write_key()

    key = load_key()
    fernet = Fernet(key)

    while True:
        action = input("Хотите добавить новый пароль или посмотреть уже существующие. 1. Посмотреть, 2. Добавить? Нажмите 3 чтобы выйти ")
        if action == "1":
            view(fernet)
        elif action == "2":
            add(fernet)
        else:
            break


if __name__ == "__main__":
    main()
