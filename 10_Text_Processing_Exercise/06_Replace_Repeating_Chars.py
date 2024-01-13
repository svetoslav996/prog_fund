def replace_duplicate_letters(input_string):
    result = ''
    prev_char = ''

    for char in input_string:
        if char != prev_char:
            result += char
        prev_char = char

    return result


def main():
    input_string = input()
    modified_string = replace_duplicate_letters(input_string)
    print(modified_string)


if __name__ == "__main__":
    main()
