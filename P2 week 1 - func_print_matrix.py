# Prints a two dimension matrix

# Input example
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(matrix):
    """ Gets a list of lists (matrix) and print it. """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == (len(matrix[0]) - 1):
                space = ''
            else:
                space = ' '
            print(f'{matrix[i][j]}', end=space)
        print()

