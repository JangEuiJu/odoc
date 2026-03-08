#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct info
{
	int day;
	string start;
	string end;
	info(int a, string b, string c)
	{
		day = a;
		start = b;
		end = c;
	}
};

bool cmp(info& i1, info& i2)
{
	if (i1.day < i2.day)
	{
		return true;
	}
	else if (i1.day == i2.day)
	{
		if (i1.end < i2.end)
		{
			return true;
		}
		else if (i1.end == i2.end)
		{
			return i1.start < i2.start;
		}
		else
		{
			return false;
		}
	}
	else
	{
		return false;
	}
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int T, N;
	int day;
	string start, end;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> N;
		vector<info> v;
		int answer = 1;
		for (int i = 0; i < N; i++)
		{
			cin >> day >> start >> end;
			v.push_back(info(day, start, end));
		}
		sort(v.begin(), v.end(), cmp);
		info prev = v.at(0);
		for (int i = 1; i < N; i++)
		{
			if (v.at(i).day == prev.day && v.at(i).start >= prev.end)
			{
				prev = v.at(i);
				answer++;
			}
			else if (v.at(i).day != prev.day)
			{
				answer++;
				prev = v.at(i);
			}
		}
		cout <<"Scenario #"<<t+1<<":" << "\n" << answer << "\n";
		if (t != T - 1)
		{
			cout << "\n";
		}
	}
	return 0;
}