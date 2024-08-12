import os
from cryptography.fernet import Fernet

# Files we create
username = "username.txt"
key_file = "key.key"
filepwd = "PassManger.txt"
encrypted_master_file = "encrypted_master.txt"

# Function to check if there's a user or not
def get_user_name():
    if os.path.exists(username):
        with open(username, "r") as file:
            name = file.readline().strip()
            print(f"Welcome back, {name}!")
    else:
        name = input("Hello! What's your name? ")
        with open(username, "w") as file:
            file.write(name + '\n')
        print(f"Nice to meet you, {name}!")

get_user_name()

# Encryption key handling
def Mkey():
    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            return file.read()
    else:
        keym = Fernet.generate_key()
        with open(key_file, "wb") as Key_file:
            Key_file.write(keym)
        return keym

def store_encrypted_master_password(master_password):
    encrypted_password = fer.encrypt(master_password.encode()).decode()
    with open(encrypted_master_file, "w") as file:
        file.write(encrypted_password)

def verify_master_password(master_password):
    with open(encrypted_master_file, "r") as file:
        encrypted_password = file.read()
    return master_password == fer.decrypt(encrypted_password.encode()).decode()

mkey = Mkey()
fer = Fernet(mkey)

# If the master password has not been set before, set it now
if not os.path.exists(encrypted_master_file):
    Master_pwd = input("Please set your Master Password: ")
    store_encrypted_master_password(Master_pwd)
else:
    Master_pwd = input("Please insert your Master Password: ")
    if not verify_master_password(Master_pwd):
        print("Incorrect Master Password. Exiting...")
        exit()

def view():
    # Ensure the file exists and is not empty
    if os.path.exists(filepwd) and os.path.getsize(filepwd) > 0:
        with open(filepwd, 'r') as file:
            for line in file.readlines():
                data = line.rstrip()
                Cat, User, Passw = data.split("|")
                print(f">> Category: {fer.decrypt(Cat.encode()).decode()} | User: {fer.decrypt(User.encode()).decode()} | Password: {fer.decrypt(Passw.encode()).decode()}\n")
    else:
        print("No data available to view.")

def add():
    Acc = input("Please Insert Your Account Name You Want To Add: ")
    pwd = input("Please Insert The Password: ")
    Category = input("What Is The Account Use For: ")

    with open(filepwd, 'a') as file:
        file.write(f"{fer.encrypt(Category.encode()).decode()}|{fer.encrypt(Acc.encode()).decode()}|{fer.encrypt(pwd.encode()).decode()}\n")

while True:
    mode = input("Please insert the mode From (Add or View) or q for Quit: ").lower()

    if mode == "q" or mode == "quit":
        break
    elif mode == "add" or mode == "a":
        add()
    elif mode == "view" or mode == "v":
        view()
    else:
        print("Invalid Mode.")
