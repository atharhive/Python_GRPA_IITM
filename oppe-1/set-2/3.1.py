
def walk_L(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[i][0])
    for i in range(1, m):
        path.append(M[m-1][i])
    return path

def walk_Z(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[0][i])
    for i in range(1, m):
        path.append(M[i][m-i-1])
    for i in range(1, m):
        path.append(M[m-1][i])
    return path

def walk_O(M):
    path = []
    m = len(M)
    for i in range(m):
        path.append(M[0][i])
    for i in range(1, m):
        path.append(M[i][m-1])
    for i in range(m-2, -1, -1):
        path.append(M[m-1][i])
    for i in range(m-2, 0, -1):
        path.append(M[i][0])
    return path


def walk_matrix(M, shape):
    """
    Walk along the matrix M according to the specified shape and return the path.

    Args:
        M (list of lists): The square matrix.
        shape (str): Path shape, one of "L", "O", or "Z".

    Returns:
        list: Path along the matrix according to the shape.
    """
    
    
    if shape == 'L':
        return walk_L(M)
    elif shape == 'Z':
        return walk_Z(M)
    elif shape == 'O':
        return walk_O(M)
    else:
        return None
    
