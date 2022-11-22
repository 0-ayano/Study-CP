# ABC275_D
# Code : UTF-8
# https://atcoder.jp/contests/abc275/tasks/abc275_d
# 再帰関数の高速化

from functools import lru_cache

@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n//2) + f(n//3)

print(f(int(input())))

"""
memo={}
def f(n):
    if(n==0):
        return 1
    if(n in memo.keys()):
        return memo[n]
    memo[n] = f(n//2)+f(n//3)
    return memo[n]
print(f(int(input())))
"""
