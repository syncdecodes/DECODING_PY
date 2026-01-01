def evenCubes(*num):
    result = []
    for n in num:
        if n % 2 == 0:
            result.append(n**3)
    return result
print(evenCubes(1, 2, 3, 4, 5, 6))