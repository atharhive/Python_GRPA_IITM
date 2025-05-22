# Write your code here

n = int(input())
word = ""
for i in range(n):
  if i%2 == 0:
      word = word + input()
  else:
      word = input() + word
print(word)

