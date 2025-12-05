str1 = "Understanding esacape \nsequence characters"  # \n used for next line
print(str1)


str2 = "For tab spaces \t is used"
print(str2)


# Basic operation on strings -:
print("Concatenation")


str3 = "Hello" + "World"
print(str3)


Fname = "Dev"
Lname = "Shraff"
FullName = Fname + " " + Lname
print(FullName)
print(len(FullName))  # in length of a string spaces are also counted


print("Indexing - we know that in progarmming we start from 0 :)")

Animal = "Monkey"
print("Monkey's name starts with:", Animal[0])
# note that we can access index places of a string but cant change them means -:
#  Animal[0] = D this wont work like Donkey but will throw an error
