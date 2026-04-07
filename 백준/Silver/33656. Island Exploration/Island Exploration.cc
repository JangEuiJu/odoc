#include <iostream>
#include <queue>
using namespace std;

int R, C, sR, sC, ans = 1;
char board[100][100];
int dr[4] = {0,0,1,-1};
int dc[4] = {1,-1,0,0};
queue<pair<int, int>> que;

void bfs() {
    que.push(make_pair(sR, sC));
    board[sR][sC] = '.';
    while (!que.empty()) {
        int r = que.front().first, c = que.front().second; que.pop();
        for (int i = 0; i < 4; i++) {
            int rr = r + dr[i], cc = c + dc[i];
            if (board[rr][cc] != '#') continue;
            board[rr][cc] = '.', ans++;
            que.push(make_pair(rr, cc));
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> R >> C;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cin >> board[r][c];
            if (board[r][c] == 'S') sR = r, sC = c;
        }
    }

    bfs();
    cout << ans;
}