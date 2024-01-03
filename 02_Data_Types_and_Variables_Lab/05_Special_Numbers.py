n = int(input())
for num in range(1, n + 1):
    temp_num = num
    digit_sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        digit_sum += digit
        temp_num = temp_num // 10

    if digit_sum == 5 or digit_sum == 11 or digit_sum == 7:
        print(f"{num} -> {True}")
    else:
        print(f"{num} -> {False}")
