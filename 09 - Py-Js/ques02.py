import math
def is_prime(n):
    if n < 2:
        return -1
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def n_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def first_n_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_n_prime(12))