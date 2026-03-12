#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int x, y; cin >> x >> y;
	int dist = 1000000007;
	int ansx, ansy;
	int T; cin >> T;
	while (T--) {
		int xx, yy; cin >> xx >> yy;
		int temp = abs(xx - x) + abs(yy - y);
		if (temp < dist) {
			dist = temp;
			ansx = xx, ansy = yy;
		}
	}

	cout << ansx << ' ' << ansy;
}