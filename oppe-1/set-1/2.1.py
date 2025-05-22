def sum_of_squares_of_even(nums: list) -> int:
    '''Return the sum of squares of all even numbers in the list.

    Args:
        nums : list - list of integers

    Returns:
        int - sum of squares of all even numbers
    '''
    
    
    # 1 - basic solution
    # total = 0
    # for num in nums:
    #     if num%2==0:
    #         total+=num**2
    # return total

    # 2 - comprehensions
    return sum([num**2 for num in nums if num%2==0])

    # 3 - functional
    return sum(map(lambda x: x**2,filter(lambda x: x%2==0, nums)))
    
