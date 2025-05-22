def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
    
    return len(s) % 2 == 1 and s == s[::-1]
