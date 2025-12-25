#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int D1, M1, Y1, N1, D2, M2, Y2; cin >> D1 >> M1 >> Y1 >> N1 >> D2 >> M2 >> Y2;
	int d1 = D1 + (M1 - 1) * 30 + (Y1 - 1) * 360;
	int d2 = D2 + (M2 - 1) * 30 + (Y2 - 1) * 360;

	cout << (N1 + (d2 - d1) - 1) % 7 + 1;
}