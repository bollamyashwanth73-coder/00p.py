class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        return self.emp_id == other.emp_id

emp1 = Employee(101, "Kiran")
emp2 = Employee(101, "Ravi")

if emp1 == emp2:
    print("Employees are equal")
else:
    print("Employees are not equal")
