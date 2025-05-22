# Write a function `is_odd_length_palindrome` that takes a string `s` and returns `True` if `s` is a palindrome with an odd length and `False` otherwise.

def is_odd_length_palindrome(s):
    # odd_length, palindrome
    # odd length
    n = len(s)
    if n % 2 == 0:
        return False
    
    # palindrome
    if s == s[::-1]:
        palindrome = True
    else:
        palindrome = False
    
    return palindrome
    # return s == s[::-1] and len(s) % 2 == 1

print(is_odd_length_palindrome("noon"))
print(is_odd_length_palindrome("radar"))