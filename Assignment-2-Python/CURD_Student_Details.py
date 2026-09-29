
students = {} #Empty dictionary

while True:
    print("\nStudent's Grade Management")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all students grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(name + "'s grade added successfully")

    elif choice == "2":
        name = input("Enter student name to update: ")

        if name in students:
            new_grade = input("Enter new grade: ")
            students[name] = new_grade
            print(name + "'s grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        if students.__len__() > 0:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(name, grade)
        else:
            print("No student records available.")

    elif choice == "4":
        print("Exiting program...")
        break                         #To exit the while loop and shouldn't go infinite

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")