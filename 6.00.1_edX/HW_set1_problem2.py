count = 0

for i in range(len(s)):
    if s[i : i+len('bob')] == 'bob':
        count += 1

print("Number of times bob occurs is: " + str(count))