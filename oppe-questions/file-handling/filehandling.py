''' name = input("Enter your name: ")
print(f"Hello, {name}!") 

name_file = open("name.txt", "a")
name_file.write(name + "\n") #to change line 
name_file.close() '''

with open("name.txt","r") as name_file:
    name_file.readline() #to ignore first line
    names= name_file.readlines() 

    '''names= name_file.readline().strip()
    names2= name_file.readline()'''

    '''print(names)''' 

    for i in names:
        print(i.upper().strip())
    