

s = "azcbobobegghakl"
savestring = ''

for i in range(len(s)):
    if s[i] == 'b':
        if s[i-1] == 'b':
            break
        else:
            savestring = savestring + s[i]
            print(savestring)
            if s[i+1] == 'o':
                savestring = savestring + s[i+1]
                print(savestring)
                if s[i+2] == 'b':
                    savestring = savestring + s[i+2]
                    print(savestring)

print(savestring)