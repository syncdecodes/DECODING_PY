# Methods that dont use the self parameters (work at class level)

class Student:
    def __init__(self, name, marks):
         self.name = name
         self.marks = marks
    
    @staticmethod # decorator
    def hello():
         return "hello" # This method does not take 'self' because it's a static method

s1 = Student("sia", 85)
print(s1.hello(),s1.name, "your m1 marks =", s1.marks)

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it