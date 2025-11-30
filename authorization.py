from main import load_key
from cryptography.fernet import Fernet


def authorization(login, password, fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            auth_info = line.rstrip()
            lgn, pwd = auth_info.split("|")
            pwd = fernet.decrypt(pwd.encode()).decode()
            if login == lgn and password == pwd:
                return True
    return False


def main():
    key = load_key()
    fernet = Fernet(key)
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if authorization(login, password, fernet):
            print("Вы авторизованы")
            break
        else:
            print("Такого пользоыателя нет")


if __name__ == "__main__":
    main()
