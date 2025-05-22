def count_odd_three_digit_nums(nums):
    
    
    # count = 0
    # for num in nums:
    #     if num is not None and num%2 and len(str(abs(num)))==3:
    #         count += 1
    # return count
    return sum(
       1
       for num in nums
       if num is not None  and num%2 and len(str(abs(num)))==3
    )
    
