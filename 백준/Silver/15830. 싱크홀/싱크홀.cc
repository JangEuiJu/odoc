#include <iostream>
using namespace std;
typedef long double ld;

ld V, W, D, DD;
ld T;
int ans = -1;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> V >> W >> D;
	T = W / V;
	while (DD < D) {
		ans++;
		DD += 5 * T * T;
		T *= 1.25;
	}

	cout << ans;
}