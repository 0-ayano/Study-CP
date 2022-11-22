# ABC278_C
# Code : UTF-8
# https://atcoder.jp/contests/abc278/tasks/abc278_c
# 条件判定

import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
F = set()
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        F.add((a,b))
    if t == 2:
        F.discard((a,b))
    if t == 3:
        if (a,b) in F and (b,a) in F:
            print('Yes')
        else:
            print('No')
