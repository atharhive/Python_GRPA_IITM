# Q1: Given a list of numbers, create a new list containing the
#  square of each number using list comprehension.

def square(n):
    return n**2

x = [1,2,3,4,5]
y = [square(i)for i in x]

print(y)
