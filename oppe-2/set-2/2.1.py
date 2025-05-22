def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    """
    Counts the number of vowels and consonants at even indices in the given string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing two integers:
            - The first integer is the count of vowels at even indices.
            - The second integer is the count of consonants at even indices.

    Example:
        >>> count_vowels_and_consonants_in_even_indices("example1")
        (3, 1)

        >>> count_vowels_and_consonants_in_even_indices("hello")
        (1, 2)
    """
    
    
    vowel_count = 0
    consonant_count = 0
    for c in s[::2].lower():
        if c in "aeiou":
            vowel_count += 1
        elif c.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count
    
