## Q1
Write a function `is_odd_length_palindrome` that takes a string `s` and returns `True` if `s` is a palindrome with an odd length and `False` otherwise. 
A palindrome is a string that reads the same forwards and backwards. For example, the strings "racecar" and "level" are palindromes, while the strings "hello" and "goodbye" are not. 

### Example:
- "hello" -> False (not palindrome)
- "noon" -> False (even length palindrome)
- "nun" -> True (odd length palindrome)

```python
def is_odd_length_palindrome(s: str) -> bool:
    length = len(s)
    if length % 2 == 0:
        return False
    
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True
```


## Q2: Remove elements at given two indices of a list
`remove_elements_at_two_indices(lst: List[int], i: int, j: int) -> List[int]`

```py
def sum_of_squares_of_even_numbers(nums):
    # Evens -> Square -> Sum
    # filter, map, sum
    evens = []
    for i in nums:
        if i%2 == 0:
            evens.append(i)
    
    for i in range(len(evens)):
        evens[i] = evens[i]**2

    return sum(evens)
```

## Q3: Sum of squares of even numbers
`sum_of_squares_of_even_numbers(nums: List[int]) -> int`
filter out evens, square them, sum them up

## Q4: Uppercase only vowels

## Q5: Student Marks Filter

Given the data of student marks in the format of list of tuples of format `(rollno:str, marks:int)`, write a function to filter student roll numbers based on the following criteria:

- **'above_average'**: Students with marks above or equal to the average.
- **'below_average'**: Students with marks below the average.
- **'fail'**: Students with marks less than 40.
- **'toppers'**: Students with marks 90 or above.
- **None**: Return all roll numbers.
- **Any other value** should return `None`.

The order of the roll numbers in the filtered roll numbers should be the same as they appear in the data.

### Example:
```
data = [("101", 85), ("102", 75), ("103", 45), ("104", 95), ("105", 35)]

print(get_roll_nos(data, 'above_average')) # Output: ["101", "102", "104"]
print(get_roll_nos(data, 'fail')) # Output: ["105"]
print(get_roll_nos(data, 'toppers')) # Output: ["104"]
print(get_roll_nos(data)) # Output: ["101", "102", "103", "104", "105"]
```


## Q6: Patterns
### 1. Right-Angled Triangle of Stars
```
n = 5
*
* *
* * *
* * * *
* * * * *
```

### 2. Right angle triangle of numbers
```
n = 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### PRACTICE: 3. Inverted Right-Angled Triangle of numbers
```
n = 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

### 4: Number Pyramid
```
n = 5
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```


## Q7: Find the student with the highest & lowest marks

```
students = [
    {"name": "Priya Sharma", "roll": 101, "marks": {"Math": 85, "Science": 92, "English": 78}},
    {"name": "Rahul Patel", "roll": 102, "marks": {"Math": 90, "Science": 88, "English": 82}},
    {"name": "Ananya Singh", "roll": 103, "marks": {"Math": 78, "Science": 95, "English": 88}}
]
```

## Q8: Calculate total price of the cart
```
cart = {
    "Basmati Rice": {"price": 80, "quantity": 2},
    "Toor Dal": {"price": 120, "quantity": 1},
    "Ghee": {"price": 450, "quantity": 1}
}
```

----


# OPPE questions
## Q1: Write a program to merge two dictionaries if a key is present in both dictionaries, sum the values. Assume the values are numbers (int or float).

```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}
merge_dict(d1, d2) -> {'a': 1, 'b': 5, 'c': 7, 'd': 5}
```

```py
def merge_dict(d1, d2):
    d = {}
    for k in d1:
        d[k] = d1[k]
    
    for k in d2:
        if k in d:
            d[k] += d2[k]
        else:
            d[k] = d2[k]
    
    return d
    ...
```

## Q2: Write a program to find most frequent numbers fromt he given numbers in the input. The most frequent valeus should be printed in the ascending order.
Input format is
first n is entered
then n times the numbers are entered


