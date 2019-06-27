import os
import operator
from functools import reduce 

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return find_files_helper(suffix, path)


def find_files_helper(suffix, path):
    # Case when path not provided
    if path == "":
        return []

    output = []
    small_outputs = []

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            if suffix != "":  # Case when suffix is provided
                if filepath.endswith(suffix):
                    output.append(filepath)
            else: # Case when suffix is not provided or suffix is empty string
                output.append(filepath)
        
        if(os.path.isdir(filepath)):
            small_outputs.append(find_files_helper(suffix, filepath))

    # Looping through the small_outputs and flatten the small_output using reduce to get a list of paths
    for small_output in small_outputs:
        if small_output is not None and small_output != []:
            output.append(reduce(operator.concat, small_output))

    return output

print(find_files(".c", "/Users/gowrijagadeesh/Documents/OnlineLearning/Udacity/DatastructureAndAlgorithms/testdir"))
print(find_files("", "/Users/gowrijagadeesh/Documents/OnlineLearning/Udacity/DatastructureAndAlgorithms/testdir"))
print(find_files(".c", ""))
print(find_files("", ""))