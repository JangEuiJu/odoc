#include <iostream>
using namespace std;

int main() {
	int test, fNum, lNum;
	cin >> test;
	int* sum = new int[test];

	for (int i = 0; i < test; i++) {
		cin >> fNum >> lNum;
		sum[i] = fNum + lNum;
	}
	for (int i = 1; i <= test; i++) {
		cout << "Case " << i << ": " << sum[i - 1] << '\n';
	}
	delete []sum;
}