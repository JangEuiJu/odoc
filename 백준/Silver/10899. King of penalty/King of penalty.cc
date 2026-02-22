#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef struct
{
	long long duration;
	int cnt;
} Result;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int P, N;
	cin >> P >> N;

	vector<int> durations(N);

	for (int i = 0; i < N; i++)
	{
		cin >> durations[i];
	}

	sort(durations.begin(), durations.end());

	int sum = 0;
	int timeLimit = P - 1;

	Result result = { 0, 0 };

	for (int i = 0; i < N && timeLimit >= durations[i]; i++)
	{
		result.duration += timeLimit;
		timeLimit -= durations[i];

		result.cnt++;
	}

	cout << result.cnt << " " << result.duration << "\n";

	return 0;
}