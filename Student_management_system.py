students = [] # Student Management System


# -------------------------------
# Grade Calculation Function
# -------------------------------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# -------------------------------
# CGPA Calculation Function
# -------------------------------
def calculate_cgpa(percentage):
    return round(percentage / 9.5, 2)


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    try:
        name = input("Enter Student Name: ")
        dob = input("Enter DOB (DD/MM/YYYY): ")

        num_subjects = int(input("Enter Number of Subjects: "))

        subjects = {}
        total_marks = 0

        print("\nEnter Subject Wise Marks:")

        for i in range(num_subjects):
            subject = input(f"Subject {i+1} Name: ")
            marks = float(input(f"Marks in {subject}: "))
            subjects[subject] = marks
            total_marks += marks

        max_marks = num_subjects * 100
        percentage = (total_marks / max_marks) * 100

        grade = calculate_grade(percentage)
        cgpa = calculate_cgpa(percentage)

        total_classes = int(input("Enter Total Classes: "))
        attended_classes = int(input("Enter Attended Classes: "))

        attendance = (attended_classes / total_classes) * 100

        result = "PASS"

        for mark in subjects.values():
            if mark < 40:
                result = "FAIL"
                break

        student = {
            "name": name,
            "dob": dob,
            "subjects": subjects,
            "total_marks": total_marks,
            "percentage": percentage,
            "grade": grade,
            "cgpa": cgpa,
            "attendance": attendance,
            "result": result
        }

        students.append(student)

        print("\nStudent Added Successfully!\n")

    except ValueError:
        print("Invalid Input!\n")


# -------------------------------
# Display Students
# -------------------------------
def display_students():

    if not students:
        print("\nNo Records Found!\n")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:

        print("\n--------------------------------")
        print("Name:", student["name"])
        print("DOB:", student["dob"])

        print("\nSubject Wise Marks:")

        for sub, mark in student["subjects"].items():
            print(f"{sub}: {mark}")

        print("Total Marks:", student["total_marks"])
        print(f"Percentage: {student['percentage']:.2f}%")
        print("Grade:", student["grade"])
        print("CGPA:", student["cgpa"])
        print(f"Attendance: {student['attendance']:.2f}%")
        print("Result:", student["result"])

        if student["attendance"] < 75:
            print("WARNING: Low Attendance!")


# -------------------------------
# Search Student
# -------------------------------
def search_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nStudent Found")
            print("--------------------")

            print("Name:", student["name"])
            print("Grade:", student["grade"])
            print("CGPA:", student["cgpa"])
            print("Result:", student["result"])

            return

    print("Student Not Found!")


# -------------------------------
# Remove Student
# -------------------------------
def remove_student():

    name = input("Enter Student Name to Remove: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student Removed Successfully!")
            return

    print("Student Not Found!")


# -------------------------------
# Generate Progress Card
# -------------------------------
def generate_progress_card():

    name = input("Enter Student Name: ")

    for student in students:

        if student["name"].lower() == name.lower():

            print("\n========== PROGRESS CARD ==========")

            print("Name:", student["name"])
            print("DOB:", student["dob"])

            print("\nSubjects:")

            for sub, mark in student["subjects"].items():
                print(f"{sub}: {mark}")

            print("\nTotal Marks:", student["total_marks"])
            print(f"Percentage: {student['percentage']:.2f}%")
            print("Grade:", student["grade"])
            print("CGPA:", student["cgpa"])
            print("Attendance:", round(student["attendance"], 2), "%")
            print("Result:", student["result"])

            return

    print("Student Not Found!")


# -------------------------------
# Rank List
# -------------------------------
def generate_rank_list():

    if not students:
        print("No Records Available!")
        return

    ranked = sorted(
        students,
        key=lambda x: x["percentage"],
        reverse=True
    )

    print("\n========== RANK LIST ==========")

    rank = 1

    for student in ranked:

        print(
            f"Rank {rank} : "
            f"{student['name']} "
            f"({student['percentage']:.2f}%)"
        )

        rank += 1


# -------------------------------
# Topper Identification
# -------------------------------
def identify_topper():

    if not students:
        print("No Records Available!")
        return

    topper = max(
        students,
        key=lambda x: x["percentage"]
    )

    print("\n========== CLASS TOPPER ==========")
    print("Name:", topper["name"])
    print(f"Percentage: {topper['percentage']:.2f}%")
    print("Grade:", topper["grade"])
    print("CGPA:", topper["cgpa"])


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Generate Progress Card")
    print("6. Generate Rank List")
    print("7. Identify Topper")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        generate_progress_card()

    elif choice == "6":
        generate_rank_list()

    elif choice == "7":
        identify_topper()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
