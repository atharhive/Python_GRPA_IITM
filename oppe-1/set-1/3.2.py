
n = int(input())
for i in range(n-1):
    print(f"{' '*i}\\{' '*(2*(n-i)-3)}/")
print(' '*(n-1)+'v')

