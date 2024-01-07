number_of_lines = int(input())
capacity = 0

for _ in range(number_of_lines):
    liters_in_water = int(input())

    if liters_in_water + capacity <= 255:
        capacity += liters_in_water
        continue

    print("Insufficient capacity!")

print(capacity)