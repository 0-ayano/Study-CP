import numpy as np
def func(x):
   return int(x/2)

h, w = map(int,input().split())
ex1 = []
ex2 = []

for count1 in range(h):
    box = ( list(map(int, input().split())) )
    i   = []
    for count2 in range( w ) :
        i.append(box[count2])
        i.append(box[count2])
    ex1.append(i)
    ex1.append(i)

for count1 in range(h):
    box = ( list(map(int, input().split())) )
    i   = []
    for count2 in range( w ) :
        i.append(box[count2])
        i.append(box[count2])
    ex2.append(i)
    ex2.append(i)

for count1 in range( len(ex1)-1 ):
    a = np.array(ex1[count1+1][1:]) + np.array(ex2[count1][:-1])
    ans = (list(map(func, a)))
    for count2 in range ( len(ans) ):
        if count2 == len(ans)-1:
            print(ans[count2])

        else :
            print(ans[count2], end=" ")