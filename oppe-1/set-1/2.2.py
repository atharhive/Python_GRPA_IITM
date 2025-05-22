
n = int(input())
for i in range(n):
    line = input()
    print("".join([c.upper() if c.lower() in "aeiou" else c.lower() for c in line]))

