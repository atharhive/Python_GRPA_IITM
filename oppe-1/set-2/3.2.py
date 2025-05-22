
n = int(input())
for i in range(n):
    print(f"{' '*i}\\{' '*(2*(n-i)-1)}/")
print(f"{' '*n}x")
for i in range(n-1,-1,-1):
    print(f"{' '*i}/{' '*(2*(n-i)-1)}\\")

