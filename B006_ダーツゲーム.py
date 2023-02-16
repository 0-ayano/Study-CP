import math

o_y, s, theta = map(int,input().split())
x, y, mark = map(int,input().split())
g = 9.8

ans = o_y + x * math.tan(math.radians(theta))
ans = ans - ( (g*x**2) / (2*s**2*math.cos(math.radians(theta))**2))
ans = round(mark-ans, 1)

if ans > 0.05:
    print( "Hit " + str(ans) )

else :
    print("Miss")