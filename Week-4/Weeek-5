def sum_of_squares(numbers):

    return sum([num**2 for num in numbers])

def total_cost(cart):

    return sum([quantity*price for quantity, price in cart])

def abbreviation(sentence):

    return ".".join([word[0].upper() for word in sentence.split()])+"."

def palindromes(words):

    return [word for word in words if word == word[::-1]]

def all_chars_from_big_words(sentence):

    return {
        letter.lower()
        for word in sentence.split()
        for letter in word
        if len(word)>5
    }

def flatten(lol):

    return [elem for row in lol for elem in row]

def unflatten(items, n_rows):

    n_cols = len(items)//n_rows
    return [
        [items[n_cols*j+i] for i in range(n_cols)]
        for j in range(n_rows)
    ]

def make_identity_matrix(m):

    return [
        [1 if i==j else 0 for i in range(m)]
        for j in range(m)
    ]

def make_lower_triangular_matrix(m):

    return [
        [i+1 if i<=j else 0 for i in range(m)]
        for j in range(m)
    ]
