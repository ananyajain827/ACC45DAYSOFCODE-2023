#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	if(t>=1&&t<=100)
	{
		while(t--)
		{
			int x,y,z;
			cin>>x>>y>>z;
			int hand=x*5+y*10;
			int count=0;
			for(int i=hand;i>=z;i-=z)
			{
				count++;
			}
			cout<<count<<endl;
		}
	}
	return 0;
}