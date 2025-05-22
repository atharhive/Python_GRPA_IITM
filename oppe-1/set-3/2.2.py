
n = int(input())
for i in range((n//2)):
    a, b = input(),input()
    print(b[::-1])
    print(a)
if n%2:
    print(input()[::-1])

