#include <iostream>
#include <set>
#include <string>
using namespace std;

int N;
set<string> st;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N;
	while (N--) {
		string s; cin >> s;
		st.insert(s);
	}

	cout << st.size();
}