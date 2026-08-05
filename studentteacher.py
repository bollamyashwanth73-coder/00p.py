# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived Class - Student
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print("Roll Number:", self.roll_no)


# Derived Class - Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print("Subject:", self.subject)


# Main Program
student = Student("Yashwanth", 20, 101)
teacher = Teacher("Ramesh", 35, "Python")

print("Student Details")
student.display()

print("\nTeacher Details")
teacher.display()