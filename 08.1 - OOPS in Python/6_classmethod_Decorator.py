# A class method is bound to the class and receives 
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("sia")
print(p1.name) # sia
print(Person.name) # anonymous


class Person2:
    name2 = "anonymous2"

    def changeName2(self, name2):
        Person2.name2 = name2

p2 = Person2()
p2.changeName2("sia2")
print(p2.name2) # sia2
print(Person2.name2) # sia2


class Person3:
    name3 = "anonymous3"

    def changeName3(self, name3):
        self.__class__.name3 = name3

p3 = Person3()
p3.changeName3("sia3")
print(p3.name3) # sia3
print(Person3.name3) # sia3


class Person4:
    name4 = "anonymous4"

    @classmethod
    def changeName4(self, name4):
        self.name4 = name4

p4 = Person4()
p4.changeName4("sia4")
print(p4.name4)       # sia4
print(Person4.name4)  # sia4

