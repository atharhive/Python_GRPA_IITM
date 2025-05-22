def num_to_words(mat):
    P = {0: 'zero', 1: 'one', 2: 'two',
    3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight',
    9: 'nine'}
    f = open('words.csv', 'w')
    n = len(mat)
    for i in range(n):
        for j in range(n):
            line = f'{P[mat[i][j]]}'
            # do not add a comma for the elements in the last column
            if j != n - 1:
                line += ','
            f.write(line)
        # go to the next line as long as you are not in the last line
        if i != n - 1:
            f.write('\n')    
    f.close()
