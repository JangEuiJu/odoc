#include <iostream>
#include <algorithm>

using namespace std;
int H, W, X, Y;
int arr[601][601] = { 0 };

void solve() {
	for (int i = X; i < H; i++) {
		for (int j = Y; j < W; j++) {
			arr[i][j] -= arr[i - X][j - Y];
		}
	}
	for (int i = 0; i < H ; i++) {
		for (int j = 0; j < W ; j++) {
			cout << arr[i][j]<< " ";
		}
		cout << "\n";
	}
}
int main() {
	cin >> H>>W>>X>>Y;
	for (int i = 0; i < H + X; i++) {
		for (int j = 0; j < W + Y; j++) {
			cin >> arr[i][j];
		}
	}
	solve();
	return 0;
}