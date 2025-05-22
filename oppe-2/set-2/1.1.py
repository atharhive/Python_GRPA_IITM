def sum_of_floored_to_tens(a:int, b:int):
    """
    Calculate the sum of two integers floored to the nearest lower multiple of 10.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers after flooring each to the nearest lower multiple of 10.

    Examples:
        >>> sum_of_floored_to_tens(23, 47)
        60
        >>> sum_of_floored_to_tens(35, 19)
        40
        >>> sum_of_floored_to_tens(0, 105)
        100
    """
    
    
    a = a // 10 * 10
    b = b // 10 * 10
    return a + b
    
