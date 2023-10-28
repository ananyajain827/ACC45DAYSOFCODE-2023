# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if(x%7==1):
        print(x//7)
    elif(x%7==0):
        print(x//7)
    else:
        print((x//7)+1)