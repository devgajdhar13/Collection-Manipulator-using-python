student_ids = []
students = {}
subjects_all = set()

print("Welcome to the Student Data Organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nEnter student details:")

        try:
            sid = int(input("Student ID: "))
        except ValueError:
            print("Invalid Student ID!")
            continue

        if sid in students:
            print("Student ID already exists!")
            continue

        name = input("Name: ")

        try:
            age = int(input("Age: "))
        except ValueError:
            print("Invalid Age!")
            continue

        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        sub_input = input("Subjects (comma-separated): ")

        subject_set = set()

        for sub in sub_input.split(","):
            if sub.strip():
                subject_set.add(sub.strip().title())

        id_dob = (sid, dob)

        students[sid] = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subject_set
        }

        student_ids.append(sid)
        subjects_all.update(subject_set)

        print("\nStudent added successfully!")

    elif choice == "2":

        print("\n--- Display All Students ---")

        if not students:
            print("No student records found.")

        else:
            for sid in student_ids:

                student = students[sid]

                print(
                    "Student ID: {} | Name: {} | Age: {} | Grade: {} | Subjects: {}".format(
                        sid,
                        student["name"],
                        student["age"],
                        student["grade"],
                        ", ".join(sorted(student["subjects"]))
                    )
                )

    elif choice == "3":

        try:
            sid = int(input("Enter Student ID to update: "))
        except ValueError:
            print("Invalid Student ID!")
            continue

        if sid not in students:
            print("Student not found!")
            continue

        student = students[sid]

        print("\nLeave blank to keep old value.")

        name = input("New Name ({}): ".format(student["name"]))
        if name:
            student["name"] = name

        age = input("New Age ({}): ".format(student["age"]))
        if age:
            try:
                student["age"] = int(age)
            except ValueError:
                print("Invalid Age!")

        grade = input("New Grade ({}): ".format(student["grade"]))
        if grade:
            student["grade"] = grade

        subs = input("New Subjects (comma-separated): ")

        if subs:
            student["subjects"] = set()

            for sub in subs.split(","):
                if sub.strip():
                    student["subjects"].add(sub.strip().title())

            subjects_all.clear()

            for s in students.values():
                subjects_all.update(s["subjects"])

        print("Student information updated successfully!")

    elif choice == "4":

        try:
            sid = int(input("Enter Student ID to delete: "))
        except ValueError:
            print("Invalid Student ID!")
            continue

        if sid not in students:
            print("Student not found!")
            continue

        del students[sid]
        student_ids.remove(sid)

        subjects_all.clear()

        for s in students.values():
            subjects_all.update(s["subjects"])

        print("Student deleted successfully!")

    elif choice == "5":

        print("\n--- Subjects Offered ---")

        if subjects_all:
            print(", ".join(sorted(subjects_all)))
        else:
            print("No subjects available.")

    elif choice == "6":

        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
