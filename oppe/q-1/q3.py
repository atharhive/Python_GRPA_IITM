# sum of squares of even numbers in a list 

def sum_of_squares_of_even_numbers(nums):
    even = []
    for i in nums:
        if i%2 ==0:
            even.append(i)

    for i in range(len(even)):
        even[i] = even[i]**2

    return sum(even) 

x = [1,2,3,4,5]
print(sum_of_squares_of_even_numbers(x)) 

# another way
''' 
def is_even(n):
    return n%2==0

def square(n):
    return n**2

def sum_of_squares_of_even_numbers(nums):
     

    evens = filter(is_even,nums)
    squares = map(square, evens)
    

    return sum(squares)

x = [1,2,3,4,5]
print(sum_of_squares_of_even_numbers(x))

'''



