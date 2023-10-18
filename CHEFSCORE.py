# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(z%y==0):
        print("yes")
    else:
        print("no")