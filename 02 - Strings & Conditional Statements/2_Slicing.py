print("Slicing - means accessing part of a string")
# str[strating_index : ending_index] where ending index is not included
str1 = "syncdecodes@gmail.com"
print(str1[0:11])  # syncdecodes


str2 = "Dev Codes"
print(len(str2))
print(str2[4 : len(str2)])  # Codes
print(str2[4:])  # Codes
print(str2[:4])  # Dev

print("Slicing -ve Indexing")

fruit = "Apple"
print(fruit, "- here index are as follows \ne = -1, l = -2, p = -3, p = -4, A = -5")
print(fruit[-5:-2])  # App note: here also ending index not included

food = "pizza"
print(food[::-1])  # to reverse a string
