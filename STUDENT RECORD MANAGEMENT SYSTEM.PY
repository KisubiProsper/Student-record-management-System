import sqlite3
connection = sqlite3.connect("student_records.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL)''')
def add_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    connection.commit()

    print("Student added successfully!")
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for record in records:
        print(record)
def update_student(student_id, name, age, course):
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    connection.commit()
    print("Student record updated successfully!")
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()
    print("Student record deleted successfully!")
def search_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    record = cursor.fetchone()
    if record:
        print(record)
    else:
        print("Student not found!")
while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search for a Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        add_student(name, age, course)
    elif choice == "2":
        view_students()
    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        update_student(student_id, name, age, course)
    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)
    elif choice == "5":
        student_id = int(input("Enter student ID to search: "))
        search_student(student_id)
    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

connection.close()
