def is_divisible_by_last_two_digits(num: int):
    """
    Checks if the given number is divisible by both of its last two digits.

    Return False if any of the last two digits is 0.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by both last two digits, False otherwise.
    """
    
    
    a,b = str(num)[-2:]
    a, b = int(a), int(b)
    return a!=0 and b!=0 and num % a == 0 and num % b == 0
    
