# Base Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


# Derived Class - Manager
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


# Derived Class - Developer
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


# Main Program
manager = Manager(101, "Ramesh", 80000, "HR")
developer = Developer(102, "Yashwanth", 60000, "Python")

print("Manager Details")
manager.display()

print("\nDeveloper Details")
developer.display()
