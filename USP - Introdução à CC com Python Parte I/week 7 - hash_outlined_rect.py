# Prints custom size rectangle outlined with hashes and empty inside
def to_number(x):
    while not x.isdigit():
        print("Please type a positive integer: ", end='')
        x = input()
    x = int(x)
    return x


def main():
    width = to_number(input("Rectangle's width: "))
    height = to_number(input("Rectangle's height: "))

    i = 0
    while i < height:
        j = 0
        while j < width:
            if j == 0 or i == 0 or i == height - 1 or j == width - 1:
                print("#", end='')
            else:
                print(" ", end = '')
            j += 1
        i += 1
        print()
        
main()
