#include <iostream>
#include <string>
#include <set>
using namespace std;

int N;
string s[10];
set<string> st[10];

void solve() {
	cin >> N;
	for (int k = 0; k < N; k++) cin >> s[k];
	for (int len = 60; len > 2; len--) {
		for (int k = 0; k < N; k++) st[k].clear();
		for (int i = 0; i <= 60 - len; i++) {
			for (int k = 0; k < N; k++) {
				st[k].insert(s[k].substr(i, len));
			}
		}
		for (auto& cur : st[0]) {
			bool chk = 1;
			
			for (int k = 1; k < N; k++) {
				if (st[k].count(cur) == 0) chk = 0;
			}
			if (chk) {
				cout << cur << '\n';
				return;
			}
		}
	}

	cout << "no significant commonalities" << '\n';
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T; cin >> T;
	while (T--) solve();
}