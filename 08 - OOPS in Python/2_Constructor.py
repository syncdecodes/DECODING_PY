# Constructor -:
# All clases have a function called __init__(), which is always executed when the object is being initiated
# jese hi hum class ko use kar ke ek new object bnate hai toh automatically __init__() fn call ho jata hai.

# creating class
class Student:
    def __init__(self):
        print("Happy coding")

# creating object (instance of class)
s1 = Student()

class Employee:

    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, salary):
        self.salary = salary
        print("Employee data")

e1 = Employee("40000")
print("emp1 salary =", e1.salary)

e2 = Employee("50000")
print("emp2 salary =", e2.salary)
