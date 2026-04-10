#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s; cin >> s;
	int cnt = 0;
	int ans = 0;
	int slen = s.length() - 1;
	for (int i = 1; i < slen; i++) {
		if (s[i] == ')' && s[i + 1] == ')') ans += cnt;
		if (s[i] == '(' && s[i - 1] == '(') cnt++;
	}

	cout << ans;
}