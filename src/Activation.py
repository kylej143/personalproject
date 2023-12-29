"""
Activation Function
"""


def ReLu(array):
    """
    Applies ReLu Activation function to the array (in place)

    Parameter:
        list or array (ndarray): In the format of nested list (list of list of ints)
    """
    for row in range(len(array)):
        for cell in range(len(array[row])):
            if array[row][cell] < 0:
                array[row][cell] = 0
