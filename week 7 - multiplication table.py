# Prints the standard multiplication table

column = 1
while column <= 10:
    line = 1
    while line <= 10:
        print(f'{line} x {column} = {line * column}', end='\t')
        line += 1
    column += 1
    print()
