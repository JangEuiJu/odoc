#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int N;
vector<pii> arr;
double ans = 0;

int main()
{
	cin >> N;
	arr.resize(N);

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i].first >> arr[i].second;
	}

	sort(arr.begin(), arr.end());

	for (int i = 1; i < N; i++)
	{
		double distance_diff = abs(arr[i].second - arr[i - 1].second);
		double time_diff = arr[i].first - arr[i - 1].first;

		ans = max(ans, distance_diff / time_diff);
	}

	cout << ans;

	return 0;
}