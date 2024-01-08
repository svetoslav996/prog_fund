def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


a, b, c = int(input()), int(input()), int(input())
number_sum = sum_numbers(a, b)
result = subtract(number_sum, c)
print(result)