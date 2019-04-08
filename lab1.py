


"""finds the max of a list of numbers and returns the value(not the index)
If int_list is empty, it returns None. If list is None, raises ValueError"""
def max_list_iter(int_list):  # must use iteration not recursion
    maximum = 100000
    if len(int_list) == 0:     
        return None
    for item in int_list:
        if item > maximum:
            maximum = item
    return maximum

 """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
def reverse_rec(int_list):   # must use recursion
    if 


 """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
def bin_search(target, low, high, int_list):  # must use recursion
    for i in range(low, high+1):
    
    pass
