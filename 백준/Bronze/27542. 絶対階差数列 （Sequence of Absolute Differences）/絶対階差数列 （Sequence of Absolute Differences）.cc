#include <iostream>
using namespace std;

int N;
int arr[2000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) cin >> arr[i];

	for (int k = N - 1; k > 0; k--) {
		for (int i = 0; i < k; i++) arr[i] = abs(arr[i + 1] - arr[i]);
	}

	cout << arr[0];
}