# cook your dish here
import math
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    if(y>x):
        print(0)
    else:
        print(x//(2*y))
