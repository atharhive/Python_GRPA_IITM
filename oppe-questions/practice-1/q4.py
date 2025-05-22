### Q4: Create a new list of tuples where each tuple contains a number and its cube for numbers from a list using list comprehension and map function.


numbers = [1, 2, 3, 4, 5]
# Expected output: [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

''' cubes = []
for num in numbers:
    t = (num, num**3)
    cubes.append(t)

print(cubes)


cubes2 = [(num, num**3) for num in numbers]
print(cubes2)

# def cube(n):
#     return (n, n**3)

cube = lambda x: (x, x**3)

# map()
cubes3 = []
for num in numbers:
    cubes3.append(cube(num))
print(cubes3)

cubes4 = [cube(num) for num in numbers]
print(cubes4)

# functional programming
cubes5 = list(map(cube, numbers))
print(cubes5) '''

cube = []

for num in numbers:
    t = (num, num**2)
    cube.append(t)

    print(cube)