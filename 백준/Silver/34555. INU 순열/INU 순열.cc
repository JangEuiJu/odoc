#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;

	vector<int> v;
	v.push_back(N);

	for (int i = 1; i < N; i++)
	{
		if (i % 2 == 1)
			v.push_back(v[i - 1] - (N - i));
		else
			v.push_back(v[i - 1] + (N - i));
	}

	reverse(v.begin(), v.end());
	
	for (int x : v)
		cout << x << ' ';

	return 0;
}