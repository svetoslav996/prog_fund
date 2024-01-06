# Function to calculate the sum each beggar brings home
def beggars_sum(input_string, num_beggars):
    # Convert the input string to a list of integers
    nums = list(map(int, input_string.split(", ")))

    # Initialize a list to store the sum each beggar brings home
    beggars_sums = [0] * num_beggars

    # Distribute the amounts among beggars
    for i in range(len(nums)):
        beggar_index = i % num_beggars
        beggars_sums[beggar_index] += nums[i]

    # Print the result
    print(beggars_sums)

# Example usage:
input_string = input()
num_beggars = int(input())

beggars_sum(input_string, num_beggars)
