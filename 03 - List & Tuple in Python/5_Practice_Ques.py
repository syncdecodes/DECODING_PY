# Ques -1
Movie1 = input("Enter you first fav Movie name: ")
Movie2 = input("Enter you 2nd fav Movie name: ")
Movie3 = input("Enter you 3rd fav Movie name: ")

Fav_Movies = [Movie1, Movie2, Movie3]
print(Fav_Movies)

# 2nd method -:

Mov1 = input("Enter you first fav Movie name: ")
Mov2 = input("Enter you 2nd fav Movie name: ")
Mov3 = input("Enter you 3rd fav Movie name: ")

Movies = []

Movies.append(Mov1)
Movies.append(Mov2)
Movies.append(Mov3)

print(Movies)

# 3rd mehod

Favourite_Mov = []
Favourite_Mov.append(input("Enter you first fav Movie name: "))
Favourite_Mov.append(input("Enter you 2nd fav Movie name: "))
Favourite_Mov.append(input("Enter you 3rd fav Movie name: "))

print(Favourite_Mov)


# Ques -2

print(
    "Lets make a palindrome - we will ask you to enter five value in sequence and then tell you that its palindrome or not: "
)

list1 = []

list1.append(input("Enter some value1: "))
list1.append(input("Enter some value2: "))
list1.append(input("Enter some value3: "))
list1.append(input("Enter some value4: "))
list1.append(input("Enter some value5: "))

list_copy = list1.copy()
list_copy.reverse() # now the list_copy is modified and reversed successfully 

if list1 == list_copy:
    print("Congrats entered values makes a palindrome")
else:
    print("enterd values does not makes a palindrome")

print("Enterd values: ", list1)
