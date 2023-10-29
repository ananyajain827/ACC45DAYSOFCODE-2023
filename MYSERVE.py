# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if((x+y)%4==0 or (x+y)%4==1):
        print("alice")
    else:
        print("bob")
        