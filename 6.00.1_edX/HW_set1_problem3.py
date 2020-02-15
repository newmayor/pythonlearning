s = 'arunununghhijjabcd'
alpha = 'abcdefghijklmnopqrstuvwxyz'
ans_s = []


for i in range(len(s)):
    print(s[i])
    if s[i] in alpha:
        ans_s[i] = s[i]
        w = alpha.index(s[i])
        for c in range(len(s[i+1:])-1):
            if s[c] == alpha[w+1]:
                ans_s[i] = ans_s[i] + s[c]
                print(ans_s)

