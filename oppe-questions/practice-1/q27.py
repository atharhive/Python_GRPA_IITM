### Q26: Extract all email addresses from a text file and save them in a new file. `emails.txt`

with open("emails.txt") as f:
    content = f.read()

print(content)

words = content.split()
print(words)

def is_email(word):
    return "@" in word

emails = []
for w in words:
     if is_email(w):
         emails.append(w)
print(emails)

''' emails = [ w for w in words if is_email(w)]
print(emails)

with open("emails2.txt", "w") as f2:
    for e in emails:
        f2.write(e + "\n")'''