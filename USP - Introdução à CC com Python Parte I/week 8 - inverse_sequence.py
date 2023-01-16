# Prompt the user to input numbers that will be added to the list then, when the user types 0, it prints the inputs in opposite order

def get_digit():
    """ Prompt the user for a digit and keep asking if user doesn't input one.
    """
    x = input()
    while not isinstance(x, int):
        try:
            x = int(x)
        except:
            print("NaN. Type a number: ", end='')
            x = input()
    return x


list = []
while True:
    print("Type a number: ", end='')
    n = get_digit()
    if n == 0:
        break
    list.append(n)

for i in range(len(list)):
    print(list[len(list) - (i + 1)])

