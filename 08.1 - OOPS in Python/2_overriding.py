# Method overriding -:

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    # Overriding the speak method
    def speak(self):
        return "Woof! Woof!"

generic_animal = Animal()
dog = Dog()

print(f"Generic animal sound: {generic_animal.speak()}")
print(f"Dog sound: {dog.speak()}")



# constructor overriding -:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll):
        # Calls parent class constructor
        super().__init__(name, age)
        
        # Child class properties
        self.roll = roll

s1 = Student("Rohit", 16, 101)
print(s1.name, s1.age, s1.roll)
