def char_in_range(ch1, ch2):
    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=' ')


char1 = input()
char2 = input()
char_in_range(char1, char2)