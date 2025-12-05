str1 = "hello I am syncdecodes"

print(str1.endswith("decodes"))  # True
print(str1.startswith("In"))  # False
print(str1.capitalize())  # capitalize 1st char

str1 = str1.replace("hello I am syncdecodes", "hello I am dev codes")
str1 = str1.capitalize()
print(str1)  # Hello I am dev codes

str2 = "Lion is king of the jungle"
print(str2.find("king"))  # Retunrs starting index of king which is 8

str3 = "hello I am dev and I am 17 years old"
print(str3.count("am"))  # 2 as am occured 2 times in str3
