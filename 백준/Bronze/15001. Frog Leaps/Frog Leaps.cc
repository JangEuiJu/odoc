#include <iostream>
using namespace std;
typedef long long ll;

int N;
ll ans, old;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> old; N--;
	while (N--) {
		ll x; cin >> x;
		ans += (x - old) * (x - old);
		old = x;
	}

	cout << ans;
}