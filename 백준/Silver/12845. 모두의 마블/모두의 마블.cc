#include <iostream>
#include <algorithm>
using namespace std;

bool DESC(int a, int b) {
	return a > b;
}

int main() {
	int N;
	int level[1000];
	int gold = 0;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> level[i];
	}
    
	sort(level, level + N, DESC);

	for (int i = 1; i < N; i++) {
		gold += (level[0] + level[i]);
	}

	cout << gold;

	return 0;
}