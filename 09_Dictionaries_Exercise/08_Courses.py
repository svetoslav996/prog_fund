courses = {}

while True:
    input_line = input()
    if input_line == "end":
        break

    course_name, student_name = input_line.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

# Print the courses and registered students
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
