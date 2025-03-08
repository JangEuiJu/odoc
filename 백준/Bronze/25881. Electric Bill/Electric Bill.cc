#include<iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int a, b, n;
	cin >> a >> b >> n;

	int energy;
	for (int i = 0; i < n; i++) {
		cin >> energy;

		int fee;
		if (energy >= 1000)
			fee = 1000 * a + (energy - 1000)*b;
		else
			fee = energy * a;

		cout << energy << ' ' << fee << '\n';
	}

	return 0;
}