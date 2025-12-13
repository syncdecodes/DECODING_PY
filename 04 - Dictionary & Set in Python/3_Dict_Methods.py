dict1 = {
    "name" : "Divyansh", 
    "age" : 20, 
    "std" : "KMV"
}

print(dict1.keys()) # returns all the keys
print(dict1.values()) # return all the values
print(dict1.items()) # return all key value pairs as tuple 
print(dict1.get("name")) # returns the value according to the key

dict1.update({"12th %" : 81, "10th %" : 81}) # returns updated dict .update can add multiple key value pairs
print(dict1)