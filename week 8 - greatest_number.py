def greatest_number(list):
    """ list: numbers' list
        return: the greatest number in the list
    """
    greatest = list[0]
    for i in list:
        if i > greatest:
            greatest = i
    return greatest



