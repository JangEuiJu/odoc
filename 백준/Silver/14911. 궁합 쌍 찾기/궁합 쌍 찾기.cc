#include <iostream>
#include <vector>
#include <set>
using namespace std;

int N;
vector<int> vec;

set<pair<int, int>> st;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int tmp;
	while (cin >> tmp) {
		vec.emplace_back(tmp);
	}
	N = vec.size() - 1;

	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (vec[i] + vec[j] == vec[N]) {
				if (vec[i] < vec[j]) st.insert(make_pair(vec[i], vec[j]));
				else st.insert(make_pair(vec[j], vec[i]));
			}
		}
	}

	for (auto& p : st) {
		cout << p.first << ' ' << p.second << '\n';
	}

	cout << st.size();
}