
name = input("Enter student name: ")

while True:
    marks = input("Enter student marks: ")

    if marks.isdigit() and 0 <= int(marks) <= 100:
        break
    else:
        print("Invalid marks! Enter marks from 0 to 100.")

with open("student.txt", "a") as file:
    file.write(f"Name: {name}, Marks: {marks}\n")

print("Student details saved!")
with open("student.txt", "r") as file:
    print("\n--- Saved Student Details----")
    print(file.read())