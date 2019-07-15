def partition(arr):
    """
    Reference: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    """
    start_index = 0
    mid_index = 0
    pivot = 1
    end_index = len(arr) - 1

    while (mid_index <= end_index):
        if arr[mid_index] < pivot:
            swap(arr, start_index, mid_index)
            start_index += 1
            mid_index += 1
        elif arr[mid_index] > pivot:
            swap(arr, mid_index, end_index)
            end_index -= 1
        else:
            mid_index += 1

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp



def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    partition(input_list)
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([1, 0])
test_function([0, 1, 0, 1, 2, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])