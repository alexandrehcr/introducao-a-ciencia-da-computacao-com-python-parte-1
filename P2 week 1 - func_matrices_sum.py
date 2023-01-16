# This function add two matrices of the same size

# Input example:
# m1 = [[1, 2, 3], [4, 5, 6]]
# m2 = [[2, 3, 4], [5, 6, 7]]


def matrices_sum(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    # Por terem tamanhos iguais, não importa se eu usar m1 ou m2 para obter o comprimento.
    lines = len(m1)
    columns = len(m1[0])
    added_matrices = []  # Declaração da matriz com as somas

    for i in range(lines):
        lin = []  # Declaração das linhas
        for j in range(columns):
            elements_sum = m1[i][j] + m2[i][j]
            lin.append(elements_sum)
        added_matrices.append(lin)

    return added_matrices
