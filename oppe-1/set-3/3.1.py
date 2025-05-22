
def get_filter(criteria):
    if criteria == 'continuous':
        return lambda x: x[-3:].lower() == 'ing'
    if criteria == 'vowel_rich':
        return lambda x: len([c for c in x.lower() if c in 'aeiou'])>5
    if criteria == 'consonant_rich':
        return lambda x: len([c for c in x.lower() if c.isalpha() and c not in 'aeiou'])>5
    if criteria == 'sorted':
        return lambda x: "".join(sorted(x.lower())) == x.lower()

def get_words_by_criteria(words, criteria=None):
    """
    Filters words based on the given criteria.

    Args:
        words (list): List of words.
        criteria (str): The filter criteria.

    Returns:
        list: Filtered list of words matching the criteria, or None if invalid criteria.
    """
    
    
    filter_func = get_filter(criteria)
    if filter_func is not None:
        return list(filter(filter_func, words))
    
