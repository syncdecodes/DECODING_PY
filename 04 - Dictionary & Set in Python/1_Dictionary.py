print("Just like objects in JS there is Dictionary in python: ")
print("Dictionaries are used to store data values in key : value pairs")
print("In dictionaries values can be string, Integers, Float, Boolean, tuple, List\nbut keys can only be strings, Integers and Float")
print("Dict. are mutable(changeable) and dont allow duplicate keys")




dict1 = {"name": "Dev", "age": 17, "Is_Teen" : True, "std": "KMV", "Marks" : [93, 98, 87, 74, 83]}

print(dict1)
print(type(dict1)) # <class 'dict'>

print(dict1["name"])
dict1["age"] = 18

# Updating existing key value pairs -:
print(dict1["age"])
print(dict1)

# Adding new key value pairs -:
dict1["Github"] = "syncdecodes"
dict1.update({"Email" : "syncdecodes@gmail.com", "Mobile no." : 8588949227}) # .update is used to update/add multible key value pairs in the dictionary.
print(dict1)

# Creating a null_dictonary -:
null_dict = {}
name = input("Enter your name: ")
age = input("Enter your age: ")

"""
null_dict.append(name) AttributeError: 'dict' object has no attribute 'append'
null_dict.append(age) AttributeError: 'dict' object has no attribute 'append'
"""

null_dict["name"] = name
null_dict["age"] = age
print(null_dict)