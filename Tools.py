import numpy as np

# returns the percentage of elements of the array are given element
# for this application, % of actions with correct solutions
def percent_correct(array, element):
    array = np.array(array)
    if array.size == 0:
        return 0
    return np.count_nonzero(array == element) / array.size
