def swap_last_chars_of_values(d: dict, k1, k2):
    """Swap the last chars of the values of given keys in the dict.

    Args:
        d (dict): The dictionary with string values.
        k1: The first key.
        k2: The second key.

    Returns:
        None - modifies the dictionary in-place.
    """
    
    
    a, b = d[k1], d[k2]  # to simplify the notation
    d[k1], d[k2] = a[:-1] + b[-1], b[:-1] + a[-1]
    
