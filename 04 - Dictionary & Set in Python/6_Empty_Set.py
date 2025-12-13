print("Empty Set")

# syntax for empty dictionary is 
collection = {}
name = input("Enter you name: ")
age = input("Enter you age: ")

collection.update({"name" : name, "age" : age})

print(collection) # returns a dictionary with key value pairs
print(type(collection)) # <class 'dict'>

# syntax for empty set is 
data = set() 
name2 = input("Enter you name: ")
age2 = input("Enter you age: ")

data.add(name2)
data.add(age2)

print(data)
print(type(data)) # <class 'set'>
