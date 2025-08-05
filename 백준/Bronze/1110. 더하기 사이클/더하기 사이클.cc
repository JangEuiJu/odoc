#include <iostream>

using namespace std;

int main() {

	int N;
	int temp;
	cin >> N;

	if (N < 10) N *= 10; 

	int cnt = 0;
	temp = N;

	while (1) {
		cnt++;
		temp = temp % 10 * 10 + (temp / 10 + temp % 10) % 10;

		if (temp == N) {
			break;
		}
	}

	cout << cnt;


	return 0;
}