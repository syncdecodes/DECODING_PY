# print("Ques 1 - counting from 1 to 25")

# num = 1
# while num <= 25:
#     print(num)
#     num += 1


# print("Ques 2 - counting from 25 to 1")

# num2 = 25
# while num2 >= 1:
#     print(num2)
#     num2 -= 1


# print("Ques 3 - write a table")

# num3 = 1
# while num3 <= 10:
#     print("7 x", num3, "=", num3 * 7)
#     num3 += 1


# print("Ques 4 - printing elements in list using loop")

# list1 = []
# num4 = 1
# while num4 <= 10:
#     list1.append(num4 * num4)
#     num4 += 1
# print(list1)


# print("Ques 5 write a table but on user's demand")

# table_no = float(input("Enter a number to print its table: "))
# num5 = 1
# while num5 <= 10:
#     print(table_no, "x", num5, "=", num5 * table_no)
#     num5 += 1


# print("ques 6 - print list value using loop")

# list2 = ["apple", "banana", "kiwi", "melon", "orange", "papaya"]
# index = 0
# while index < len(list2):
#     print(list2[index])
#     index += 1


# print("Ques 7 - search for x in tuple")
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 11)
# x = 7
# idx = 0
# while idx < len(tup):
#     if tup[idx] == x:
#         print(x, "Found at index", idx)
#     else:
#         print("Finding")
#     idx += 1


print("Ques 8 - print all the odd numbers bw 50 and 1")

x = 50
while x >= 1:
    if x % 2 == 0:
        x -= 1
        continue
    print(x)
    x -= 1


print("Ques 8 - print all the even numbers bw 50 and 1")

y = 50
while y >= 1:
    if (y % 2 == 0):
        print(y)
        y -= 1
        continue
    y -= 1
