# CPE 202 Lab 1: Allie Blaising

def max_list_iter(int_list):  # must use iteration not recursion
  if int_list == None: 
    raise ValueError
  elif not int_list: 
    return None 
  else: 
    start_max = int_list[0] ## initialize the max variable with the first # in the list of #s 
    for i in int_list: 
      if i > start_max: # if any number in the list is larger than start_max i.e. the first # in the list, then it's the new start_max 
        start_max = i 
    return start_max # once gone through every number in the list, start_max will contain the largest # in the list 


"""finds the max of a list of numbers and returns the value (not the index)
If int_list is empty, returns None. If list is None, raises ValueError"""

def reverse_rec(int_list):   # must use recursion
  if int_list == None: 
    raise ValueError
  elif not int_list: 
      return int_list ## this is the base case, once it's true, i.e. there is an empty list, then we can move into the recursion step below 
  return int_list[-1:] + reverse_rec(int_list[:-1]) # recursion begins, start list by grabbing the last # in the int_list, and beginning to 
  ## create list in reverse order 


"""recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

## for every 3-4 lines of codes, add a comment to explain 

def bin_search(target, low, high, int_list): 
   if int_list == None: 
    raise ValueError 
   if low == high and int_list[low] != target: 
       return None ## checks condition in which there are no results of target in a list, 
   mid = (low + high) // 2 ## calculates mid point 
   if int_list[mid] == target: 
       return mid 
   elif target > int_list[mid]: ## if the target is larger than the value at the mid index, then assuming it's ordered, we need to increase lower bound by 1 
       low = mid + 1 
       return bin_search(target, low, high, int_list) 
   elif target < int_list[mid]: ## if target is smaller than the value at the mid index, then assuming ordered, we need to decrease the upper bound by 1
       high = mid - 1 
       return bin_search(target, low, high, int_list) 
   
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
