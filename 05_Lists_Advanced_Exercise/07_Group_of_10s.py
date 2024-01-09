def print_sorted_groups(numbers_str):
    # Convert the input string of numbers to a list of integers
    numbers = [int(num) for num in numbers_str.split(", ")]

    # Initialize variables
    group_boundary = 10
    current_group = 0

    # Loop until the numbers list is empty
    while numbers:
        # Filter numbers less than or equal to the current group boundary
        current_group_numbers = [num for num in numbers if num <= group_boundary]

        # Remove the filtered numbers from the original list
        numbers = [num for num in numbers if num > group_boundary]

        # Print the current group
        print(f"Group of {group_boundary}'s: {current_group_numbers}")

        # Update the group boundary for the next iteration
        group_boundary += 10
        current_group += 1

# Example usage
numbers_input = input()
print_sorted_groups(numbers_input)
