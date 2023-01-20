# Prime factorization

n = input('Type a number greater than 1: ')

while not n.isnumeric():
    print ('Invalid input. Type a number greater than 1: ', end = '')
    n = input()
    print()

n = int(n)
factor = 2

while n > 1:
    mult = 0
    while n % factor == 0:
        n /= factor
        mult += 1
    if mult > 0:
        print(f'Factor {factor}, multiplicity {mult}')
    factor += 1
    



