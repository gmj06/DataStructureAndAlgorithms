
def search_pivot(arr, start_index, end_index):
    """
    Identify the index at which the given array is rotated
    """
    if end_index < start_index:
        return -1
    if end_index == start_index:
        return start_index


    mid = (start_index + (end_index - start_index))//2

    if mid < end_index and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > start_index and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[start_index] >= arr[mid]:
        return search_pivot(arr, start_index, mid - 1)
    else: 
        return search_pivot(arr, mid + 1, end_index)


def binary_search_recursive(arr, target, start_index, end_index):
    """
    Searching the target in the given array using Binary Search Recursive approach    
    """
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = arr[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(arr, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(arr, target, mid_index + 1, end_index)
        

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = search_pivot(input_list, 0, len(input_list) - 1)
    # print(f"pivot - {str(pivot)}")

    if pivot == -1: # given array is not rotated
        return binary_search_recursive(input_list, number, 0, len(input_list) - 1)

    if input_list[pivot] == number:
        return pivot
    elif input_list[0] <= number: 
        return binary_search_recursive(input_list, number, 0, pivot - 1)
    else:
        return binary_search_recursive(input_list, number, pivot + 1, len(input_list) - 1)




def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    # print(f"linear_search(input_list, number) - {str(linear_search(input_list, number))}")
    # print(f"rotated_array_search(input_list, number) - {str(rotated_array_search(input_list, number))}")


    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[], 5]) # empty array
test_function([[4, 5, 1, 2, 3], 3]) # number = last element of an array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # number = first element of an array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # number exists in the array
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # number = element at pivot
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # number = element at (pivot - 1)
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # number does not exists in the given array
test_function([[1, 2, 3, 4, 5, 6, 7], 10]) # number does not exists in the given sorted array
test_function([[1, 2, 3, 4, 5, 6, 7], 5]) # number exists in the given sorted array