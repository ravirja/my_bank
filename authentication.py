# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:46:54 2024

@author: Ravi
"""

import hashlib
import getpass
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def register(username, password):
    users = load_users()
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = {
            "password": hash_password(password),
            "accounts": {}
        }
        save_users(users)
        print(f"User {username} registered successfully!")

def authenticate(username, password):
    users = load_users()
    if username in users and users[username]["password"] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
