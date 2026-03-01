#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cout << "Gnomes:\n";
	int T; cin >> T;
	while (T--) {
		int x, y, z; cin >> x >> y >> z;
		if ((x < y && y < z) || (x > y && y > z)) cout << "Ordered\n";
		else cout << "Unordered\n";
	}
}