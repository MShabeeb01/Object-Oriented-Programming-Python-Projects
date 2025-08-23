import json
import os

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username   # Public
        self._email = email        # Protected
        self.__password = None     # Private (initialize as None)
        self.set_password(password)

    # Getter for email
    def get_email(self):
        return self._email

    # Setter for email
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email updated successfully")
        else:
            print("Invalid email format")

    # Setter for password
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Password must be at least 6 characters long.")
        else:
            self.__password = new_password
            print("Password set successfully.")

    # Convert object to dictionary for JSON
    def to_dict(self):
        return {
            "username": self.username,
            "email": self._email,
            "password": self.__password
        }

    # Create object from dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["email"], data["password"])

    # Display profile (without showing password)
    def display_profile(self):
        print("\n---User Profile---")
        print(f"Username: {self.username}")
        print(f"Email: {self._email}")


# JSON Handling
FILENAME = "profiles.json"

def load_users():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        data = json.load(f)
        return [UserProfile.from_dict(user) for user in data]

def save_users():
    with open(FILENAME, "w") as f:
        json.dump([user.to_dict() for user in users], f, indent=4)


# Main Program
users = load_users()  # Load existing users at start

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = UserProfile(username, email, password)
    users.append(user)
    save_users()  # Save immediately
    print("User created successfully")

def view_profile():
    if not users:
        print("No users found")
    else:
        for user in users:
            user.display_profile()

def update_email():
    username = input("Enter username to update email: ") 
    for user in users:
        if user.username == username:
            new_email = input("Enter new email: ")
            user.set_email(new_email)
            save_users()  # Save after update
            return
    print("User not found.")


# Main Menu
while True:
    print("\n--- Secure User Profile App ---")
    print("1. Create user")
    print("2. View all profiles")
    print("3. Update email")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_user()
    elif choice == "2":
        view_profile()
    elif choice == "3":
        update_email()
    elif choice == "4":
        save_users()  # Final save before exiting
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid choice.")
