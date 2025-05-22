def get_freq(filename):
    f = open(filename, 'r')
    freq = dict()
    for line in f:
        word = line.strip()
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    f.close()
    return freq
