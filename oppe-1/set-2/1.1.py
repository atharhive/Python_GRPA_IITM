def is_positive_odd_or_negative_even(n: int) -> bool:
    '''Check if the number is a positive odd or a negative even.

    Args:
        n : int - input integer

    Returns:
        bool - True if positive odd or negative even, else False
    '''
    
    return (n % 2 != 0 and n > 0) or (n % 2 == 0 and n < 0)
