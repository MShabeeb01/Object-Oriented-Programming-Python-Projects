#Employee Management System 

import json

# Base Class : Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n---Employee Details---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.1

    def to_dict(self):
        return {
            "type": "Employee",
            "name": self.name,
            "emp_id": self.emp_id,
            "salary": self.salary
        }


# Derived Class : Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.2

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Manager"
        data["department"] = self.department
        return data


# Derived Class : Developer
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.15

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Developer"
        data["programming_language"] = self.programming_language
        return data


# JSON Handling Functions
FILENAME = "employee.json"
employees = []


def load_employees():
    """Load employees from JSON file."""
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            for emp in data:
                if emp["type"] == "Employee":
                    employees.append(Employee(emp["name"], emp["emp_id"], emp["salary"]))
                elif emp["type"] == "Manager":
                    employees.append(Manager(emp["name"], emp["emp_id"], emp["salary"], emp["department"]))
                elif emp["type"] == "Developer":
                    employees.append(Developer(emp["name"], emp["emp_id"], emp["salary"], emp["programming_language"]))
    except FileNotFoundError:
        pass


def save_employees():
    """Save employees to JSON file."""
    with open(FILENAME, "w") as file:
        json.dump([emp.to_dict() for emp in employees], file, indent=4)



# Core Functions
def add_employee():
    print("\n---Choose Employee Type---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter your choice: ").strip())

    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: "))

    if choice == 1:
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        department = input("Enter Department: ").strip()
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == 3:
        programming_language = input("Enter Programming Language: ").strip()
        employees.append(Developer(name, emp_id, salary, programming_language))
    else:
        print("Invalid Choice")
        return

    save_employees()


def display_all_employees():
    if not employees:
        print("\nNo employees to display.")
        return

    print("\n--- All Employees ---")
    for employee in employees:
        employee.display_info()
        print(f"Bonus: {employee.calculate_bonus()}")


def search_employee_by_id():
    emp_id = input("\nEnter Employee ID to search: ").strip()
    for emp in employees:
        if emp.emp_id == emp_id:
            print("\n--- Employee Found ---")
            emp.display_info()
            print(f"Bonus: {emp.calculate_bonus()}")
            return
    print("\nEmployee not found.")


def search_employee_by_name():
    name = input("\nEnter Employee Name to search: ").strip().lower()
    found = False
    for emp in employees:
        if emp.name.lower() == name:  # case insensitive search
            print("\n--- Employee Found ---")
            emp.display_info()
            print(f"Bonus: {emp.calculate_bonus()}")
            found = True
    if not found:
        print("\nEmployee not found.")


# Main Program
load_employees()

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Search Employee by Name")
    print("5. Exit")
    choice = int(input("Enter your Choice: ").strip())

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        search_employee_by_id()
    elif choice == 4:
        search_employee_by_name()
    elif choice == 5:
        print("Exiting the program. Data saved.")
        break
    else:
        print("Invalid Choice")
