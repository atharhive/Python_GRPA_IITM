## Q2: Remove elements at given two indices of a list
import re

def remove_elements_at_two_indices(lst, i, j):
    lst.pop(i)
    lst.pop(j-1)

    return lst 
numbs = [1,2,3,4,5]
print(remove_elements_at_two_indices(numbs,1,3))
