import sys
input = sys.stdin.readline
import numpy as np

def idx_of_the_nearest(data, value):
    idx = np.argmin(np.abs(np.array(data) - value))
    return np.abs( value - data[idx] )

n, k = map(int,input().split())
t = []
for c1 in range(n):
    tmp = int(input())
    t.append(tmp)

tmp = idx_of_the_nearest(t, k)

box = []
for c1 in t:
    if k+tmp >= c1 and k-tmp <= c1:
        box.append(c1)

box.sort()
for c1 in box:
    print(c1)
