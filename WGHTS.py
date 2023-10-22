# cook your dish here
t=int(input())
for i in range(t):
	l=list(map(int,input().split()))
	#print(l)
 	
	flag=0
	for i in range(1,len(l)):
		for j in range(1,i+1):
			if l[0]==sum(l[j:i+1]) or l[0]==l[1]+l[3]:
				flag=1
		
	if flag==1:
		print('yes')
	elif flag==0:
		print('no')