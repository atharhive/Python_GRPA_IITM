# Write your code here

# Read the number of names
n = int(input())
names = []

# Process each name
for _ in range(n):
    name = input()
    parts = name.split()
    # Create the abbreviated name
    short_name = f'{". ".join(map(lambda x: x[0], parts[:-1]))}. {parts[-1]}'
    names.append(short_name)

# Sort and print the results
for name in sorted(names):
    print(name)

