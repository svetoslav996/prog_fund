import math

num_of_people = int(input())
capacity_of_elevator = int(input())
courses = num_of_people / capacity_of_elevator
print(math.ceil(courses))
