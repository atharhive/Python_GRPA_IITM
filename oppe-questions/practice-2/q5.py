## Q1: Write a program to merge two dictionaries if a key is present in both dictionaries, sum the values. Assume the values are numbers (int or float).

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dict(d1, d2) {'a': 1, 'b': 5, 'c': 7, 'd': 5} 

def merge_dic(d1, d2):
    d = {}
    for k in d1:
        d[k]= d1[k]
    for k in d2:
        if k in d:
            d[k] += d2[k]
        else:
            d[k] = d2[k]
    return d

print(merge_dic(d1, d2))
