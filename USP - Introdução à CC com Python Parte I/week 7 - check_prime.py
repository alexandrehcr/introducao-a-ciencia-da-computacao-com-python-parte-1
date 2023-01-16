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


# ===========================================================================
'''I could also use the code bellow to convert the n string to integer, but it wouldn't accept negative integers.'''
# while not n.isdigit():
#     print("\nInsira somente números.")
#     n = input()
# n = int(n)

# ===========================================================================
'''Likewise, I could also declare the function as shown bellow, but it does more tests.'''
# def is_prime(n):
#     if n > 1:
#         divider = 2

#         while not n % divider == 0:
#             divider += 1

#         if divider == n:
#             return True
#         else:
#             return False
#     else:
#         return False
'''To do about the same number of tests, I could create an 'max_div = math.ceil(n / 2)' variable, put the condition 'while not n % divider and divider <= max_div' and, lastly, modify the 2nd if to be 'if divider == max_div', but it would require more lines of code as well as time to comprehend.'''
# ===========================================================================
