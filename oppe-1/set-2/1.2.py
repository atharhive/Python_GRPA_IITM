def within_and_has_double_quotes(s: str) -> bool:
    '''Check if the string is enclosed with double quotes and has double quotes inside.

    Args:
        s : str - input string

    Returns:
        bool - True if the string starts and ends with double quotes and has double quotes inside
    '''
    
    return s[0] == s[-1] == '"' and '"' in s[1:-1]
