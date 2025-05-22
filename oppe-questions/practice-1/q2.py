### Q2: Extract all even numbers from a given list using list comprehension.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: [2, 4, 6, 8, 10]
'''
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)

print(even_numbers) '''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
