#Define a function that accepts roll number and returns whether the student is present or 
#absent.
def check_attendance(roll_number):
    # For demonstration, let's assume students with even roll numbers are present and odd roll numbers are absent
    if roll_number in [1 to 100]:  # Assuming roll numbers are between 1 and 100
        if roll_number % 2 == 0:
            return "Present"
        else:
            return "Absent"
    else:
        return "Invalid roll number. Please enter a number between 1 and 100."
roll_number_input = int(input("Enter the roll number of the student: "))
attendance_status = check_attendance(roll_number_input)
print(f"Student with roll number {roll_number_input} is {attendance_status}.")

