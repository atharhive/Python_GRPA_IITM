# This writes the stdin to the input file
import tempfile
import sys
_ , filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
  f.write(sys.stdin.read())



with open(filename) as f:
    vowel_count = 0
    for line in f:
        for char in line:
            if char in 'aeiou':
                if vowel_count % 2 == 0:
                    print("ub", end="")
                else:
                    print("dub", end="")
                vowel_count += 1
            print(char, end="")

