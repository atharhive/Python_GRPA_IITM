def relation(file1, file2):
    f1 = open(file1, 'r')
    L1 = f1.readlines()
    for i in range(len(L1)):
        L1[i] = L1[i].strip()
    f1.close()

    f2 = open(file2, 'r')
    L2 = f2.readlines()
    for i in range(len(L2)):
        L2[i] = L2[i].strip()    
    f2.close()

    if L1 == L2:
        return 'Equal'

    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return 'No Relation'
    return 'Subset'
