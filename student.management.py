
students = []

# Enter multiple students
while True:
    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty!")
        name = input("Enter student name: ").strip()

    # Validate marks
    while True:
        marks = input("Enter student marks (0-100): ")

        if marks.isdigit() and 0 <= int(marks) <= 100:
            marks = int(marks)
            break
        else:
            print("Invalid marks! Enter 0 to 100.")

    # Store student details
    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    # Save details to file
    with open("student.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    print("Student details saved!")

    choice = input("Add another student? (yes/no): ")

    if choice.lower() != "yes":
        break

# Display student list with grades
print("\n--- Student List ---")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])

    if student["marks"] >= 90:
        print("Grade: A")
    elif student["marks"] >= 75:
        print("Grade: B")
    elif student["marks"] >= 60:
        print("Grade: C")
    elif student["marks"] >= 35:
        print("Grade: D")
    else:
        print("Grade: Fail")

    print("--------------------")

# Search for a student
search_name = input("Enter student name to search: ").strip()
found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent found!")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        found = True

if not found:
    print("Student not found!")

# Display saved records from file
print("\n--- All Saved Student Details ---")

with open("student.txt", "r") as file:
    print(file.read())

