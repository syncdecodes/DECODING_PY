# Methods are functions defined inside a class and called on objects.

# creating class
class Student:

    # parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    # creating method
    def hello(self):
        print("hello", self.name)
    
    # creating method
    def get_marks(self):
        print(self.name, "marks =", self.marks)

# creating object (instance)
s1 = Student("arjun", 78)
s1.hello()
s1.get_marks()
