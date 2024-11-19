students = ("Alice", "Bob", "Charlie")

print(type(students))

# Iterate
for index, student in enumerate(students):
    print(f"{index} : {student}")

# Enhanced for
for student in students:
    print(student)
    
first_student, second_student, third_student = students

print(f"First Student: {first_student}")
print(f"Second Student: {second_student}")
print(f"Third Student: {third_student}")

students = list(students)
students[0] = "Jim"
students = tuple(students)

print(students)