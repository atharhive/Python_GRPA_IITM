
n = int(input())
for i in range(n):
  a,b = map(int, input().split(','))
  if i%2==0:
      print(a+b)
  else:
      print(abs(a-b))

