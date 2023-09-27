# cook your dish here
t=int(input())
for t in range(t):
    x,y=map(int,input().split())
    if x>y:
        print(x//y)
    else:
        print(0)