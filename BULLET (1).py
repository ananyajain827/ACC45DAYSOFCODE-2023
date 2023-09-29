# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if((y//x)<z):
        print(z-(y//x))
    else:
        print(0)