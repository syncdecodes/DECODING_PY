def indices(mainstr, substr):
    if substr not in mainstr: return -1
    ind = []
    start = 0
    while True:
        index = mainstr.find(substr, start)
        if index == -1: break
        ind.append(index)
        start = index + 1
    return ind
print(indices("abababababababaabab", "abab"))