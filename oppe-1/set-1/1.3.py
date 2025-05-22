def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    '''Remove elements at two specified indices in the list.

    Args:
        l : list - input list
        i1, i2 : int - indices of elements to remove
            both are non-negative and unique

    Returns:
        None - modifies the list in place
    '''
    
    i1, i2 = sorted([i1, i2], reverse=True)
    del l[i1]
    del l[i2]
    
    
