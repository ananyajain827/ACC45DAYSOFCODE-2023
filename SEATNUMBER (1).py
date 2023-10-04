# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if(0<x<11):
        print("lower double")
    elif(10<x<16):
        print("lower single")
    elif(15<x<26):
        print("upper double")
    else:
        print("upper single")
        