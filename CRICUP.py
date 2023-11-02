# cook your dish here
t= int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(abs(x-y)<=z):
        print("yes")
    else:
        print("no")