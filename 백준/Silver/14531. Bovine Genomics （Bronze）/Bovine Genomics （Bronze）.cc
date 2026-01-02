#include <bits/stdc++.h>
using namespace std;
 
int N, M, check[200];
char spotty[101][101], plain[101][101];
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> N >> M;
    for(int i = 0; i < N; i++) for(int j = 0; j < M; j++)
        cin >> spotty[i][j];
    for(int i = 0; i < N; i++) for(int j = 0; j < M; j++)
        cin >> plain[i][j];
 
    int ans = 0;
    for(int j = 0; j < M; j++) {
        memset(check, 0, sizeof(check));
        for(int i = 0; i < N; i++)
            check[spotty[i][j]] = 1;
        int flag = 1;
        for(int i = 0; i < N; i++) {
            if(check[plain[i][j]] != 0) {
                flag = 0;
                break;
            }
        }
        if(flag) ans++;
    }
 
    cout << ans << '\n';
    return 0;
}