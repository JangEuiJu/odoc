#include <iostream>
using namespace std;

int T;
int vowel[128];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	vowel['a'] = vowel['e'] = vowel['i'] = vowel['o'] = vowel['u'] = 1;

	cin >> T;
	while (T--) {
		int vcnt = 0, ccnt = 0;
		string s; cin >> s;
		for (auto& l : s) {
			if (vowel[l]) vcnt++;
			else ccnt++;
		}

		if (vcnt > ccnt) cout << s << '\n' << 1 << '\n';
		else cout << s << '\n' << 0 << '\n';
	}
}