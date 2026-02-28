#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <climits>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>

using namespace std;

int N, M;

vector<int> dy = { -1, -1, -1 };
vector<int> dx = { -1, 0, 1 };

const int MAX = 6 * 6 * 100 + 1;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    vector<vector<int>> Board(N, vector<int>(M, 0));
    int dp[7][7][3];
    fill(dp[0][0], dp[6][7], MAX);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> Board[i][j];
        }
    }

    for (int j = 0; j < M; j++)
    {
        for (int k = 0; k < 3; k++)
        {
            dp[0][j][k] = Board[0][j];
        }
    }

    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            for (int k = 0; k < 3; k++)
            {
                int fromY = i + dy[k];
                int fromX = j + dx[k];

                if (fromY < 0 || fromY >= N || fromX < 0 || fromX >= M) continue;

                for (int t = 0; t < 3; t++)
                {
                    if (k == t) continue;

                    if (dp[i][j][k] > dp[fromY][fromX][t] + Board[i][j])
                    {
                        dp[i][j][k] = dp[fromY][fromX][t] + Board[i][j];
                    }
                }
            }
        }
    }

    int ans = INT_MAX;
    for (int j = 0; j < M; j++)
    {
        for (int k = 0; k < 3; k++)
        {
            ans = min(ans, dp[N - 1][j][k]);
        }
    }

    cout << ans;

    return 0;
}