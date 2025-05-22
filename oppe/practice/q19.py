### Q19: Given a string s, input the type of bracket and surround the first two and last two characters of the string with the given bracket type.

# s = "Hello World"
# bracket_type = "["
# # Expected output: "[He]llo Wor[ld]"

# s = "Param"
# bracket_type = ")"
# # Expected output: "(Pa)r(am)"

s = "Parampreet"
bracket = input()   # [], (), {}

first_two = s[:2]   # Pa
middle = s[2:-2]    # rampre
last_two = s[-2:]   # et

if bracket == "[" or bracket == "]":
    s2 = "[" + first_two + "]" + middle + "[" + last_two + "]"
elif bracket in "()":
    s2 = "(" + first_two + ")" + middle + "(" + last_two + ")"
elif bracket in "{}":
    s2 = "{" + first_two + "}" + middle + "{" + last_two + "}"
print(s2)