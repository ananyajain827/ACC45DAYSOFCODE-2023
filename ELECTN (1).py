# cook your dish here
for i in range(int(input())):
    N,X=map(int,input().split())
    s=list(map(int,input().split()))
    count=0
    for y in s:
        if(y>=X):
            count=count+1
    print(count)
    
    