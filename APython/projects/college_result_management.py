#5. College Result Management Teachers enter marks, calculate GPA
def calculate_gpa(marks):
    if marks >= 90:
        return 4.0
    elif marks >= 80:
        return 3.0
    elif marks >= 70:
        return 2.0
    elif marks >= 60:
        return 1.0
    else:
        return 0.0
marks = float(input("Enter marks: "))
gpa = calculate_gpa(marks)
print(f"GPA: {gpa}")
