students = []
while True:
    name = input("Enter student name:")
    marks = int(input("Enter student marks:"))
    student = {
        "name": name,
        "marks":marks
    }
    students.append(student)
    choice = input("Add another student? (yes/no):")
    if choice.lower() != "yes":
        break

print("\n--- Student List ---")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("----------------")
