### Q3: Create a new list containing the lengths of each string in the given list using list comprehension 

strings = ['apple', 'banana', 'cherry', 'date']
# Expected output: [5, 6, 6, 4]

legths = []

for s in strings:
    n = len(s)
    legths.append(n)

print(legths)
legths2 = [len(s)for s in strings]
print(legths2)