import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append( tmp )
x = int(input())
r, s = [], []
for i in range(x):
    tmp = list(map(int, input().split()))
    r.append( tmp[0] )
    s.append( tmp[1] )

ans = 0
memory = 0
for i in range(x):
    tmp = a[r[i]-1][memory] - a[r[i]-1][s[i]-1]
    memory = s[i]-1
    ans += abs(tmp)
print(ans)
