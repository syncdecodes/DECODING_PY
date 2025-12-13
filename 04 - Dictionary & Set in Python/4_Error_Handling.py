num1 = 10 
num2 = 20 
num3 = 30 
num4 = 40 
num5 = 50 

print(num1)
print(num2)

try:
    print(num3)  # If this part raises any error it will be catched so that the nxt line of codes run properly
except Exception as err:
    print("Error:", err)   # Catch the error and print it - now as we used try except the nxt line of codes will run without any prob.

print(num3)
print(num4)
print(num5)