## Q3: Write a program to count the number of students in each engineering branch.

## Q4: Find the average GPA of all students and display the names of students who have a GPA above this average.

## Q5: Write a program to find maximum and minimum age. Print the names of students who lies between the maximum and minimum age (both exclusive).

```
students = [
    {"Roll No": 1, "Name": "Aditi Sharma", "Age": 21, "Gender": "Female", "Branch": "Computer Science", "GPA": 8.9},
    {"Roll No": 2, "Name": "Anuj Gupta", "Age": 22, "Gender": "Male", "Branch": "Mechanical Engineering", "GPA": 7.5},
    {"Roll No": 3, "Name": "Divya Singh", "Age": 20, "Gender": "Female", "Branch": "Electrical Engineering", "GPA": 9.0},
    {"Roll No": 4, "Name": "Kunal Mehta", "Age": 23, "Gender": "Male", "Branch": "Computer Science", "GPA": 8.0},
    {"Roll No": 5, "Name": "Priya Shah", "Age": 19, "Gender": "Female", "Branch": "Chemical Engineering", "GPA": 8.5},
    {"Roll No": 6, "Name": "Rahul Verma", "Age": 21, "Gender": "Male", "Branch": "Civil Engineering", "GPA": 7.2},
    {"Roll No": 7, "Name": "Shreya Patel", "Age": 22, "Gender": "Female", "Branch": "Computer Science", "GPA": 9.5},
    {"Roll No": 8, "Name": "Tanvi Desai", "Age": 20, "Gender": "Female", "Branch": "Electronics and Communication Engineering", "GPA": 9.1},
    {"Roll No": 9, "Name": "Varun Singh", "Age": 23, "Gender": "Male", "Branch": "Information Technology", "GPA": 7.8},
    {"Roll No": 10, "Name": "Yash Gupta", "Age": 21, "Gender": "Male", "Branch": "Mechanical Engineering", "GPA": 8.2}
]
```


## Q6: Find the total salary for each department.

## Q7: Group employees based on their department and list their names under each department.


```
employees = [
    {"Name": "Amit Kumar", "Department": "Finance", "Salary": 75000},
    {"Name": "Neha Sharma", "Department": "HR", "Salary": 68000},
    {"Name": "Rahul Verma", "Department": "IT", "Salary": 85000},
    {"Name": "Priya Desai", "Department": "Marketing", "Salary": 72000},
    {"Name": "Vikas Patel", "Department": "Operations", "Salary": 79000},
    {"Name": "Simran Kaur", "Department": "IT", "Salary": 91000},
    {"Name": "Rohit Mehta", "Department": "Finance", "Salary": 80000},
    {"Name": "Anjali Roy", "Department": "HR", "Salary": 70000},
    {"Name": "Kunal Singh", "Department": "Marketing", "Salary": 76000},
    {"Name": "Tanvi Joshi", "Department": "Operations", "Salary": 73000}
]
```


## Q7: Write a program to input n and make Z pattern for it.
Say: n = 3
***
 *
***

n=5
*****
   *
  *
 *
*****


n = 7, rows = 7, 5
*******
     *  - 5 spaces 1st row, n - i
    *   - 4 spaces 2nd row, n - i
   *    - 3 spaces 3rd row
  *     - 2 spaces 4th row
 *      - 1 space 5th row, 5 - 4 (n - i)
*******

## Q8: Write a program to input n and make W pattern for it.
n = 3
\    /\    /
 \  /  \  /
  \/    \/

"""
Practice questions, open code editor 2-3 hrs
write program for the questions,
if you are stuck
 - chatgpt, perplexity
 - share the question, your code and write "THis is my code ..., this is the question..., my code i"

"""

tic tac toe
random number generator
OTP generator
Mini project: Make ASCII art with loops for A-Z and prompt name and n from user and print their name in ASCII art.
4-5 mini projects from the concepts of week 1 to 6