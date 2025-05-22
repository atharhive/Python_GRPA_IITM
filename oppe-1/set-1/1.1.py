def sum_squares_abs_diff_squares(a:int, b:int) -> tuple:
    '''Return the sum of squares and the absolute difference of squares.

    Args:
        a, b : int - input numbers

    Returns:
        tuple - tuple with sum of squares and absolute difference of squares.

    '''
    
    return (a**2 + b**2, abs(a**2 - b**2))
