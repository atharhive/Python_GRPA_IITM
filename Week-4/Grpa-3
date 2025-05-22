min =  None

def find_min(items:list):

    minimum = items[0]
    for item in items[1:]:
        if item<minimum:
            minimum = item
    return minimum

def odd_increment_even_decrement_no_modify(items) -> list:

    new_items = []
    for item in items:
        if item%2!=0:
            new_items.append(item+1)
        else:
            new_items.append(item-1)
    return new_items

def odd_square_even_double_modify(items:list) -> list:

    for i in range(len(items)):
        if items[i]%2!=0:
            items[i]**=2
        else:
            items[i]*=2
    return items

def more_than_two_unique_vowels(sentence):

    vowels = set("aeiou")
    words = set()
    for word in sentence.split(","):
        if len(set(word) & vowels)>2:
            words.add(word)
    return words

def sum_of_list_of_lists(lol):

    total = 0
    for row in lol:
        for n in row:
            total+=n
    return total

def flatten(lol):

    flat = []
    for row in lol:
        for item in row:
            flat.append(item)
    return flat

def all_common(strings):

    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    return ''.join(sorted(common_chars))

def vocabulary(sentences):

    vocab = set()
    for sentence in sentences:
        for word in sentence.split(" "):
            vocab.add(word.lower())
    return vocab
