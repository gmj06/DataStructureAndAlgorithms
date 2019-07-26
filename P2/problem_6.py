def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if not isinstance(ints, list):
        print("Please provider the list of intergers to get min and max")
        return 
    
    size = len(ints)

    if size <= 0:
        return (0, 0)
    
    if size == 1:
        return (ints[0], ints[0])

    if size == 2:
        if ints[0] < ints[1]:
            return (ints[0], ints[1])
        else:
            return (ints[1], ints[0])
        
    min_ele = ints[0]
    max_ele = ints[size - 1]

    for elem in ints:
        if elem < min_ele:
            min_ele = elem
        elif elem > max_ele:
            max_ele = elem
    
    return (min_ele, max_ele)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# EDGE CASES
print ("Pass" if ((0, 0) == get_min_max([])) else "Fail") # empty list
print ("Pass" if (None == get_min_max('string not list')) else "Fail") # string as input
print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail") # single digit list
print ("Pass" if ((-1, 10) == get_min_max([10, -1])) else "Fail") # list with two ints

print ("Pass" if ((-10, 15) == get_min_max([5, 1, 0, -1, 10, 15, 8, -10])) else "Fail")

