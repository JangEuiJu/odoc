#include <iostream>
using namespace std;
typedef long double ld;

int T;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cout << fixed;
	cout.precision(2);

	cin >> T;
	while (T--) {
		int N; cin >> N;
		ld ans = 0;

		while (N--) {
			string s; ld n, p; cin >> s >> n >> p;
			ans += n * p;
		}

		cout << '$' << ans << '\n';
	}
}