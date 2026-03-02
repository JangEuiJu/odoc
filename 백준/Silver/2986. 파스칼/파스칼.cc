#include <iostream>
using namespace std;

int N;
int ans;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	ans = N - 1;

	for (int i = 2; i * i <= N; i++) {
		if (N % i) continue;
		ans = N - N / i;
		break;
	}

	cout << ans;
}