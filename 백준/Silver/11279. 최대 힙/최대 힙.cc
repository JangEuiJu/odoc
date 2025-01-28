#include <iostream>
#include <queue>
//37
using namespace std;

int main(void) {
	cin.sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	priority_queue<int> pq;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (num == 0) {
			if (pq.empty())
				cout << 0 << "\n";
			else {
				cout << pq.top() << "\n";
				pq.pop();
			}
		}
		else
			pq.push(num);
	}

	return 0;
}

