#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

string x;
int ans = 0;

int main(){
    cin.tie(0);
    cout.tie(0);
    cin >> x;
    for(int i = 0; i < x.size(); i++){
        if(x[i] == ',') ans++;
    }
    cout << ans + 1;
    return 0;
}