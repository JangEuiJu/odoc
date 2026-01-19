#include <bits/stdc++.h>
using namespace std;
 
int n, m, ans[101];
vector<int> v[101];
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
 
    for(int i = 1; i <= n; i++) {
        for(int g = 1; g <= 4; g++) {
            bool flag = 1;
            for(int j = 0; j < v[i].size(); j++)
                if(ans[v[i][j]] == g) flag = 0;
            if(flag) {
                ans[i] = g;
                break;
            }
        }
    }
 
    for(int i = 1; i <= n; i++)
        cout << ans[i];
    cout << '\n';
    return 0;
}
 