num_students = int(input())

students = {}

for _ in range(num_students):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

filtered_students = {name: sum(grades) / len(grades) for name, grades in students.items() if sum(grades) / len(grades) >= 4.50}

# Print the final dictionary with students and their average grades
for name, average_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {average_grade:.2f}")
