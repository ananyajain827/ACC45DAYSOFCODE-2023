# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if(x%3==0):
        print(0)
    elif(x%3==1):
        print(2)
    else:
        print(1)