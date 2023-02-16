h, w, k = map(int,input().split())
s = []
ans = []

for c1 in range( h ):
    box = input()
    tmp = []
    for c2 in range(w):
        tmp.append( int(box[c2]) )
    s.append(tmp)

for c1 in range( h ):
    for c2 in range ( w ):
        if( c2+(k-1) < h ):
            ans.append(s[c1][c2:c2+k])
        if( c1+(k-1) < h ):
            tmp = []
            for c3 in range(k):
                tmp.append(s[c1+c3][c2])
            ans.append(tmp)

box = []
for c1 in range( len(ans) ):
    tmp = 0
    for c2 in range( len(ans[c1]) ):
        tmp = tmp + ans[c1][c2] * 10**(len(ans[c1])-c2-1)
    box.append(tmp)

print(max(box))
