def swap_halves(items):

    m = len(items)//2
    return items[m:]+items[:m]

def swap_at_index(items,k):

    return items[k+1:] + items[:k+1]

def rotate_k(items,k=1):

    k = k % len(items)
    return items[-k:]+items[:-k]

def first_and_last_index(items,elem):

    return items.index(elem), len(items)-1-items[::-1].index(elem)

def reverse_first_and_last_halves(items):

    m = len(items)//2
    items[:m], items[m:] = items[:m][::-1], items[m:][::-1]
