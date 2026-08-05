from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Main Program
full = FullTimeEmployee(50000)
part = PartTimeEmployee(80, 300)

print("Full Time Employee Salary:", full.calculate_salary())
print("Part Time Employee Salary:", part.calculate_salary())