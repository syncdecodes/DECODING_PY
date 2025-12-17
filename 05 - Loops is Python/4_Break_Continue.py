# break 1
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

# break 2
print("Ques 7 - advanced search for x in tuple")
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 11)
x = int(input("Enter num bw 1 - 11 to get its index in tuple: "))

idx = 0
while idx < len(tup):
    if x > 12:
        print("Enter number bw 1 - 11 only")
    else:
        if tup[idx] == x:
            print(x, "Found at index: ", idx)
            break
        else:
            print("Finding.....")
            idx += 1

# continue
n = 0
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1


""" 
continue ka matlab hota hai → is iteration ka baaki code skip karo aur loop firse start karo if the condition is true as per the code.

Matlab agar condition true hui aur continue mila, to uske baad ka code us iteration me nahi chalega but if the condition is false the baki ka code chalega again as per the code.
"""