#include <iostream>
#include <string>
#include <vector>
#define MAX 31

using namespace std;

string tictactoe[MAX];
int dx[] = {0, 0, -1, 1, -1, -1, 1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N;

bool DFS(int a, int b);

int main(void) {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> tictactoe[i];
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(tictactoe[i][j] != '.') {
                if(DFS(i, j)) return 0;
                else continue;
            }
        }
    }
    
    cout << "ongoing\n";
    return 0;
}

bool DFS(int a, int b) {
    char c = tictactoe[a][b];

    for(int i = 0; i < 8; i++) {
        if(a + 2 * dy[i] < 0 || a + 2 * dy[i] > N || b + 2 * dx[i] < 0 || b + 2 * dx[i] > N) continue;

        if(c == tictactoe[a + dy[i]][b + dx[i]] && c == tictactoe[a + 2 * dy[i]][b + 2 * dx[i]]) {
            cout << c << endl;
            return true;
        }
    }
    return false;
}