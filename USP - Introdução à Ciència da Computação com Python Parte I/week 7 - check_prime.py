n = input("Verify if it's a prime number: ")

while not isinstance(n, int):
    try:                 # used 'try...except' so it can accept negative numbers strings and convert it.
        n = abs(int(n))  # could use 'if n < 0: n *= -1' too.
    except:
        print("Type a number: ", end="")
        n = input()


def is_prime(n):
    if n > 1:
        divider = n // 2
        while not n % divider == 0:
            divider -= 1

        if divider == 1:
            return True
        else:
            return False
    else:
        return False


print("That's a prime!") if (is_prime(n)) else print("Not prime")
