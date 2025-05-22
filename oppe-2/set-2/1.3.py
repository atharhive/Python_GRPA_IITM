def number_with_more_unique_digits(n1:int, n2:int):
    """
    Compares two integers and returns the one with more unique digits.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int or tuple: The integer with more unique digits. 
        If both numbers have the same number of unique digits, 
        returns a tuple of both integers `(n1, n2)`.

    Example:
        >>> number_with_more_unique_digits(123, 1122)
        123

        >>> number_with_more_unique_digits(1122, 2211)
        (1122, 2211)
    """
    
    
    n1_n_unique = len(set(str(n1)))
    n2_n_unique = len(set(str(n2)))
    if n1_n_unique> n2_n_unique:
        return n1
    elif n2_n_unique> n1_n_unique:
        return n2
    else:
        return (n1,n2)
    
