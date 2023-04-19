import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    tmp = int(input())
    a.append( tmp )

num = 1
ans = -1
while num <= n:
    for i in a:
        if num == i:
            num = num + 1
            print(num, i)
    ans += 1
print(ans)
