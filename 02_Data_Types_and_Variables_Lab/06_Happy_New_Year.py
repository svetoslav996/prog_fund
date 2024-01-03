def is_happy_year(year):
    year_str = str(year)
    return len(set(year_str)) == len(year_str)

def find_next_happy_year(current_year):
    next_year = current_year + 1
    while not is_happy_year(next_year):
        next_year += 1
    return next_year

current_year = int(input())
next_happy_year = find_next_happy_year(current_year)

print(f"{next_happy_year}")
