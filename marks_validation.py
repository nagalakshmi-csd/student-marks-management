
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            print("Valid marks!")
            break
        else:
            print("Invalid marks! Enter 0 to 100.")

    except ValueError:
        print("Numbers only! Try again.")


