''' with open("gate.csv") as f:
    f.readline()
    lines = f.readlines()

    for l in lines:
        data = l.split(",")
        paper = data[2]

        print(paper) ''' 

import csv

with open("gate.csv") as f:
    reader_software = csv.reader(f)

    next(reader_software)
    data = list(reader_software)

for row in data:
    paper= row[2]
    print(paper)