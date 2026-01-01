import math
import sys

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
eqn = f"{a}x^2 + {b}x + {c} = 0"
print(eqn)

d = b**2 - 4 * a * c

if d < 0:
    print("no roots exist")
    sys.exit()

elif d > 0:
    r1 = (-b + math.sqrt(d)) / 2 * a
    r2 = (-b - math.sqrt(d)) / 2 * a
    print("root1", r1)
    print("root2", r2)
else:
    r = (-b + math.sqrt(d)) * 2 * a
    print("root", r)
