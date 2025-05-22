def is_present_in_opposite_halves(elem, l1: list, l2: list):
    """
    Determines whether an element is present in the first half of one list 
    and the second half of the other list, or vice versa.

    Args:
        elem (Any): The element to check for.
        l1 (list): The first list to search.
        l2 (list): The second list to search.

    Returns:
        bool: True if `elem` is present in opposite halves of `l1` and `l2`, 
        False otherwise.
    """
    
    
    m1 = len(l1) // 2
    m2 = len(l2) // 2
    return (
        (elem in l1[:m1] and elem in l2[m2:])
        or (elem in l1[m1:] and elem in l2[:m2])
    )
    
