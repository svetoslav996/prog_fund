def gift_planner(gifts, commands):
    gifts_list = gifts.split()

    for command in commands:
        tokens = command.split()
        action = tokens[0]

        if action == "OutOfStock":
            gift_to_remove = tokens[1]
            for i in range(len(gifts_list)):
                if gifts_list[i] == gift_to_remove:
                    gifts_list[i] = "None"

        elif action == "Required":
            gift_to_replace = tokens[1]
            index = int(tokens[2])
            if 0 <= index < len(gifts_list):
                gifts_list[index] = gift_to_replace

        elif action == "JustInCase":
            gifts_list[-1] = tokens[1]

        elif action == "No":
            break

    final_gifts = [gift for gift in gifts_list if gift != "None"]
    print(" ".join(final_gifts))

# Example usage:
gifts_input = input()
commands_input = []
print()
while True:
    command = input()
    if command == "No Money":
        break
    commands_input.append(command)

gift_planner(gifts_input, commands_input)
