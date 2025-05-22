def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
    
    
    # 1 - Basic method
    # count =0
    # for num in nums:
    #     if num is not None and num>0:
    #         count += 1
    # return count

    # 2 - Comprehensions
    # return len([num for num in nums if num is not None and num>0])

    # 3 - functional
    return len(list(filter(lambda x : x is not None and x>0, nums)))
    
