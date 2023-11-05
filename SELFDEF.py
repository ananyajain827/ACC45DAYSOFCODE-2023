# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    woman=list(map(int,input().split()))
    eligible=0
    for i in range(len(woman)):
        if(woman[i]>=10 and woman[i]<=60):
            eligible+=1
    print(eligible)
        