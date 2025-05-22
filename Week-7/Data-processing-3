


def find_longest_antakshari(words):
    max_len = 1
    prev_word = words[0]
    anthakshari_len = 1
    for word in words[1:]:
        if prev_word[-1] == word[0]:
            anthakshari_len +=1
        else:
            anthakshari_len = 1
        if anthakshari_len > max_len:
            max_len = anthakshari_len
        prev_word = word
    return max_len

n = int(input())
for i in range(n):
    print(find_longest_antakshari(input().split(',')))
        

