# # ques 1 -:
# # define a class to create a circle with radius r using the constructor
# # define an area() method
# # define a perimeter() method

# class Circle:
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         a = 3.14*(self.radius**2)
#         print(a)

#     def perimeter(self):
#         p = 2*3.14*self.radius
#         print(p)

# c1 = Circle(5)
# c1.area()
# c1.perimeter()

# # ques 2 -:

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.department = dept
#         self.salary = salary

#     def showDetails(self):
#         print(self.role, self.department, self.salary)

# emp1 = Employee("manager", "comp science", 40000)
# emp1.showDetails()

# emp2 = Employee("peon", "maths science", 80000)
# emp2.showDetails()

# class Engineer(Employee):
#     def __init__(self, name, age, role, dept, salary):
#         self.name = name
#         self.age = age
#         super().__init__(role, dept, salary)
#         # we can also write this -:
#         # super().__init__("engineer", "software", 90000)

#     def showDetails2(self):
#         print(self.name, self.age, self.role, self.department, self.salary)

# eng1 = Engineer("dev", 17, "engineer", "software", 90000)
# eng1.showDetails2()


# ques 3 -:


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("chips", 40)
odr2 = Order("coke", 50)

print(odr1 > odr2)
