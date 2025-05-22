

n = int(input())
for i in range(n):
    roll, marks = map(int, input().split())
    if marks % 10 in [8, 9]:
        marks = (marks // 10 + 1) * 10
        print(roll, marks)

