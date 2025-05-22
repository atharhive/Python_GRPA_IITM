# Basic idea behind the solution:
# The sum of all steps in a sequence should add up to n
# The last term in any sequence could be either 1, 2 or 3
# The number of sequences with last step as 1 is given by steps(n - 1)
# The number of sequences with last step as 2 is given by steps(n - 2)
# The number of sequences with last step as 3 is given by steps(n - 3)
# So, total number of sequences is steps(n - 1) + steps(n - 2) + steps(n - 3)
def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return steps(1) + steps(2) + 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
