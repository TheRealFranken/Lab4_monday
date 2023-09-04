import datetime

class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id} {self.name} {self.age} {self.salary}"

class EmployeeSorter:
    def __init__(self, employees):
        self.employees = employees

    def sort(self, sorting_parameter):
        if sorting_parameter == 1:
            return sorted(self.employees, key=lambda emp: emp.age)
        elif sorting_parameter == 2:
            return sorted(self.employees, key=lambda emp: emp.name)
        elif sorting_parameter == 3:
            return sorted(self.employees, key=lambda emp: emp.salary)
        else:
            return self.employees

def print_employee_table(employees):
    print("Employee Table")
    print("Employee ID Name Age Salary (PM)")
    for emp in employees:
        print(emp)

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print_employee_table(employees)

    sorting_parameter = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))

    sorter = EmployeeSorter(employees)
    sorted_employees = sorter.sort(sorting_parameter)

    print("\nSorted Employee Table")
    print_employee_table(sorted_employees)

    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nExecuted by: Bir Fateh Singh (e22cseu1242)")
    print(f"Date and Time of Execution: {formatted_date}")

if __name__ == "__main__":
    main()
