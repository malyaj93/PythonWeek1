# Create a login page backend to ask users to enter the username and password.
# Make sure to ask for a Re-Type Password and if the password is incorrect give a chance to enter it again.
# User should only get 3 tries to re-enter the password.

def login_system():
    user_database = {}

    username = input("Enter your username: ")

    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            user_database[username] = password
            print("Registration successful!\n")
            break
        else:
            print("Passwords does not match. Try again.")

    attempt_count = 0
    while attempt_count < 3:
        login_username = input("Enter your username: ")
        login_password = input("Enter your password: ")

        if login_username in user_database and user_database[login_username] == login_password:
            print("Login successful!")
            return
        else:
            print("Incorrect username or password. Try again.")
            attempt_count += 1

        if attempt_count == 3:
            print("Too many failed attempts. Try again later.")


login_system()