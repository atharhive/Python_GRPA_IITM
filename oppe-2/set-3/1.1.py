def product_of_sum_and_abs_diff_of_digits(num: int):
    """Returns the product of the sum and absolute difference of digits of a two digit number.

    Assume number is a two digit number.

    Args:
        num (int) - The given number

    Returns:
        The required product.

    Examples:
        >>> product_of_sum_and_abs_diff_of_digits(38)
        55
        >>> product_of_sum_and_abs_diff_of_digits(55)
        0
    """
    
    
    a, b = num // 10, num % 10
    return (a + b) * abs(a - b)
    
