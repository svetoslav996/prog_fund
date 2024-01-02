n = int(input())

for _ in range(n):
    current_string = input()

    if all(char not in current_string for char in [',', '.', '_']):
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
