import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Change if different
    password="Praveen@@8",       # Set your MySQL password
    database="employee_db"
)

cursor = conn.cursor()

# Add Employee
def add_employee(name, age, position, salary):
    query = "INSERT INTO employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, position, salary))
    conn.commit()
    print(" Employee added successfully.")

# Remove Employee
def remove_employee(emp_id):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
        conn.commit()
        print(" Employee removed.")
    else:
        print(" Employee not found.")

# Promote Employee
def promote_employee(emp_id, new_salary):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    if cursor.fetchone():
        cursor.execute("UPDATE employees SET salary = %s WHERE id = %s", (new_salary, emp_id))
        conn.commit()
        print(" Employee promoted.")
    else:
        print(" Employee not found.")

# Display Employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    print("\n--- Employee List ---")
    print("ID | Name | Age | Position | Salary")
    print("-" * 40)
    for emp in employees:
        print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4]}")
    print("-" * 40)

# Menu Loop
def menu():
    while True:
        print("""
-------- Employee Management System --------
1. Add Employee
2. Remove Employee
3. Promote Employee
4. Display All Employees
5. Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            add_employee(name, age, position, salary)

        elif choice == '2':
            emp_id = int(input("Enter Employee ID to remove: "))
            remove_employee(emp_id)

        elif choice == '3':
            emp_id = int(input("Enter Employee ID to promote: "))
            new_salary = float(input("Enter new salary: "))
            promote_employee(emp_id, new_salary)

        elif choice == '4':
            display_employees()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print(" Invalid choice. Try again.")

# Run the program
menu()

# Close connection
cursor.close()
conn.close()
