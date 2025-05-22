import math
def get_angle(x,y):
    return math.atan2(y,x)

def sort_close_to_y_axis(points):
    return sorted(points, key=lambda p: (abs(p[0]), get_angle(p[0],p[1])))

def closest_point_to_origin(points):
    return min(points, key=lambda p: (abs(p[0]) + abs(p[1]), get_angle(p[0],p[1])))

def get_quadrant(point):
    x, y = point
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

def group_by_quadrant(points):
    groups = {}
    for point in points:
        quadrant = get_quadrant(point)
        if quadrant not in groups:
            groups[quadrant] = set()
        groups[quadrant].add(point)
    return groups


def process_points(points:set, task:str):
    """Process the ponts according to the given task.

    Args:
        points (set[tuple[int,int]]) - Set of points in 
            cartesian corrdinates as (x,y) tuples
        task (str) - String with one of the below values.
            - 'sort_close_to_y_axis'
            - 'closest_point_to_origin'
            - 'group_by_quadrant'

    Returns:
        The output of the corresponding task.

    """
    
    
    if task == "sort_close_to_y_axis":
        return sort_close_to_y_axis(points)
    elif task == "closest_point_to_origin":
        return closest_point_to_origin(points)
    elif task == "group_by_quadrant":
        return group_by_quadrant(points)
    
