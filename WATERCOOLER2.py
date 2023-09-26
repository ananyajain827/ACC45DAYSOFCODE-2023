# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    if(y>x):
        print(y//x)
    else:
        print(0)