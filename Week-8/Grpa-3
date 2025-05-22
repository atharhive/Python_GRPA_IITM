def get_goals(filename, country):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()
    nplayers, ngoals = 0, 0
    for line in f:
        # Unpacking a list into three variables
        player, country_file, goals = line.split(',')
        if country_file == country:
            nplayers += 1
            ngoals += int(goals)
    f.close()
    if nplayers > 0:
        return (nplayers, ngoals)
    return (-1, -1)
