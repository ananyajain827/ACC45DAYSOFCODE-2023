# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x-(x/10)==y):
        print("either")
    elif(x-(x/10)>y):
        print("dining")
    else:
        print("online")
        
    