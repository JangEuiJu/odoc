#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int L, R, A; cin >> L >> R >> A;
	int total = L + R + A;

	if (L < R) {
		int diff = min(R - L, A);
		L += diff, A -= diff;
	}
	else {
		int diff = min(L - R, A);
		R += diff, A -= diff;
	}

	if (R == L) cout << total - (A & 1);
	else cout << total - abs(R - L);
}