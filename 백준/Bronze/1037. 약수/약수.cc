#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int num;           
	int divisor[50];   
	int N = 0;          

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> divisor[i];
	}

	sort(divisor, divisor + num);

	N = divisor[0] * divisor[num - 1];
	cout << N;

	return 0;
}