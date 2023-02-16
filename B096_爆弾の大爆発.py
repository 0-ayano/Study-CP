import re

h, w = map(int,input().split())
s    = []
ans  = 0

for c1 in range(h):
    box = ( input() )
    tmp = []
    for c2 in range( len(box) ):
        if box[c2] == "#":
            tmp.append(int(1))
        else :
            tmp.append(int(0))
    s.append(tmp)

for c1 in range(h):
    for c2 in range(w):
        if s[c1][c2] == 1:
            for c3 in range(w):
                if (s[c1][c3] == 0):
                    s[c1][c3] = 2
            for c3 in range(h):
                if (s[c3][c2] == 0):
                    s[c3][c2] = 2
                

for c1 in range(h):
    ans = ans + sum([i > 0 for i in s[c1]])
print(ans)