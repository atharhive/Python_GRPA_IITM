

num_word = {
    0: 'zero',1: 'one',2: 'two',3: 'three',
    4: 'four',5: 'five',6: 'six',7: 'seven',
    8: 'eight',9: 'nine'
}


def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    
    
    words = []
    for digit in str(num):
        words.append(num_word[int(digit)])
    return "-".join(words)
    
    # comprehensions
    return '-'.join(num_word[int(digit)] for digit in str(num))
    # functional
    # return "-".join(map(num_word.get, map(int, str(num))))
    
