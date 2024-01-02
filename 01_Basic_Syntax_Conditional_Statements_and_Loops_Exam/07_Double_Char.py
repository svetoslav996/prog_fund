while True:
    current_string = input()

    if current_string == "End":
        break

    if current_string != "SoftUni":
        doubled_string = ''.join(char * 2 for char in current_string)
        print(doubled_string)
