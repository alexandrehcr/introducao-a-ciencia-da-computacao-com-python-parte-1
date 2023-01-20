def remove_repeated(list):
    """ Returns a sorted list with no duplicate elements
    """            
    newList = []
    for x in list:
        if x not in newList:
            newList.append(x)
    return sorted(newList)
