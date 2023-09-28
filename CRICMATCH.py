# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    if(36*y>=x):
        print("yes")
    else:
        print("no")