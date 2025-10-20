#include<bits/stdc++.h>
using namespace std;

int N, Q;
int pSum[111111][3];

int main() {ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

cin >> N >> Q;
for (int i = 1; i <= N; ++i) {
	for (int k = 0; k < 3; ++k) pSum[i][k] = pSum[i - 1][k];
	int num;
	cin >> num;
	pSum[i][num - 1]++;
}
for (int i = 0; i < Q; ++i) {
	int l, r;
	cin >> l >> r;
	cout << pSum[r][0] - pSum[l - 1][0] << ' ';
	cout << pSum[r][1] - pSum[l - 1][1] << ' ';
	cout << pSum[r][2] - pSum[l - 1][2] << '\n';
}

return 0;
}