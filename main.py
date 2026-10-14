import sqlite3

# Create database connection
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_no TEXT UNIQUE NOT NULL,
                department TEXT,
                email TEXT)''')
conn.commit()

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    dept = input("Enter Department: ")
    email = input("Enter Email: ")
    try:
        cursor.execute("INSERT INTO students (name, roll_no, department, email) VALUES (?,?,?,?)",
                       (name, roll, dept, email))
        conn.commit()
        print("-> Student Added Successfully!\n")
    except sqlite3.IntegrityError:
        print("-> Error: Roll No already exists!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("-> No records found\n")
        return
    print("\n--- Student List ---")
    print("ID | Name | Roll No | Department | Email")
    for row in rows:
        print(row)
    print("--------------------\n")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()
    if cursor.rowcount > 0:
        print("-> Student Deleted Successfully!\n")
    else:
        print("-> Roll No not found!\n")

# Main Menu
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again\n")
