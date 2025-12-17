# print("Ques 1 - create a list and print its element using for loop")
# list1 = []
# num = 1
# while num <= 10:
#     list1.append(num * num)
#     num += 1
# print(list1)

# for val in list1:
#     print(val)


print("Ques 2 - create a tuple which contains square of numbers from 1 to 10 and then ask the user to 'Enter any square number bw 1 to 10' and find its index number in the tuple and show it to the user")

list3 = []
num3 = 1
while num3 <= 10:
    list3.append(num3 * num3)
    num3 += 1
tup3 = tuple(list3)
print(tup3)

x = int(input("Enter any square number of 1 to 10: "))

idx = 0
for el in tup3:
    if el == x:
        print(x, "Found at index", idx)
        break
    print("Finding index of entered number....")
    idx += 1


# print("Ques 3 - linear searches")
# tup4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# z = 6
# idx = 0
# for el in tup4:
#     if el == z:
#         print("num found at index", idx)
#         break
#     else:
#         print("Finding num")
#     idx += 1
