def surround_first_two_and_last_two_with_brackets(s: str):
    """
    Surrounds the first two and last two characters of the input string with square brackets.

    It is assumed that the input has atleast four characters.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with the first two and last two characters surrounded by square brackets.

    Example:
        >>> surround_first_two_and_last_two_with_brackets("example")
        '[ex]amp[le]'
    """
    
    return f"[{s[:2]}]{s[2:-2]}[{s[-2:]}]"
