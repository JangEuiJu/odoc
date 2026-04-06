#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
bool visited[5][5];
int map[5][5];
int r, c;

int bfs() {
	queue<pair<int, pair<int, int>>> q;
	q.push({ 0, {r, c} });
	visited[r][c] = true;
	while (!q.empty()) {
		int y = q.front().second.first;
		int x = q.front().second.second;
		int time = q.front().first;
		q.pop();
		if (map[y][x] == 1) return time;
		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (0 <= ny && ny <= 4 && 0 <= nx && nx <= 4) {
				if (!visited[ny][nx] && map[ny][nx] != -1) {
					visited[ny][nx] = true;
					q.push({ time + 1, {ny, nx} });
				}
			}
		}
	}
	return -1;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++) {
			cin >> map[i][j];
			visited[i][j] = false;
		}
	cin >> r >> c;
	cout << bfs() << endl;
}