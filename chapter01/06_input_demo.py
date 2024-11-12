name = input("Please enter your name: ")

is_student = input("Are you a student? (yeas/no): ").lower() == "yes"

print(f"name: {name}")
print(f"Is student: {is_student}")

if is_student:
    print("You are a student")
else: 
    print("You are not a student")
    
