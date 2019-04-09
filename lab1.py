
"""finds the max of a list of numbers and returns the value(not the index)
If int_list is empty, it returns None. If list is None, raises ValueError"""
def max_list_iter(int_list):  # must use iteration not recursion
    maximum = -100000 #change to -2^(32)-1
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    for item in int_list:
        if item > maximum:
            maximum = item
    return maximum

"""recursively reverses a list of numbers and returns the reversed list
If list is None, raises ValueError"""
def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError
    if len(int_list) == 1:
        return int_list
    return [int_list[-1]] + reverse_rec(int_list[:-1])
    
"""searches for target in int_list[low..high] and returns index if found
If target is not found returns None. If list is None, raises ValueError """
def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:
        raise ValueError
    if not low < high:
        return None
    mid_point = (high + low) // 2
    if int_list[mid_point] == target:
        return mid_point
    if int_list[mid_point] > target:
        return bin_search(target, low, mid_point, int_list)
    if int_list[mid_point] < target:
        return bin_search(target, mid_point+1, high, int_list)

