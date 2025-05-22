# This writes the stdin to the input file
import tempfile
import sys
_, filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
    f.write(sys.stdin.read())



with open(filename) as f:
    lines = f.readlines()
    lines, ordering = lines[:-1], lines[-1].strip().split(",")
    ordered_lines = [lines[int(num) - 1] for num in ordering]
    print(*ordered_lines, sep="")

