students = {
    'Alice':[85, 92, 78],
    'Bob':[79, 95, 88],
    'Charlie':[68, 72, 80],
    'Diana':[95, 98, 100],
    'Eve':[50, 68, 58]
}

def main():
    threshold = int(input("Please insert a threshold (int): "))
    
    average_grades ={student: round(sum(grades) / len(grades)) for student, grades in students.items()
                     if round(sum(grades) / len(grades)) > threshold}
    print(average_grades)
    
    for student, grades in average_grades.items():
        print(f"{student} : {grades}")

if __name__ == "__main__":
    main()