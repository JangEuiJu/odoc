#include <iostream>
#include <cstring>
using namespace std;

int N, M;

int cnts[10001];

int main()
{
    ios::sync_with_stdio(0), cin.tie(0);

    cin >> N >> M;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            int num;
            cin >> num;

            ++cnts[num];
        }
    }

    int oddCount = 0;

    for (const int &cnt : cnts)
    {
        if (cnt % 2)
        {
            ++oddCount;
        }
    }

    if (M == 1)
    {
        cout << "YES";
    }
    else
    {
        if (oddCount > N || (oddCount % 2 && N % 2 != 1) || (M % 2 == 0 & oddCount > 0))
        {
            cout << "NO";
        }
        else
        {
            cout << "YES";
        }
    }
    return 0;
}