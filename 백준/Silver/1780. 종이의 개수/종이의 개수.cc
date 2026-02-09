#include<iostream>
using namespace std;

int cnt_1 = 0, cnt0 = 0, cnt1 = 0;
int arr[2200][2200];

bool issame(int y, int x, int n) {		
	int num = arr[y][x];
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (num != arr[i][j]) {
				return false;
			}
		}
	}
	return true;
}

void div(int y, int x, int n) {
	if (issame(y, x, n)) {		
		if (arr[y][x] == -1) {
			cnt_1++;
		}
		else if (arr[y][x] == 0) {
			cnt0++;
		}
		else if (arr[y][x] == 1) {
			cnt1++;
		}
	}
	else {		
		int volume = n / 3;		
		for (int i = 0; i < 3; i++) {		
			for (int j = 0; j < 3; j++) {
				div(volume * i + y, volume * j + x, volume);
			}
		}
	}
}

int main(void) {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}
	div(0, 0, n);		
	cout << cnt_1 << '\n' << cnt0 << '\n' << cnt1;
	return 0;
}