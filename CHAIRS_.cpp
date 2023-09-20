#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
    	int x,y;
    	cin >> x >> y;
    	cout << max(x-y,0) << endl;
    }
	return 0;
}


