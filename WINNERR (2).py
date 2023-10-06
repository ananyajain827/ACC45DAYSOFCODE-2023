# cook your dish here
t=int(input())
for i in range(t):
    pa,pb,qa,qb=map(int,input().split())
    if(max(pa,pb)<max(qa,qb)):
        print("P")
    elif(max(qa,qb)<max(pa,pb)):
        print("Q")
    else:
        print("TIE")
    