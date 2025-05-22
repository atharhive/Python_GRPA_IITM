def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
    '''
    Increment the value for the given key in the 
    dictionary by `inc`, but not beyond `limit`.

    Modify the value in the dictionary do not return the new value.

    Args:
        d : dict - dictionary with integer values
        key : str - key to increment in the dictionary
        inc : int - increment value
        limit : int - maximum limit for the value

    Returns:
        None
    '''
    
    d[key] = min(d[key]+inc, limit)
