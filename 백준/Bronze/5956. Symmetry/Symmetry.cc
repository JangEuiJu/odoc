#include <iostream>
using namespace std;
typedef long long ll;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int R, C; cin >> R >> C;
	ll ans = 0;
	while ((R & 1) && (C & 1)) {
		ans = ans * 4 + 1;
		R >>= 1, C >>= 1;
	}

	cout << ans;
}