class Dog:
    # 'species' is a class variable, shared by all instances
    species = "Canine"

    def __init__(self, name, age):
        # 'self.name' and 'self.age' are instance variables
        self.name = name  # unique to each instance
        self.age = age  # unique to each instance

    def bark(self): # it is an instance method
        return f"{self.name} says wolf!"

# Create two different instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing and modifying instance variables
print(f"{dog1.name} is {dog1.age} years old and a {dog1.species}")
print(f"{dog2.name} is {dog2.age} years old and a {dog2.species}")

# Modifying dog1's age does not affect dog2
dog1.age = 4
print(f"Dog 1 new age: {dog1.age}")
print(f"Dog 2 age: {dog2.age}") # Value remains unchanged



# # creating class
# class Student:
#     # class attributes
#     name = "karan"

# # creating object (instance)
# s1 = Student()
# print(s1.name)

# # creating object (instance)
# s2 = Student()
# print(s2.name)
