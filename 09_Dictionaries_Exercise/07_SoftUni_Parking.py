def parking_system(commands):
    registered_users = {}

    for command in commands:
        tokens = command.split()
        action = tokens[0]
        username = tokens[1]

        if action == "register":
            license_plate_number = tokens[2]

            if username in registered_users:
                print(f"ERROR: already registered with plate number {registered_users[username]}")
            else:
                registered_users[username] = license_plate_number
                print(f"{username} registered {license_plate_number} successfully")
        elif action == "unregister":
            if username not in registered_users:
                print(f"ERROR: user {username} not found")
            else:
                print(f"{username} unregistered successfully")
                del registered_users[username]

    for username, license_plate_number in registered_users.items():
        print(f"{username} => {license_plate_number}")


# Reading input
n = int(input())
commands = [input() for _ in range(n)]

# Execute the parking system
parking_system(commands)
