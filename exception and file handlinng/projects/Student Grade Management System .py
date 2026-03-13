#.Student Grade Management System Program that records, updates, and deletes student grades. 
#Handle exceptions like invalid student ID, empty grade inputs, and type mismatches. 
class StudentGradeManagementSystem:
    def __init__(self):
        self.students = {}

    def record_student(self, student_id, name):
        if not student_id:
            raise ValueError("Student ID cannot be empty")
        if not name:
            raise ValueError("Student name cannot be empty")
        self.students[student_id] = name
    def update_grade(self, student_id, grade):
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        if not grade:
            raise ValueError("Grade cannot be empty")
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        self.students[student_id] = grade
    def delete_student_grade(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        del self.students[student_id]
# Example usage
if __name__ == "__main__":
    system = StudentGradeManagementSystem()
    try:
        print("Recording student...")
        s1 = input("Enter student ID: ")
        n1 = input("Enter student name: ")
        system.record_student(s1, n1)
        print("Updating grade...")
        g1 = float(input("Enter grade for student ID {}: ".format(s1)))
        system.update_grade(s1, g1)
        print("Student grade updated successfully.")
        print("Student records:")
        for student_id, grade in system.students.items():
            print(f"ID: {student_id}, Name: {system.students[student_id]}, Grade: {grade}")
    except (ValueError, TypeError) as e:
        print(e)


