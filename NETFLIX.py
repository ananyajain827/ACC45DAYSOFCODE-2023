# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a+b>=d):
        print("yes")
    elif(b+c>=d):
        print("yes")
    elif(a+c>=d):
        print("yes")
    else:
        print("no")