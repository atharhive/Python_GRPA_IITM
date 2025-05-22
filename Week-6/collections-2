
def swap_alternate_elements(t):
    '''Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    
    
    lst_t = list(t)
    for i in range(0, len(lst_t) - 1, 2): 
        lst_t[i], lst_t[i+1] = lst_t[i+1], lst_t[i]
    return tuple(lst_t)
     
