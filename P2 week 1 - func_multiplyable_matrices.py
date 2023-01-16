# This function multiplies to matrices if they're multiplyable. Two matrices are multiplyable if the number of columns of the first one is the number of lines of second other.

# Input example:
# m1 = [[1], [2], [3]]
# m2 = [[1, 2, 3], [4, 5, 6]]


def are_multiplyable(m1, m2):
    """ Gets to matrices and returns True if they're multiplyable; False otherwise."""
    if len(m1[0]) == len(m2):
        return True
    else:
        return False

