# we use @property decorator or any method in the class to use the method as a property.


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     def calPer(self):
#         self.per = (self.phy + self.chem + self.math) / 3


# s1 = Student(78, 96, 84)
# s1.phy = 95
# s1.calPer()
# print(s1.per)


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def per(self):
        return (self.phy + self.chem + self.math) / 3

s1 = Student(78, 96, 84)
print(s1.per)

s1.phy = 87
print(s1.per)