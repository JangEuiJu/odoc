#include <bits/stdc++.h>
using namespace std;
 
char puzzle[4][4], solved[4][4];
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++)
        solved[i][j] = 4 * i + j + 'A';
    for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++)
        cin >> puzzle[i][j];
 
    int ans = 0;
    for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) {
        for(int k = 0; k < 4; k++) for(int l = 0; l < 4; l++) {
            if(puzzle[i][j] == solved[k][l])
                ans += abs(i - k) + abs(j - l);
        }
    }
 
    cout << ans << '\n';
    return 0;
}