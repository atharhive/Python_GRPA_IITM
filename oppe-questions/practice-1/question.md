# OPPE 2 Questions

## Comprehensions

### Q1: Given a list of numbers, create a new list containing the square of each number using list comprehension.

```python
numbers = [1, 2, 3, 4, 5]
# Expected output: [1, 4, 9, 16, 25]
```

### Q2: Extract all even numbers from a given list using list comprehension.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: [2, 4, 6, 8, 10]
```

### Q3: Create a new list containing the lengths of each string in the given list using list comprehension and lambda function.

```python
strings = ['apple', 'banana', 'cherry', 'date']
# Expected output: [5, 6, 6, 4]
```

### Q4: Create a new list of tuples where each tuple contains a number and its cube for numbers from a list using list comprehension and map function.

```python
numbers = [1, 2, 3, 4, 5]
# Expected output: [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]
```

### Q5: Create a dictionary from two lists using dictionary comprehension.

```python
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
# Expected output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

### Q6: Create a dictionary from a list of names and their lengths using dictionary comprehension.

```python
names = ['Alice', 'Bob', 'Charlie', 'David']
# Expected output: {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'David': 5}
```

## LEGB Rule

### Q7: Create a function that updates the global variable `x` and returns its value.

### Q8: Create a file named 'extra.py' with a variable `x` set to 10. Import this file into `main.py` and create a variable `x` with a different value. Print both variables before and after the import statement to see the difference.

## Dictionary Based questions

### Q9: Find the person having minimum and maximum age from the given list of dictionaries.

```python
details = [
    {'id': 7027, 'name': 'Andrew Owens', 'age': 40, 'city': 'Atlanta', 'email': 'andrew.owens@example.com'},
    {'id': 6121, 'name': 'David Scott', 'age': 64, 'city': 'Houston', 'email': 'david.scott@example.com'},
    {'id': 3149, 'name': 'Katherine Jackson', 'age': 72, 'city': 'Austin', 'email': 'katherine.jackson@example.com'},
    {'id': 4760, 'name': 'Benjamin Williams', 'age': 59, 'city': 'Chicago', 'email': 'benjamin.williams@example.com'},
    {'id': 5542, 'name': 'Emily White', 'age': 30, 'city': 'San Francisco', 'email': 'emily.white@example.com'},
    {'id': 2367, 'name': 'George Harris', 'age': 48, 'city': 'Dallas', 'email': 'george.harris@example.com'},
    {'id': 8145, 'name': 'Michael Brown', 'age': 55, 'city': 'Denver', 'email': 'michael.brown@example.com'},
    {'id': 9821, 'name': 'Sarah Moore', 'age': 27, 'city': 'Seattle', 'email': 'sarah.moore@example.com'},
    {'id': 2794, 'name': 'Jessica Clark', 'age': 61, 'city': 'Miami', 'email': 'jessica.clark@example.com'}
]

# Expected output:
# minimum age is: 27
# maximum age is: 72
```

### Q10: Filter out all items that expire in less than 7 days and print them in a list.

```python
grocery_data = [
    {"item": "Apple", "category": "Fruit", "price": 2.5, "quantity": 10, "expiry_days": 7},
    {"item": "Milk", "category": "Dairy", "price": 3.0, "quantity": 5, "expiry_days": 5},
    {"item": "Bread", "category": "Bakery", "price": 2.0, "quantity": 8, "expiry_days": 4},
    {"item": "Carrot", "category": "Vegetable", "price": 1.2, "quantity": 15, "expiry_days": 10},
    {"item": "Chicken", "category": "Meat", "price": 7.5, "quantity": 3, "expiry_days": 3},
    {"item": "Rice", "category": "Grains", "price": 5.0, "quantity": 20, "expiry_days": 180},
    {"item": "Eggs", "category": "Dairy", "price": 4.0, "quantity": 12, "expiry_days": 14},
    {"item": "Orange", "category": "Fruit", "price": 3.2, "quantity": 10, "expiry_days": 10},
    {"item": "Butter", "category": "Dairy", "price": 6.0, "quantity": 4, "expiry_days": 30},
    {"item": "Potato", "category": "Vegetable", "price": 0.9, "quantity": 25, "expiry_days": 20},
    {"item": "Fish", "category": "Meat", "price": 8.0, "quantity": 2, "expiry_days": 2},
    {"item": "Pasta", "category": "Grains", "price": 4.5, "quantity": 10, "expiry_days": 365}
]
```

### Q11: Create a dictionary where categories are keys and the total price of all items in that category is the value.

