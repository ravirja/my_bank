import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def open_account(username, account_number, initial_balance=0):
    users = load_users()
    if account_number in users[username]["accounts"]:
        print("Account number already exists. Please choose a different account number.")
    else:
        users[username]["accounts"][account_number] = initial_balance
        save_users(users)
        print(f"Account {account_number} opened for {username} with balance ${initial_balance}.")

def deposit(username, account_number, amount):
    users = load_users()
    if account_number in users[username]["accounts"]:
        users[username]["accounts"][account_number] += amount
        save_users(users)
        print(f"Deposited: ${amount}. New balance: ${users[username]['accounts'][account_number]}")
    else:
        print("Account number not found.")

def withdraw(username, account_number, amount):
    users = load_users()
    if account_number in users[username]["accounts"]:
        if amount <= users[username]["accounts"][account_number]:
            users[username]["accounts"][account_number] -= amount
            save_users(users)
            print(f"Withdrawn: ${amount}. New balance: ${users[username]['accounts'][account_number]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account number not found.")

def check_balance(username, account_number):
    users = load_users()
    if account_number in users[username]["accounts"]:
        print(f"Account balance: ${users[username]['accounts'][account_number]}")
    else:
        print("Account number not found.")
