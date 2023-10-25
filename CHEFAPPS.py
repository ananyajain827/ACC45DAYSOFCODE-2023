# cook your dish here
t = int(input())
for i in range(t):
    S,X,Y,Z = map(int,input().split())
    if X+Y+Z<=S:
        print(0)
    elif (X+Y <= S and ((S-X>=Z) or (S-Y>=Z))):
        print(1)
    else:
        print(2)
