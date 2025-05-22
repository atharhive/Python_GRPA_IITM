# This writes the stdin to the input file
import tempfile
import sys
_, filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
    f.write(sys.stdin.read())



with open(filename) as f:
    n = int(f.readline())
    i = 1
    for line in f:
        filled_line = ""
        for char in line:
            if char == "_" and i <= n:
                filled_line += str(i)
                i += 1
            else:
                filled_line += char
        print(filled_line, end="")

