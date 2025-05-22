def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    return row.index(elem)

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    return len(row) - 1 - row[::-1].index(elem)

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''

    r,c = len(M), len(M[0])
    return 0<=x<r and 0<=y<c

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1,y1)
      for x1,y1 in {(x-1,y), (x+1,y), (x,y-1),(x,y+1)} # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''

    x,y = curr_coords
    for x1,y1 in valid_adjacent_coordinates(x,y, M)-{prev_coords}:
        if M[x1][y1] == value:
            return x1,y1

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)

    path = []
    prev_coords= None
    curr_coords = x_start, y_start
    while curr_coords != (x_end,y_end):
        path.append(curr_coords)
        curr_coords, prev_coords = next_coordinate_with_value(curr_coords, 1, M,prev_coords), (curr_coords)
    path.append(curr_coords)
    return path

def print_path(M):
    path = get_path_coordinates(M)

    for coordinate in path:
        print(coordinate)

def alternate_path(M):
    path = get_path_coordinates(M)

    for i,(x,y) in enumerate(path,1):
        if i%2==0:
            M[x][y] = 2

def count_path(M):
    path = get_path_coordinates(M)

    for i,(x,y) in enumerate(path,1):
        M[x][y] = i

def mirror_horizontally(M):
    path = get_path_coordinates(M)

    for x,y in path:
        M[x][-y-1] = 1

def mirror_vertically(M):
    path = get_path_coordinates(M)

    for x,y in path:
        M[-x-1][y] = 1
