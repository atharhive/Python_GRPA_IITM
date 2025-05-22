
def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    
    
    # basic
    max_i, max_zeros = -1,-1 # since index and count cannot be less than 0
    for i in range(len(matrix)):
        n_zeros = matrix[i].count(0)
        if n_zeros>max_zeros:
            max_i = i
            max_zeros = n_zeros
    return max_i
    
    # functional approach
    # return max(range(len(matrix)), key= lambda x: matrix[x].count(0))
    

