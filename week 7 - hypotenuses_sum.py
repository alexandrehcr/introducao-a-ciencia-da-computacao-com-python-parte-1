""" Write a function that gets an integer `n` as a parameter and returns the sum of all the integers between 1 and n that are hypotenuse's length of any right triangle with integer legs.
h² = i² + j²
"""

def is_hypotenuse(h):
    c1 = 1
    while h > c1:
        c2 = c1 + 1  # To not repeat the same operation twice (e.g.: 2² + 3³ == 3² + 2²) and '+ 1' bc sides can't be equal.
        while h ** 2 > c1 ** 2 + c2 ** 2:
            c2 += 1
        if h ** 2 == c1 ** 2 + c2 ** 2:
            return True
        c1 += 1
    return False


def hypotenuse_sum(n):
    i = 5  # Minimum integer value that an hypotenuse can be, because sides must be different and c1 < c2 < c3
    hyp_sum = 0
    while i <= n:
        if is_hypotenuse(i):
            hyp_sum += i
        i += 1
    return hyp_sum

