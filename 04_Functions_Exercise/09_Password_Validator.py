def is_valid_password(password):
    # List to store error messages
    error_messages = []

    # Rule 1: Check the length of the password
    if not (6 <= len(password) <= 10):
        error_messages.append("Password must be between 6 and 10 characters")

    # Rule 2: Check if the password consists only of letters and digits
    if not password.isalnum():
        error_messages.append("Password must consist only of letters and digits")

    # Rule 3: Check if the password has at least 2 digits
    if sum(c.isdigit() for c in password) < 2:
        error_messages.append("Password must have at least 2 digits")

    # If there are any error messages, print them
    if error_messages:
        for message in error_messages:
            print(message)
    else:
        print("Password is valid")

# Example usage:
password = input()
is_valid_password(password)
