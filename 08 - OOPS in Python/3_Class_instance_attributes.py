class Student:
    college = "xyz"
    name = "abc" # class attribute

    def __init__(self, name, marks):
        # object attribute
        self.name = name # object attribute > class attr
        self.marks = marks

s1 = Student("arjun", 56)
s2 = Student()
