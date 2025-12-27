class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_average(self):
        sum = 0
        for num in self.marks:
            sum += num
        print(self.name, "average marks =", sum/3)


s1 = Student("sia", [70, 80, 90])
s1.get_average()

# we can also change the attributes directly -:
s1.name = "kiku"
s1.get_average()