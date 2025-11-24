#include <iostream>
#include <string>
#include <map>
using namespace std;

int N, slen; string sname, s;
map<string, string> mp;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	while (N--) {
		cin >> sname;
		getline(cin, s); s += ' ';
		slen = s.length();
		int L = 1, R = 1;
		while (L < slen) {
			while (s[R] != ' ') {
				s[R] = tolower(s[R]);
				R++;
			}
			mp.insert(make_pair(s.substr(L, R - L), sname));
			R++;
			L = R;
		}
	}

	getline(cin, s);
	while (getline(cin, s)) {
		s += ' ';
		slen = s.length();

		int L = 0, R = 0;
		while (L < slen) {
			while (('A' <= s[R] && s[R] <= 'Z') || ('a' <= s[R] && s[R] <= 'z') || s[R] == '\'' || s[R] == '-') {
				s[R] = tolower(s[R]);
				R++;
			}
			string tmp = s.substr(L, R - L);
			if (mp.count(tmp)) {
				cout << mp[tmp] << '\n';
				break;
			}
			R++;
			L = R;
		}
	}
}