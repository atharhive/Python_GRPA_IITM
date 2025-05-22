import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''

    groups = {}
    for item in data:
        group = key(item)
        if group not in groups:
            groups[group] = []
        groups[group].append(item)
    return groups

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''

    return {
      group: func(members)
      for group, members in groups.items()
    }

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''

    return min(map(lambda x:x[course], student_data))

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''

    return max(map(lambda x:x[course], student_data))

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''

    return max(student_data,key= lambda x: x[course])['rollno']

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''

    sorted_student_data = sorted(student_data,key= lambda stud: (stud[course1],stud[course2],stud[course3]))
    return list(map(lambda stud: stud["rollno"], sorted_student_data))

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''

    students_by_city = groupby(student_data, lambda stud: stud["city"])
    return apply_to_groups(students_by_city, len)

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''

    city_student_count = count_students_by_cities(student_data)
    return max(city_student_count, key=city_student_count.get)

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''

    # this lambda is named so that it is easy to remember what it is doing.
    get_sorted_rollnos = lambda items: sorted(map(lambda item: item['rollno'],items))
    students_by_city = groupby(student_data, lambda x: x["city"])
    return apply_to_groups(students_by_city, get_sorted_rollnos)

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''

    students_by_city = groupby(student_data, lambda x: x['city'])
    avg = lambda x: sum(x)/len(x)
    get_course_avg = lambda items: avg(list(map(lambda x: x[course], items)))
    course_avg_by_city = apply_to_groups(students_by_city,get_course_avg)
    return max(course_avg_by_city, key=course_avg_by_city.get)
