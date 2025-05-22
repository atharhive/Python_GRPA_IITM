"""
# List continued
lst = [1, 2, 3, 4, 5]
lst[1:3] = [0]
print(lst)

List matrix based question
- PRACTICE: Addition, transpose, matrix multiplication

# Functions continued
- calling same function on function
- list default value at argument


- Dictionary
- Set

- If-else expression 1 liner
- Comprehension: List, Dict, Set

- Lambda function

- Map, Filter, reverse, sorted, zip, enumearte, any, all, sum, min/max

not and operator


Dict -> keys and in set the elements must be hashable (immutable)

Immutable (cannot be changed/modified) -> string, tuple, frozenset
mutable (can be changed/modified) -> list, set, dict

python < 3.9 -> dict, set -> unordered
python > 3.9 -> dict are ordered, set are unordered


set
- unique elements
- immutable (hashable) elements
- cannot be indexed
- cannot be sliced
"""

name = ['a', 'b', 'c', 'd', 'e']
age = [10, 20, 30, 40]


# n = len(name)
# for i in range(n):
#     print(name[i], age[i])


for i in zip(name, age, strict=True):
    # n = i[0]
    # a = i[1]
    n, a = i    # n, a = (name, age)
    print(i, n, a)