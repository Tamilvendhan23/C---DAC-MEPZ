def add_student(students: list, student_id: str, name: str, city: str, marks: int) -> None:
    """
    Adds a student record.
    Raise ValueError if marks are not between 0 and 100.
    """

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    # check duplicate ID
    for student in students:
        if student["id"] == student_id:
            raise ValueError("Student ID already exists.")

    student = {
        "id": student_id,
        "name": name,
        "city": city,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def get_high_scorers(students: list, cutoff: int) -> list:
    """
    Returns students whose marks are greater than or equal to cutoff.
    """
    return [student for student in students if student["marks"] >= cutoff]


def remove_student(students: list, student_id: str) -> None:
    """
    Removes student by ID.
    Raise ValueError if student does not exist.
    """

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student removed successfully.")
            return

    raise ValueError("Student ID not found.")


def save_students_to_file(file_path: str, students: list) -> None:
    """
    Saves student records to a text file.
    Must use context manager.
    """

    with open(file_path, "w") as file:
        for student in students:
            line = f"{student['id']},{student['name']},{student['city']},{student['marks']}\n"
            file.write(line)

    print("Students saved to file successfully.")

def main():

    students = []

    while True:
        try:
            print("\n===== Student Record Management =====")
            print("1. Add Student")
            print("2. View High Scorers")
            print("3. Remove Student")
            print("4. Save to File")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            # Add Student
            if choice == 1:
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                city = input("Enter City: ")
                marks = int(input("Enter Marks: "))

                add_student(students, student_id, name, city, marks)

            # View High Scorers
            elif choice == 2:
                cutoff = int(input("Enter cutoff marks: "))
                high_scorers = get_high_scorers(students, cutoff)

                if not high_scorers:
                    print("No students found above cutoff.")
                else:
                    print("\nHigh Scorers:")
                    for s in high_scorers:
                        print(f"{s['id']} - {s['name']} - {s['city']} - {s['marks']}")

            # Remove Student
            elif choice == 3:
                student_id = input("Enter Student ID to remove: ")
                remove_student(students, student_id)

            # Save to File
            elif choice == 4:
                file_path = input("Enter file path (example: students.txt): ")
                save_students_to_file(file_path, students)

            # Exit
            elif choice == 5:
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please select 1-5.")
        except:
            print("error try again")

main()