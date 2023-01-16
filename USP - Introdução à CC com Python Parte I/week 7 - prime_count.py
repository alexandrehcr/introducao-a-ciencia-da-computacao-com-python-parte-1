# Prints the amount of primes less than or equal to the input number

def n_primos(n):
    prime_count = 0
    while n > 1:
        divider = n // 2
        while not n % divider == 0:
            divider -= 1
        if divider == 1:
            prime_count += 1
        n -= 1
        
    return prime_count

