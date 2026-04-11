#include<bits/stdc++.h>

using namespace std;
using ll = long long;

const ll MOD = (ll)1e6;

int main()
{
	ll n;
	cin >> n;

	ll ans = 0;
	for (ll x = 0; x <= n; x++) {
		if (3 * x > n)break;
		ans += (n-3*x) / 2 + 1;
	}
	cout << ans%MOD;
	return 0;
}