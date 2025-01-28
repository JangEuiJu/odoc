#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, w, d, total;

	while (cin >> N >> w >> d >> total) {
		int ans = (w * (N * (N - 1)) / 2 - total) / d;
		if (ans) cout << ans << '\n';
		else cout << N << '\n';
	}
}