#include <iostream>
using namespace std;

int lv;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> lv;
	if (lv < 206) cout << 1;
	else if (lv < 218) cout << 2;
	else if (lv < 229) cout << 3;
	else cout << 4;
}