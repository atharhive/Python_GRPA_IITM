def div_by_exactly_one(num: int, a: int, b: int) -> bool:
    '''Check if num is divisible by exactly one of a or b.

    Args:
        num, a, b : int - input numbers

    Returns:
        bool - True if num is divisible by exactly one of a or b, otherwise False.
    '''
    
    return (num % a == 0) ^ (num % b == 0)
