def mm_dd_yy_to_yy_dd_mm(date: str) -> str:
    """
    Convert a date string from the format mm-dd-yy to yy-dd-mm.

    Args:
        date (str): The date in the format "mm-dd-yy".

    Returns:
        str: The date in the format "yy-dd-mm".

    Example:
        >>> mm_dd_yy_to_yy_dd_mm("12-25-21")
        "21-25-12"
    """
    
    
    mm, dd, yy = date.split('-')
    return f"{yy}-{dd}-{mm}"
    
