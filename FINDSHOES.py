# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(y>x):
        print(x)
    else:
        print((x-y)*2+y)