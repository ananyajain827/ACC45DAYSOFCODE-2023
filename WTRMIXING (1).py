# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    if(b==a):
        print("yes")
    elif(b>a):
        if((b-a)<=x):
            print("yes")
        else:
            print("no")
    else:  
        if((a-b)<=y):
            print("yes")
        else:
            print("no")