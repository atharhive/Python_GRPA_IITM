import csv
details = [
    {'id': 7027, 'name': 'Andrew Owens', 'age': 40, 'city': 'Atlanta', 'email': 'andrew.owens@example.com'},
    {'id': 6121, 'name': 'David Scott', 'age': 64, 'city': 'Houston', 'email': 'david.scott@example.com'},
    {'id': 3149, 'name': 'Katherine Jackson', 'age': 72, 'city': 'Austin', 'email': 'katherine.jackson@example.com'},
    {'id': 4760, 'name': 'Benjamin Williams', 'age': 59, 'city': 'Chicago', 'email': 'benjamin.williams@example.com'},
    {'id': 5542, 'name': 'Emily White', 'age': 30, 'city': 'San Francisco', 'email': 'emily.white@example.com'},
    {'id': 2367, 'name': 'George Harris', 'age': 48, 'city': 'Dallas', 'email': 'george.harris@example.com'},
    {'id': 8145, 'name': 'Michael Brown', 'age': 55, 'city': 'Denver', 'email': 'michael.brown@example.com'},
    {'id': 9821, 'name': 'Sarah Moore', 'age': 27, 'city': 'Seattle', 'email': 'sarah.moore@example.com'},
    {'id': 2794, 'name': 'Jessica Clark', 'age': 61, 'city': 'Miami', 'email': 'jessica.clark@example.com'},
    {'id': 4571, 'name': 'Mark Davis', 'age': 39, 'city': 'New York', 'email': 'mark.davis@example.com'},
    {'id': 2840, 'name': 'Linda Miller', 'age': 45, 'city': 'Los Angeles', 'email': 'linda.miller@example.com'},
    {'id': 1932, 'name': 'Patricia Lee', 'age': 67, 'city': 'Philadelphia', 'email': 'patricia.lee@example.com'},
    {'id': 6892, 'name': 'Robert Harris', 'age': 22, 'city': 'Portland', 'email': 'robert.harris@example.com'},
    {'id': 4681, 'name': 'John Martin', 'age': 53, 'city': 'Boston', 'email': 'john.martin@example.com'},
    {'id': 5731, 'name': 'William Robinson', 'age': 37, 'city': 'Phoenix', 'email': 'william.robinson@example.com'},
    {'id': 7345, 'name': 'Dorothy Evans', 'age': 60, 'city': 'San Antonio', 'email': 'dorothy.evans@example.com'},
    {'id': 6415, 'name': 'Alice Wilson', 'age': 50, 'city': 'Las Vegas', 'email': 'alice.wilson@example.com'},
    {'id': 5463, 'name': 'Charles Taylor', 'age': 43, 'city': 'Sacramento', 'email': 'charles.taylor@example.com'},
    {'id': 2178, 'name': 'Helen Clark', 'age': 74, 'city': 'San Diego', 'email': 'helen.clark@example.com'},
    ] 

''' with open("details.csv","w") as f:
    for raw in details:
        values = list(raw.values())
        values[0] = str(values[0])
        values[2]= str(values[2])

        x = ','.join(values)
        print(x)
        f.write(x + "\n") '''

with open("details2.csv","w") as f:
    header= ["id","name","age","city","email"]
    writer= csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    # writer.writerow(details[0])
    writer.writerows(details)

# for list
'''
with open("my.csv","w") as f:
    writer = csv.writer(f)
    header= ["id","name","age","city","email"]
    writer = writerow(header)
    writer = writerows(data)
    
'''