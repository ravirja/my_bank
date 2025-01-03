# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:25:36 2024

@author: Ravi
"""
import hashlib
import getpass

class BankSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store user credentials

    def hash_password(self, password):
        """Hash a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, username, password):
        """Add a new user to the system."""
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = self.hash_password(password)
            print(f"User {username} added successfully!")

    def authenticate_user(self, username, password):
        """Authenticate a user."""
        hashed_password = self.hash_password(password)
        if username in self.users and self.users[username] == hashed_password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

def main():
    bank_system = BankSystem()
    
    while True:
        print("\nBank System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = getpass.getpass("Enter a password: ")
            bank_system.add_user(username, password)

        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            bank_system.authenticate_user(username, password)

        elif choice == "3":
            print("Exiting the banking system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
