def is_perfect_number(number):
    # Ensure the number is positive
    if number <= 0:
        print("It's not so perfect.")
        return

    # Find the sum of proper divisors
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)

    # Check if the number is perfect
    if divisors_sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

# Example usage:
number = int(input())
is_perfect_number(number)
