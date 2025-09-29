#include <iostream>
#include <cstring>
using namespace std;

int seg[2049];

int upd(int L, int R, int qI, int qVal, int sI) {
	if (R < qI || qI < L) return seg[sI];
	if (L == R) return seg[sI] = qVal;
	return seg[sI] = max(upd(L, (L + R) / 2, qI, qVal, sI * 2), upd((L + R) / 2 + 1, R, qI, qVal, sI * 2 + 1));
}

int rangemax(int L, int R, int qL, int qR, int sI) {
	if (R < qL || qR < L) return 0;
	if (qL <= L && R <= qR) return seg[sI];
	return max(rangemax(L, (L + R) / 2, qL, qR, sI * 2), rangemax((L + R) / 2 + 1, R, qL, qR, sI * 2 + 1));
}

void solve() {
	memset(seg, 0, sizeof(seg));
	int N; cin >> N;
	int NN = N;
	while (NN--) {
		int x; cin >> x;
		int mx = rangemax(1, 1000, 1, x - 1, 1);
		upd(1, 1000, x, mx + 1, 1);
	}

	cout << N - seg[1] << '\n';
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
}