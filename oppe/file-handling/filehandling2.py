with open("para.txt", "r") as f:
    lines = f.read()

    count = lines.count(".") # for we can use count of " " 
    print("no. of sentences: ", count) 