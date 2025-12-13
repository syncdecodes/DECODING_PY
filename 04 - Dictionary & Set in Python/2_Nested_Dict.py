Students = {
    "Data": {
        "name": "Dev",
        "Class": "10th",
        "Score": {
            "Core sub": {
                "Maths": 95,
                "Science": 89,
                "Basic sub": {
                    "English": 93,
                    "Hindi": 91,
                    "SST": 96,
                },
            }
        },
    }
}

print("0 - ", Students["Data"])
print("1 - ", Students["Data"]["Score"])
print("2 - ", Students["Data"]["Score"]["Core sub"])
print("3 - ", Students["Data"]["Score"]["Core sub"]["Maths"])
print("4 - ", Students["Data"]["Score"]["Core sub"]["Basic sub"])
print("5 - ", Students["Data"]["Score"]["Core sub"]["Basic sub"]["English"])

dict1 = {
    "name" : "kiku", 
    "age" : 17, 
    "std" : "KMV"
}

print(dict1.keys()) # returns all the keys
print(dict1.values()) # return all the values
print(dict1.items()) # return all key value pairs as tuple 

print(dict1["name"]) # .get works like this but try to use .get to not to get error :)
print(dict1.get("name")) # returns the value according to the key

name = "Dev"
name2 = "Sia"

print("You know what we both have 3 letter in our names and that is something special :)")
print("Aaj ek normal day hi tha.. but suddenly you showed up ;) \n and now Dat normal day became special for me") # 29th august 2025