### Q12: Write a function that accepts a category and returns the total price of all items in that category.

### Q13: Find the average age of all students.

```python
students = [
    {"id": "S001", "name": "Ananya Sharma", "age": 19, "college": "St. Xavier's College", "major": "Computer Science", "year": 1},
    {"id": "S002", "name": "Arjun Kumar", "age": 20, "college": "Delhi University", "major": "Electrical Engineering", "year": 2},
    {"id": "S003", "name": "Riya Gupta", "age": 21, "college": "University of Mumbai", "major": "Mechanical Engineering", "year": 3},
    {"id": "S004", "name": "Amit Verma", "age": 22, "college": "MIT Pune", "major": "Electronics", "year": 3},
    {"id": "S005", "name": "Neha Patel", "age": 18, "college": "IIT Bombay", "major": "Mathematics", "year": 1},
    {"id": "S006", "name": "Varun Singh", "age": 20, "college": "BITS Pilani", "major": "Civil Engineering", "year": 2},
    {"id": "S007", "name": "Simran Kaur", "age": 22, "college": "Amity University", "major": "Biotechnology", "year": 3},
    {"id": "S008", "name": "Manish Mehta", "age": 19, "college": "Jawaharlal Nehru University", "major": "Physics", "year": 1},
    {"id": "S009", "name": "Pooja Verma", "age": 21, "college": "Lady Shri Ram College", "major": "Political Science", "year": 2},
    {"id": "S010", "name": "Harshad Joshi", "age": 23, "college": "Indian Institute of Science", "major": "Chemical Engineering", "year": 4},
    {"id": "S011", "name": "Sweta Sinha", "age": 18, "college": "SRM Institute of Science and Technology", "major": "Computer Science", "year": 1},
    {"id": "S012", "name": "Shivani Yadav", "age": 22, "college": "VIT Vellore", "major": "Mechanical Engineering", "year": 3},
    {"id": "S013", "name": "Deepak Reddy", "age": 20, "college": "IIT Madras", "major": "Electrical Engineering", "year": 2},
    {"id": "S014", "name": "Ankit Jain", "age": 21, "college": "Loyola College", "major": "Mathematics", "year": 2}
]
```

### Q14: Implement a function that searches for a student by ID and returns their details. If the ID is not found, return "Student not found".

### Q15: Find out which academic year has the most students.

## Matrix Based questions

### Q16: Write a function to compute the transpose of a given N × M matrix.

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Expected output:
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

### Q17: Given an N × M matrix, write a function to return a tuple with maximum row sum and maximum column sum.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Expected output: (24, 18)
```

### Q18: Write a function to multiply two matrices.

```python
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Expected output:
[
    [58, 64],
    [139, 154]
]
```

## Extra Questions

### Q19: Given a string s, input the type of bracket and surround the first two and last two characters of the string with the given bracket type.

```python
s = "Hello World"
bracket_type = "["
# Expected output: "[He]llo Wor[ld]"

s = "Param"
bracket_type = ")"
# Expected output: "(Pa)r(am)"
```

### Q20: Given two numbers `n1` and `n2` return the number that contains more unique digits. If both have the same number of unique digits, return the smaller number.

```python
n1 = 12345
n2 = 67890
# Expected output: 12345

n1 = 112233
n2 = 567890
# Expected output: 567890
```

## CSV File I/O
### Q21: Count the number of "Received," "Declined," and "Called" calls in the dataset. `call_logs.csv`

### Q22: Sort the call logs based on call duration in descending order and write the sorted data to `sorted_calls.csv`.

### Q23: Create 3 CSV files for each call type: "Received," "Declined," and "Called" with the respective call logs.

### Q24: Calculate the total price for each item (i.e., Quantity × Price per Unit) and add a new column "Total Cost". `billing.csv`

### Q25: Find out how many items have a price per unit greater than ₹50 and display their names.

## Text File I/O

### Q26: Extract all email addresses from a text file and save them in a new file. `emails.txt`

### Q27: Write a function that accepts a file and count and print the occurrence of each vowel in the descending order of their frequency. `sentence.txt`


---

35 + 15 = 50 questions
2 days to practice
30-40 mins, 1hr each
- chatgpt, perplexity
1 hr -> 30-40 mins -> 15-20 mins
repeat - 20 questions - 100/100

2 hrs - 120 mins - 100
7 questions, 17 mins approx
- 5 min to read and understand the question
- 5 mins to write pseudocode in pen/paper
- 2 min to write code
- 3 min to fix the errors