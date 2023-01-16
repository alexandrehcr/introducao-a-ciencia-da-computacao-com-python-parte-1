# Those functions get a list of strings, strip the blank spaces, capitalize them and return the smallest or largest strings in the list.

# Input example:
# names_list = ["josé  ", " Arquibaldo", "Bia", "Alouhis ","pedro", "Fernando", " Clodoaldo ", " valdemiro", "ana"]

# Helper function to smallest_names and largest_names
def format_list(list):
    """ Remove the blank spaces at the ends, capitalize and sort strings in alphabetical order. """
    for i in range(len(list)):
        list[i] = list[i].strip().capitalize()
    list.sort()
    return list


def smallest_names(names_list):
    """ Gets a list of strings and returns a list with the smallest strings in alphabetical order if there's more than one. """
    format_list(names_list)
    smallest = [names_list[0]]
    for i in names_list:
        for j in range(len(smallest)):
            if len(i) < len(smallest[j]):
                smallest = []
                smallest.append(i)
            elif len(i) == len(smallest[j]) and smallest[j] != i:
                smallest.append(i)
    return smallest


def largest_names(names_list):
    """ Gets a list of strings and returns a list with the largest strings in alphabetical order if there's more than one.
    """ 
    format_list(names_list)
    largest = [names_list[0]]
    for i in names_list:
        for j in range(len(largest)):
            if len(i) > len(largest[j]):
                largest = []
                largest.append(i)
            elif len(i) == len(largest[j]) and i != largest[j]:
                largest.append(i)
    return largest

