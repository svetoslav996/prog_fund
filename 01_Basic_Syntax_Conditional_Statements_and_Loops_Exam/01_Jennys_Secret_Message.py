def greet_user(name):
    if name.lower() == 'johnny':
        print("Hello, my love!")
    else:
        print(f"Hello, {name}!")

# Get user input for the name
user_name = input()

# Call the greet_user function with the user's name
greet_user(user_name)