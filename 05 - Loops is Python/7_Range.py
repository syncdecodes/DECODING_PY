print(
    "Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."
)

"""range(start?, stop, step?)"""


print("Trying range")
for i in range(1, 11):
    print(i)


print("Trying range steps")
for x in range(10, 110, 10):
    print(x)


print("Odd numbers usinf for loop")
for i in range(1, 50, 2):
    print(i)


print("Even numbers usinf for loop")
for i in range(2, 50, 2):
    print(i)
