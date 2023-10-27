t = int(input())
for i in range(t):
    a1,a2,b1,b2 = map(int,input().split())
    nxa = a1 - a2
    nxb = b1 - b2
    if(nxa+nxb<0):
        print('YES')
    else:
        print('NO')
    