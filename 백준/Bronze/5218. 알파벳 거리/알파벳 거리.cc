#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cmath>
#include <string>

using namespace std;

int N;

int main(){
    cin.tie(0);
    cin >> N;
    for(int i = 0; i < N; i++){
        string x, y;
        cin >> x >> y;
        cout << "Distances: ";
        for(int j = 0; j < x.length(); j++){
            int X = x[j] - 'A';
            int Y = y[j] - 'A';
            if(Y - X >= 0) cout << Y - X << " ";
            else cout << Y - X + 26 << " ";
        }
        cout << "\n";
    }
    return 0;
}