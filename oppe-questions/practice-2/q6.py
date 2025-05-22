''' Write a program to find most frequent numbers fromt he given numbers in the input. The most frequent valeus should be printed in the ascending order.
Input format is
first n is entered
then n times the numbers are entered '''

n = int(input("enter n: "))

freq = {}
max_count = 0

for i in range(n):
    x = int(input("enter a number: "))
    if x not in freq:
        freq[x]=0
    freq[x] += 1

    if freq[x] > max_count:
        max_count = freq[x]
print(freq, max_count)

most_freq = []
for i in freq:
    if freq[i] == max_count:
        most_freq.append(i)

most_freq.sort()
print(most_freq)





