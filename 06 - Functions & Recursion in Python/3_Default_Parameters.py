def cal_prod(a, b):
    return a * b

"""
print(cal_prod()) will throw an error bcs arguments a and b are not passed to solve this issue we can give default parameters/value to a and b
"""
try:
    print(cal_prod()) 
except Exception as err:
    print(err)

""" Default parameters -: """

def cal_divi(a=1, b=1):
    return a/b

print(cal_divi())