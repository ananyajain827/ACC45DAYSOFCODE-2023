# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    print(w+x*z-y*z)