function is_prime(n) {
    if (n < 2) return -1
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false
    }
    return true
}

function n_prime(n) {
    let primes = []
    for (let i = 2; i <= n; i++) {
        if (is_prime(i)) primes.push(i)
    }
    return primes
}

function first_n_primes(n) {
    let primes = []
    num = 2
    while (primes.length < n) {
        if (is_prime(num)) primes.push(num)
        num++
    }
    return primes
}

console.log(first_n_primes(12))